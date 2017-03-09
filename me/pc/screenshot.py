# -*- coding: utf-8 -*-
import os


class Screenshot:

    @staticmethod
    def area():
        os.system('gnome-screenshot -a -f /home/kevin/Desktop/screenshot.jpeg')

