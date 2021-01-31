# 
# ASAppManagerView.rpy
# AliceOS
# 
# Created by Marquis Kurt on 9/9/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

screen ASAppManagerView():
    style_prefix "ASInterface"

    python:
        apps = appManager.gatherAllApplications()

    default currentAppView = None

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 900
        ysize 600

        has vbox:
            xalign 0.5
            yfit True

            use ASInterfaceTitlebar("Менеджер приложений", onClose=Hide("ASAppManagerView"))

            hbox:
                style_prefix "ASAppManager"
                spacing 8

                vbox:
                    spacing 8
                    label "Приложения"

                    viewport:
                        style_prefix "ASInterfaceScrollbar"
                        mousewheel True
                        scrollbars "vertical"
                        style "ASAppManager_viewport"

                        vbox:
                            for app in apps:
                                button action SetScreenVariable("currentAppView", app):
                                    ymaximum 56
                                    xsize 300
                                    has hbox:
                                        spacing 8

                                        add app.icons[48]
                                        vbox:
                                            text "[app.bundleName]":
                                                style "ASAppManager_AppName_text"
                                            text "[app.bundleAuthor]"


                vbox:
                    xfill True
                    if currentAppView == None:
                        text "Выберите приложение из списка слева, чтобы просмотреть его свойства.":
                            xalign 0.5


                    else:
                        hbox:
                            spacing 12

                            add currentAppView.icons[128]:
                                zoom 0.9

                            vbox:
                                label "[currentAppView.bundleName]":
                                    style "ASAppManager_DetailedAppName"
                                text "[currentAppView.bundleAuthor]":
                                    style "ASAppManager_DetailedAppAuthor_text"
                                text "Версия [currentAppView.bundleVersion] ([currentAppView.bundleId])"
                                null height 8

                                textbutton "Запустить" action Function(currentAppView.applicationWillLaunch):
                                    style "ASInterfacePushButton"

                        null height 8

                        vbox:
                            $ currentAppView_description = currentAppView.bundleDescription.strip()
                            text "Об этом приложении":
                                style "ASAppManager_DetailedEmphasis_text"
                            text "[currentAppView_description]"
                            null height 16

                            if currentAppView.requires:

                                text "Разрешить приложению:":
                                    style "ASAppManager_DetailedEmphasis_text"

                                vbox:
                                    style_prefix "ASInterfaceCheckbox"
                                    spacing 8

                                    if AS_REQUIRES_NOTIFICATIONKIT in currentAppView.requires:
                                        textbutton "Отправлять уведомления" action ToggleDict(persistent.AS_PERMISSIONS[currentAppView.bundleId], AS_REQUIRES_NOTIFICATIONKIT, True, False)
                                        text "Уведомления могут включать в себя баннеры, предупреждения и звуки.":
                                            style "ASAppManager_text"

                                    if AS_REQUIRES_FULL_DISK_ACCESS in currentAppView.requires:
                                        textbutton "Доступ к файлам" action ToggleDict(persistent.AS_PERMISSIONS[currentAppView.bundleId], AS_REQUIRES_FULL_DISK_ACCESS, True, False)
                                        text "Доступ к файлам может включать в себя вашу Домашнюю папку и директорию вашей установленной копии AliceOS.":
                                            style "ASAppManager_text"

                                    if AS_REQUIRES_SYSTEM_EVENTS in currentAppView.requires:
                                        textbutton "Изменять настройки и отслеживать системные события" action ToggleDict(persistent.AS_PERMISSIONS[currentAppView.bundleId], AS_REQUIRES_SYSTEM_EVENTS, True, False)
                                        text "Это может включать в себя изменение настроек AliceOS и/или отслеживание таких системных событий, как запуск.":
                                            style "ASAppManager_text"
                            else:
                                text "Разрешения для этого приложения не требуются."
