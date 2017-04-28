# -*- coding: utf-8 -*-
import os


class ScreenSaver:

    @staticmethod
    def lock():
        os.system('xset dpms force off ;xtrlock')
