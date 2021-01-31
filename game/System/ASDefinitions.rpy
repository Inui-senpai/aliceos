# 
# ASDefinitions.rpy
# AliceOS
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init -1000:

    # MARK: OS release definitions
    # These definitions are used as a means of identifying the current
    # version of AliceOS provided with a 
    define AS_SYS_INFO = {
        "VERSION": "2.0.0",
        "COMMON_NAME": "Prospect Park",
        "BUILD_ID": "GITHASH"
    }

    # MARK: OS directory definitions
    # Define system-wide directories here. These definitions are used
    # to prevent re-typing common directory locations.
    define AS_SYSTEM_DIR = "System/"
    define AS_FRAMEWORKS_DIR = "System/Frameworks/"
    define AS_CORESERVICES_DIR = "System/CoreServices/"
    define AS_DEFAULT_APP_DIR = "System/Applications/"
    define AS_FONTS_DIR = "System/Library/Fonts/"
    define AS_APPS_DIR = "Applications/"
    define AS_LIBRARY_DIR = "System/Library/"

    init python:
        
        # Get the framework directory from the framework name. This function
        # is intended to prevent re-typing of framework locations for typical
        # AliceOS frameworks.
        def AS_FRAMEWORK_DIR(FRAMEWORK_NAME="Default"):
            return AS_FRAMEWORKS_DIR + FRAMEWORK_NAME + ".aosframework/"

    # MARK: OS permissions definitions
    define AS_REQUIRES_NOTIFICATIONKIT = "REQ_NOTIFICATIONKIT"
    define AS_REQUIRES_FULL_DISK_ACCESS = "REQ_FULL_DISK"
    define AS_REQUIRES_SYSTEM_EVENTS = "REQ_SYSTEM_EVENTS"


    # MARK: OS permissions strings
    define AS_REQUIRE_NOTIFKIT_NAME = "Отправлять уведомления"
    define AS_REQUIRE_NOTIFKIT_DESC = "Уведомления могут включать в себя баннеры, предупреждения и звуки. Это можно настроить в Менеджере приложений."
    define AS_REQUIRE_FDA_NAME = "Доступ к файлам"
    define AS_REQUIRE_FDA_DESC = "Доступ к файлам может включать в себя вашу Домашнюю папку и директорию вашей установленной копии AliceOS. Это можно настроить в Менеджере приложений."
    define AS_REQUIRE_SYSEV_NAME = "Управлять настройками AliceOS"
    define AS_REQUIRE_SYSEV_DESC = "Доступ к настройкам может включать в себя параметры специальных возможностей, системные события и её конфигурацию. Это можно настроить в Менеджере приложений."

    # MARK: OS permissions enumerations
    define AS_REQUIRE_PERMS_NAME = {
        AS_REQUIRES_NOTIFICATIONKIT: AS_REQUIRE_NOTIFKIT_NAME,
        AS_REQUIRES_FULL_DISK_ACCESS: AS_REQUIRE_FDA_NAME,
        AS_REQUIRES_SYSTEM_EVENTS: AS_REQUIRE_SYSEV_NAME
    }

    define AS_REQUIRE_PERMS_DESC = {
        AS_REQUIRES_NOTIFICATIONKIT: AS_REQUIRE_NOTIFKIT_DESC,
        AS_REQUIRES_FULL_DISK_ACCESS: AS_REQUIRE_FDA_DESC,
        AS_REQUIRES_SYSTEM_EVENTS: AS_REQUIRE_SYSEV_DESC
    }
