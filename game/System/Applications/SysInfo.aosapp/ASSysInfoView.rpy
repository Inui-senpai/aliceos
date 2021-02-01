#
# ASSysInfoView.rpy
# AliceOS
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init offset = 10

screen ASSysInfoView():
    style_prefix "ASInterface"
    frame:
        xmaximum 800

        has vbox:
            xalign 0.5
            yalign 0.5

            use ASInterfaceTitlebar("О системе AliceOS", onClose=Hide("ASSysInfoView"))

            hbox:
                spacing 32

                add ASSysInfoApp.bundleDir + "Resources/Elements/SystemIcon.png":
                    size (256, 256)
                    xoffset 16

                vbox:
                    text "AliceOS {=ASSysInfoTitle_text_nobold}[AS_SYS_INFO[COMMON_NAME]]{/}":
                        style "ASSysInfoTitle_text"
                    text "Версия [AS_SYS_INFO[VERSION]] ([AS_SYS_INFO[BUILD_ID]])":
                        style "ASSysInfoVersion_text"
                    null height 16
                    text "{=ASSysInfoProperty_text_bold}Сделано для Ren'Py{/} [renpy.version_only]":
                        style "ASSysInfoProperty_text"
                    null height 24
                    text "Перевод на русский язык: MtnDewSmoker420, специально для RG Smoking Room."
                    null height 32
                    text "© 2018-2019 Project Alice.\nAliceOS является свободным программным обеспечением с открытым исходным кодом, лицензированным по условиям лицензии BSD 2-го типа.":
                        style "ASSysInfoCopyright_text"
                        yalign 1.0
