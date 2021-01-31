# 
# ASHaltMessage.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init screen ASHaltMessage(error=""):
    tag ASHaltMessage
    zorder 500
    modal True
    
    on "show":
        action [
                Function(SetThumbnailFull),
                FileTakeScreenshot(),
                Function(SetThumbnailOriginal)
                ]

    add FileCurrentScreenshot()

    frame at ASDynamicBlurTransition:
        style "ASDynamicBlurFrame"
        xfill True
        yfill True

        vbox:
            xalign 0.5
            yalign 0.5
            xsize 700
            
            add ASHalt.bundleDir + "Resources/Elements/HaltSymbol.png":
                xalign 0.5
            
            null height 8
            
            vbox:
                xfill True
                spacing 10
            
                text "Систему AliceOS необходимо перезапустить, поскольку возникла критическая ошибка.":
                    style "ASHaltMessageTitle"
                    xalign 0.5
                text "Вы можете найти подробности об ошибке в Базе данных ошибок, открыв сайт https://errordb.aliceos.app или отсканировав QR-код ниже. Система автоматически перезапустится через 10 секунд.":
                    style "ASHaltMessageDetails"
                    xalign 0.5
            
            null height 32
            
            add ASHalt.bundleDir + "Resources/Elements/QRCode.png":
                xalign 0.5
            
            null height 16
            
            text error:
                style "ASHaltMessageCode"
                xalign 0.5

    timer 10.0 action Return()
