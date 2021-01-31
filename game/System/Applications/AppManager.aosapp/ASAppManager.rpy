# 
# ASAppManager.rpy.rpy
# AliceOS
# 
# Created by Marquis Kurt on 9/9/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

init 10 python:
    class ASAppManager(ASAppRepresentative):
        bundleName = "Менеджер приложений"
        bundleId = "app.aliceos.app-manager"
        bundleDir = AS_DEFAULT_APP_DIR + "AppManager.aosapp/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Подробный просмотр установленных приложений на AliceOS и управление их разрешениями.
        """

        requires = { }

        def applicationWillLaunch(self):
            renpy.show_screen("ASAppManagerView")
            pass

        # Looks for all apps using AppKit and returns a list of them.
        def gatherAllApplications(self):
            import gc
            apps = []
            for obj in gc.get_objects():
                if isinstance(obj, ASAppRepresentative):
                    apps.append(obj)
            return apps

        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "AppManager.aosapp/")

    appManager = ASAppManager()