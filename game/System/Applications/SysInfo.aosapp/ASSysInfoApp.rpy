#
# ASSysInfoCoreService.rpy
# AliceOS
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init 5 python:

    class ASSysInfoApp(ASAppRepresentative):
        bundleName = "О системе AliceOS"
        bundleId = "app.aliceos.sysinfo"
        bundleDir = AS_DEFAULT_APP_DIR + "SysInfo.aosapp/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Просмотр информации об операционной системе AliceOS.
        """

        requires = { }

        def applicationWillLaunch(self):
            renpy.show_screen("ASSysInfoView")

        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "SysInfo.aosapp/")

    ASSysInfo = ASSysInfoApp()