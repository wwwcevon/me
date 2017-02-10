# -*- coding: utf-8 -*-
import os


class Browser:

    @staticmethod
    def dingtalk():
        os.system('chromium --app=https://im.dingtalk.com/ &')
