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
        ui_message_report="在加载配置时有一些警告，请查看 log/submod_log.log.",
        warning=True
    )

translate chinese python in _fom_presence:

    _ERROR_SOCKET_NOT_FOUND = error.Error(
        log_message_report="无法连接到 Discord Rich Presence. Discord是否在本地运行? (不是在浏览器中）",
        log_message_resolve="与Discord Rich Presence建立连接"
    )

    _ERROR_CLIENT_CONNECTION = error.Error(
        log_message_report="无法连接到 Discord RPC: {0}.",
        log_message_resolve="与Discord Rich Presence建立连接.",
        ui_message_report="无法与 Discord 建立连接.",
        ui_message_resolve="与Discord Rich Presence建立连接."
    )

    _ERROR_CLIENT_TIMEOUT = error.Error(
        log_message_report="与Discord Rich Presence建立连接超时.",
        log_message_resolve="与Discord Rich Presence建立连接.",
        ui_message_report="Discord连接超时, 将于 {0} 秒后重新尝试连接.".format(int(_TIMEOUT_LOCK_DURATION.total_seconds())),
        ui_message_resolve="与Discord Rich Presence建立连接."
    )

    _ERROR_CLIENT_PINGING = error.Error(
        log_message_report="与 Discord 断开连接: {0}.",
        log_message_resolve="与Discord Rich Presence重新建立连接.",
        ui_message_report="与 Discord 断开连接. 尝试重新建立连接...",
        ui_message_resolve="与Discord Rich Presence重新建立连接."
    )

    _ERROR_CLIENT_ACTIVITY = error.Error(
        log_message_report="无法设置discord活动状态: {0}",
        ui_message_report="无法设置discord活动状态."
    )

translate chinese strings:
    old "Enable Discord Rich Presence."
    new "启用 Discord Rich Presence"

    old "Forcibly reconnect to Discord Rich Presence."
    new "强行重新连接到 Discord Rich Presence."

    old "Forcibly reload presence activity."
    new "强制重新加载 Discord 活动状态"

    old "Reload presence configs."
    new "强制重新加载配置文件"