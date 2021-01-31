# 
# ASDesktopCoreService.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init 5 python:

    class ASDesktopCoreService(ASCoreServiceRepresentative):
        bundleName = "Рабочий стол"
        bundleId = "app.aliceos.core-services.desktop"
        bundleDir = AS_CORESERVICES_DIR + "Desktop.aoscservice/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Рабочий стол предоставляет быстрый доступ ко всем приложениям в AliceOS.
        """

        # Looks for all apps using AppKit and returns a list of them.
        def gatherAllApplications(self):
            import gc
            apps = []
            for obj in gc.get_objects():
                if isinstance(obj, ASAppRepresentative):
                    apps.append(obj)
            return apps

        def gatherCurrentTime(self):
            from datetime import datetime
            now = datetime.now()
            weekday = now.weekday()
            weekdays = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
            return now.strftime("{w}, %H:%M").format(w=weekdays[weekday])

        def _callDesktop(self):
            renpy.call_screen("ASDesktopShellView")

        def showDesktop(self):
            renpy.show_screen("ASDesktopShellView")

        def showTopBar(self):
            renpy.call_screen("ASDesktopTopBar")

        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Desktop.aoscservice/")

    ASDesktop = ASDesktopCoreService()
