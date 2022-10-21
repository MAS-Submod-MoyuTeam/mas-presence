# config.rpy contains classes and functions for working with presence config
# files as well as stores persistent variables affecting the behavior of
# Discord Presence Submod.
#
# This file is part of Discord Presence Submod (see link below):
# https://github.com/friends-of-monika/discord-presence-submod

default persistent._fom_presence_enabled = True


init 90 python in _fom_presence_config:

    import store

    from store import persistent
    from store import _fom_presence as mod
    from store import _fom_presence_discord as discord
    from store import _fom_presence_error as error
    from store import _fom_presence_logging as logging

    import sys
    import os
    import time

    if sys.version_info.major == 2:
        import ConfigParser as configparser
        import io
    else:
        import configparser


    # Errors and warnings

    _ERROR_CONFIG_LOADING = error.Error(
        log_message_report="Could not load presence config from file {0}: {1}.",
        ui_message_report="Could not load some presence configs, see log/submod_log.log."
    )

    _ERROR_CONFIG_INHERITANCE = error.Error(
        log_message_report="Presence config {0} inherits nonexistent config ID: {1}.",
        ui_message_report="Could not load some presence configs, see log/submod_log.log."
    )


    # Logger

    _logger = logging.DEFAULT


    # Supplier and related functions and constructors

    class _Supplier(object):
        """
        Supplier is a simple utility class that provides a way to dynamically
        access certain data with some input in context.
        """

        def __init__(self, provide_func):
            """
            Creates a new supplier instance with the provided providing
            function.

            IN:
                provide_func -> function:
                    Function that will return requested data.
            """

            self._provide = provide_func

        def get(self, *args, **kwargs):
            """
            Invoke providing function with passed parameters and get result.

            IN:
                *args:
                    Arbitrary positional arguments to pass to function.

            OUT:
                any:
                    Data returned by underlying providing function.
            """

            return self._provide(*args, **kwargs)

    _none_supplier = _Supplier(lambda: None)

    def _substitute_supplier(s):
        """
        Creates a supplier that will performs renpy.substitute on the provided
        string every time its get(...) method is called.

        IN:
            s -> str:
                String to perform substitution on.

        OUT:
            Supplier:
                Supplier that performs substitution on a string.
        """

        def supply():
            return renpy.substitute(s)
        return _Supplier(supply)



    # Timestamps and related functions and variables

    def _datetime_to_int(dt):
        """
        Converts datetime instance to Unix milliseconds timestamp.

        IN:
            dt -> datetime.datetime:
                Datetime to convert.

        OUT:
            int:
        """

        return int(time.mktime(dt.timetuple()) + dt.microsecond / 1000000.0)


    _timestamps_db = dict()
    _timestamps_db["none"] = _none_supplier

    def _parse_ts_supplier(s):
        """
        Parses provided string to retrieve a timestamp supplier from database.

        IN:
            s -> str:
                Timestamp supplier name, case insensitive.

        OUT:
            Supplier:
                Supplier that provides a timestamp.

            None:
                If none found by the specified name.
        """

        return _timestamps_db.get(s.lower())

    def _timestamp_session_start():
        """
        Supplier that provides session begin timestamp.

        OUT:
            int:
                Unix timestamp of session begin.
        """
        return _datetime_to_int(persistent.sessions["current_session_start"])

    _timestamps_db["sessionstart"] = _Supplier(_timestamp_session_start)

    def _timestamp_brb_start():
        brb_ev = store.mas_getEV(brb_evl)
        return brb_ev and brb_ev.last_seen

    def _timestamp_upcoming_event_1h():
        """
        Supplier that provides upcoming event timestamp.

        OUT:
            int:
                Unix timestamp of an upcoming event.

        NOTE:
            Due to Discord limitations regarding timestamps in activity, this
            supplier does not return timestamps for events that are further than
            one hour ahead.
        """

        # NOTE: Discord just won't render timestamps that exceed 1 hour.
        eve = _get_next_event(1)
        if eve is None:
            return None
        if eve[0].total_seconds() > 3600:
            return None
        return int(time.time() + eve[0].total_seconds())
    _timestamps_db["upcomingevent1h"] = _Supplier(_timestamp_upcoming_event_1h)


    # ConfigParser wrapper and related functions and classes

    def _parse_bool(s):
        """
        Parses a string and returns a boolean value for its content.
        Values "true", "yes", "y" (case-insensitive) will be considered True,
        anything else will be False.

        IN:
            s -> str:
                String to parse boolean from.

        OUT:
            True:
                For strings "true", "yes", "y" (case-insensitive.)

            False:
                For any other strings.
        """

        if s.lower() in ("true", "yes", "y"):
            return True
        return False

    if sys.version_info.major == 2:
        def _open_with_encoding(path, mode, encoding="utf-8"):
            """
            Opens file with specified encoding.

            IN:
                path -> str:
                    Path to file to open.

                mode -> str:
                    Mode of file to open, see built-in function open(...)

                encoding -> str, default "utf-8":
                    Encoding to use when reading/writing to file.

            OUT:
                File-like object:
                    File opened in the provided mode with provided encoding.
            """

            return io.open(path, mode, encoding="utf-8")
    else:
        def _open_with_encoding(path, mode, encoding="utf-8"):
            """
            Opens file with specified encoding.

            IN:
                path -> str:
                    Path to file to open.

                mode -> str:
                    Mode of file to open, see built-in function open(...)

                encoding -> str, default "utf-8":
                    Encoding to use when reading/writing to file.

            OUT:
                File-like object:
                    File opened in the provided mode with provided encoding.
            """

            return open(path, mode, encoding="utf-8")

    class _ParserWrapper(object):
        """
        ParserWrapper is a wrapper for ConfigParser that provides get_value(...)
        method for reading strings and deserializing them to proper data types.
        """

        def __init__(self, parser):
            """
            Creates a new instance of ParserWrapper with the provided
            ConfigParser instance to wrap.

            IN:
                parser -> configparser.ConfigParser:
                    ConfigParser instance to wrap.
            """

            self._parser = parser

        def get_value(self, section, value, deserializer=str, default=None):
            """
            Gets value from underlying ConfigParser instance and applies
            deserialization logic on it.

            IN:
                section -> str:
                    Section to load value from.

                value -> str:
                    Key of the value to retrieve.

                deserializer -> function, default str:
                    Deserializer function to apply to retrieved string.

                default -> any, default None:
                    Default value to return if there is no such section/value.
            """

            try:
                return deserializer(self._parser.get(section, value, raw=True))
            except (configparser.NoOptionError, configparser.NoSectionError) as e:
                return default


    # Config object and related functions and variables

    class Config(object):
        """
        Config provides uniform way to access data stored in .conf/.ini/.cfg
        files that is loaded using ParserWrapper and deserializers.
        """

        def __init__(self, parser):
            """
            Creates a new instance of Config with the provided ParserWrapper
            to load values with.

            IN:
                parser -> ParserWrapper:
                    ParserWrapper that will load values from ConfigParser.
            """

            condition = parser.get_value("Presence", "Condition")
            if condition is not None:
                condition = condition.strip()
                if len(condition) > 0:
                    compile(condition, "<string>", "eval")
                else:
                    condition = None
            self.condition = condition

            self.priority = parser.get_value("Presence", "Priority", int, 0)
            self.dynamic = parser.get_value("Presence", "Dynamic", _parse_bool, True)
            self.id = parser.get_value("Presence", "ID", str, None)
            self.inherit_id = parser.get_value("Presence", "Inherit", str, None)

            self.app_id = parser.get_value("Client", "ApplicationID", int)

            self.details = parser.get_value("Activity", "Details", _substitute_supplier, _none_supplier)
            self.state = parser.get_value("Activity", "State", _substitute_supplier, _none_supplier)

            self.large_image = parser.get_value("Assets", "LargeImage")
            self.large_text = parser.get_value("Assets", "LargeText", _substitute_supplier, _none_supplier)
            self.small_image = parser.get_value("Assets", "SmallImage")
            self.small_text = parser.get_value("Assets", "SmallText", _substitute_supplier, _none_supplier)

            self.start_ts = parser.get_value("Timestamps", "Start", _parse_ts_supplier, _none_supplier)
            self.stop_ts = parser.get_value("Timestamps", "End", _parse_ts_supplier, _none_supplier)

            self._activity = None
            self._inherit_applied = False

        @staticmethod
        def from_file(path):
            """
            Loads Config from path.

            IN:
                path -> str:
                    Path to config file.

            OUT:
                Config:
                    Config loaded from file.
            """

            c = configparser.ConfigParser()
            with _open_with_encoding(path, "r", encoding="utf-8") as f:
                c.readfp(f, path.replace("\\", "/").split("/")[:-1])
            return Config(_ParserWrapper(c))

        def inherit(self, config, force=False):
            """
            Copies values from another config (only omitted, None or
            _none_supplier values) over to this config. Unless force parameter
            is set to True, does nothing on next call.

            IN:
                config -> Config:
                    Config to copy values from. Inherit method is not called,
                    inheritance is not done recursively by this method, users
                    should care about this themselves.

                force -> bool, default False:
                    If True, skips inheritance status checks and applies values
                    over again.
            """

            if self._inherit_applied and not force:
                return

            if self.app_id is None:
                self.app_id = config.app_id
            if self.details is _none_supplier:
                self.details = config.details
            if self.state is _none_supplier:
                self.state = config.state
            if self.large_image is None:
                self.large_image = config.large_image
            if self.large_text is _none_supplier:
                self.large_text = config.large_text
            if self.small_image is None:
                self.small_image = config.small_image
            if self.small_text is _none_supplier:
                self.small_text = config.small_text
            if self.start_ts is _none_supplier:
                self.start_ts = config.start_ts
            if self.stop_ts is _none_supplier:
                self.stop_ts = config.stop_ts

            self._inherit_applied = True

        @property
        def inherited(self):
            """
            Returns inheritance status flag value.

            OUT:
                True:
                    If this config has inherited from other config.

                False:
                    If this config has not inherited from another config.
            """

            return self._inherit_applied

        def to_activity(self):
            """
            Creates Activity instance from the values stored in Config.
            If dynamic property is set to False this is only evaluated once,
            stored in _activity and then retrieved from it on next call, not
            re-evaluating suppliers and not building fresh Activity.

            OUT:
                Activity:
                    Activity based on properties this Config instance has.
            """

            if self._activity is not None:
                return self._activity
            a = discord.Activity()

            if self.state is not None:
                a.state = self.state.get()
            if self.details is not None:
                a.details = self.details.get()

            if self.start_ts is not None:
                a.timestamps.start = self.start_ts.get()
            if self.stop_ts is not None:
                a.timestamps.end = self.stop_ts.get()

            if self.large_image is not None:
                a.assets.large_image = self.large_image
                if self.large_text is not None:
                    a.assets.large_text = self.large_text.get()
            if self.small_image is not None:
                a.assets.small_image = self.small_image
                if self.small_text is not None:
                    a.assets.small_text = self.small_text.get()

            if not self.dynamic:
                self._activity = a
            return a


    _config_dir = os.path.join(mod.basedir, "config")
    _configs = list()
    _config_id_map = dict()

    def reload_configs():
        """
        Clears global _configs variable and populates it with new valid configs.

        NOTE:
            All errors will be reported using Error objects in global current
            error context. Reported errors are not resolved on successful loads.
        """

        del _configs[:]
        _config_id_map.clear()

        for _dir, _, files in os.walk(_config_dir):
            for _file in files:
                if not (
                    _file.endswith(".ini") or
                    _file.endswith(".cfg") or
                    _file.endswith(".conf")
                ):
                    continue

                try:
                    _file = os.path.join(_dir, _file)
                    config = Config.from_file(_file)
                    if config.condition is not None:
                        eval(config.condition, dict(), store.__dict__)

                    _configs.append((_file, config))
                    if config.id is not None:
                        if not config.id in _config_id_map or config.priority > _config_id_map[config.id].priority:
                            _logger.info("Config {0} has existing ID and higher priority over existing config {1}, overriding.".format(_file[len(_config_dir) + 1:], e))
                            _config_id_map[config.id] = config

                except Exception as e:
                    _ERROR_CONFIG_LOADING.report(_file[len(_config_dir) + 1:], e)

        # Once configs are loaded, we now copy inherited values.
        def inherit(config):
            # Prevent loops and infinite recursions.
            if config.inherited:
                return True

            if config.inherit_id is not None:
                parent = _config_id_map.get(config.inherit_id)
                if parent is None:
                    _ERROR_CONFIG_INHERITANCE.report(_file[len(_config_dir) + 1:], config.inherit_id)
                    return False

                # Inheritance is done recursively.
                if not inherit(parent):
                    return False
                config.inherit(parent)

            return True

        idx = 0
        while idx < len(_configs):
            _file, config = _configs[idx]
            if not inherit(config):
                del _configs[idx]
            else:
                idx += 1

        # Sort configs on reload to save precious time on every loop.
        _configs.sort(key=lambda it: it[1].priority, reverse=True)

    def get_active_config():
        """
        Evaluates conditions in configs in global Ren'Py scope and returns
        config with the highest priority of all configs which conditions
        evaluated to True.

        NOTE:
            All errors will be reported using Error objects in global current
            error context. Reported errors are not resolved on successful loads.
        """

        for _file, conf in _configs:
            if conf.condition is not None:
                try:
                    if bool(eval(conf.condition, dict(), store.__dict__)):
                        return conf
                except Exception as e:
                    _ERROR_CONFIG_LOADING.report(_file[len(_config_dir) + 1:], e)

        return None

    def get_config(_id):
        """
        Fetches config by its ID (defined as ID= parameter in Presence section).

        IN:
            _id -> str:
                ID of the config to fetch reference to.

        OUT:
            Config:
                If config with such ID exists and was successfully loaded.

            None:
                If config with such ID does not exist.
        """

        return _config_id_map.get(_id)
