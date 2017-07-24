# -*- coding: utf-8 -*-
import os


class Screenshot:

    @staticmethod
    def area():
        os.system('maim -st 0 | xclip -selection clipboard -t image/png')

