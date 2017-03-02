# -*- coding: utf-8 -*-
import os


class ScreenSaver:

    @staticmethod
    def lock():
        os.system('xset -display :0 dpms force off ;xtrlock')
