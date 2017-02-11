# -*- coding: utf-8 -*-
import os
import sys
import time
from multiprocessing import Process
from getch import getch

from me.todo.pmt import PMT
from me.pc.screen_saver import ScreenSaver
from me.pc.browser import Browser
from me.pc.wm import WM

MENU_DOC = """
Check P̱MT
Ḻock screen
Ḏingtalk
S̱earch in Google
O̱pen promgram

Input choice, q to exit ...
"""

def menu():
    if len(sys.argv) == 1:
        interactive()
    else:
        func = select(sys.argv[1])
        if func is None:
            exit()
        rs = func(*sys.argv[2:])
        if type(rs) is str:
            print(rs)

def interactive():
    clear()
    print(MENU_DOC)
    _ = getch()
    func = select(_)
    if func is None:
        print('Unavailable choice')
        press_any_key_to_continue()
        interactive()
    clear()
    rs = wait(func)
    if rs is None:
        exit()
    clear()
    print(rs)
    press_any_key_to_continue()
    interactive()


def select(choice):
    if choice == 'q':
        exit()
    availabes = {
        'p':PMT.check,
        'l':ScreenSaver.lock,
        'd':Browser.dingtalk,
        's':Browser.search,
        'o':WM.switch_or_open,
        'q':exit
    }
    func = availabes.get(choice, None)
    return func

def press_any_key_to_continue():
    print('Press any key to continue...')
    getch()
    clear()

def wait(func):
    def print_wait():
        print('Please wait', end='\r')
        count = 0
        while p.is_alive():
            time.sleep(0.5)
            count += 1
            print('Please wait'+'.'*count+'     ', end='\r')
            if count == 5:
                count = 0
    p = Process(target=print_wait)
    p.start()
    rs = func()
    p.terminate()
    return rs

def clear():
    os.system('clear')
