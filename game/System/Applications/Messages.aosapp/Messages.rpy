# 
# Messages.rpy
# AliceOS
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init 10 python:
    class ASMessages(ASAppRepresentative):
        bundleName = "Сообщения"
        bundleId = "app.aliceos.messages"
        bundleDir = AS_DEFAULT_APP_DIR + "Messages.aosapp/"
        bundleAuthor = "Project Alice"
        bundleVersion = "2.0.0"
        bundleDescription = """\
            Отправка и получение сообщений между вами и вашими любимыми персонажами в игре.
        """

        requires = {
            AS_REQUIRES_NOTIFICATIONKIT
        }
        
        def receiveMessage(self, fromPerson, message):
            return self.applicationWillRequestNotification(message=fromPerson, withDetails=message)

        def applicationShouldRequestNotification(self):
            return True

        def applicationWillLaunch(self):
            self.applicationWillRequestBasicAlert("Приложение «Сообщения» не готово", "У вас по-прежнему будет возможность получать сообщения от персонажей в игре, но не будет возможности отправлять их.")
            return

        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "Messages.aosapp/")

    messages = ASMessages()
