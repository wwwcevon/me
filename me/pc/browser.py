# -*- coding: utf-8 -*-
import os
import subprocess


class Browser:

    @staticmethod
    def dingtalk():
        os.system('chromium --app=https://im.dingtalk.com/ ')

    @staticmethod
    def search():
        proc = subprocess.run(['xclip', '-o'], stdout=subprocess.PIPE)
        to_search = proc.stdout.decode()
        search_command = "chromium 'https://www.google.com/#q=%s'" % to_search
        os.system(search_command)
