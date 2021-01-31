# 
# ASSetupAssistantCoreService.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init 5 python:
    
    class ASSetupAssistantCoreService(ASCoreServiceRepresentative):
        bundleName = "Мастер установки"
        bundleId = "app.aliceos.core-services.setup-assitant"
        bundleDir = AS_CORESERVICES_DIR + "Setup.aoscservice/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Быстрая настройка AliceOS для дальнейшей конфигурации.
        """
        
        def getFromElements(self, filename):
            return self.bundleDir + "Resources/Elements/" + filename

        def runStep(self, title, instruction, typeInput=False, complete=False):
            return renpy.call_screen("ASSetupAssistantView", title=title, instructions=instruction, useInputMethod=typeInput, completed=complete)
        
        def startSetup(self, express=True, disclaimer=None):
            persistent.AS_COMPLETED_SETUP = False
            if not express:
                self.runStep("Добро пожаловать в AliceOS", "Добро пожаловать в мастер установки AliceOS. Мастер поможет вам настроить такие важные части AliceOS, как ваше имя пользователя, и урегулировать любые юридические соглашения.\n\nДля продолжения нажмите «Далее».")
                self.runStep("Знайте свои права", "AliceOS является свободным программным обеспечением с открытым исходным кодом, лицензированным под условиями лицензии BSD. Эта лицензия позволяет вам и создателю игры модифицировать AliceOS в любом ключе без необходимости спрашивать разрешения.\n\nВерсия BSD-лицензии должна быть включена в пакет AliceOS; в противном случае, посетите сайт {b}https://opensource.org/licenses/BSD-2-Clause{/b} и свяжитесь с разработчиком игры, дабы тот добавил лицензию.")
            if disclaimer != None:
                self.runStep("Лицензионное соглашение", "Издатель вашей игры попросил вас прочитать следующую информацию и согласиться с любыми условиями.\n\n" + disclaimer)
            persistent.playername = self.runStep("Создайте своё имя пользователя", "Введите имя пользователя, которое вы хотите использовать в среде AliceOS. Это имя также будет отображаться в качестве имени вашего персонажа, если применимо.", typeInput=True)
            if not express:
                self.runStep("Установка завершена", "Мастер установки завершил все необходимые задачи, и система AliceOS готова к использованию.\n\nПодробности о системе AliceOS, примечания к данному релизу, и всё то, что вы можете делать с ним, можно найти на сайте {b}https://aliceos.app{/b}.\n\nСпасибо, что выбрали AliceOS. Для выхода из мастера установки нажмите «Завершить».", complete=True)
            persistent.AS_COMPLETED_SETUP = True
            return persistent.playername

        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Setup.aoscservice/")
    
    ASSetup = ASSetupAssistantCoreService()
