translate chinese python in _fom_presence_config:

    # Errors and warnings

    _ERROR_CONFIG_LOADING = error.Error(
        log_message_report="无法从 {0} 加载配置: {1}.",
        ui_message_report="有些配置加载失败了, 请查看 log/submod_log.log."
    )

    _ERROR_CONFIG_INHERITANCE = error.Error(
        log_message_report="配置 {0} 继承了一个不存在的配置 ID: {1}.",
        ui_message_report="有些配置加载失败了, 请查看 log/submod_log.log."
    )

    _ERROR_CONFIG_OVERRIDE = error.Error(
        log_message_report="配置 {0} 覆盖了一个不存在的配置 ID: {1}.",
        ui_message_report="有些配置加载失败了, 请查看 log/submod_log.log."
    )

    _WARNING_CONFIG_CLASH = error.Error(
        log_message_report="配置 {0} 与其他配置的名称冲突: {1}.",
        ui_message_report="在加载配置是出现了警告, 请查看 log/submod_log.log.",
        warning=True
    )