# -*- coding: utf-8 -*-
import os


class WM:

    @staticmethod
    def switch_or_open(name=None):
        if name is None:
            name = input()
        os.system('wmctrl -x -a "{}" || {}'.format(name, name))
