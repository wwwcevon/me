# -*- coding: utf-8 -*-
import os
import sys
import time
from multiprocessing import Process
from getch import getch

from me.todo.pmt import PMT

MENU_DOC = """
1. Check PMT
q. Exit
Input choice:
"""

def menu():
    if len(sys.argv) == 1:
        interactive()

def interactive():
    clear()
    print(MENU_DOC)
    _ = getch()
    func = select(_)
    if func is None:
        print('Unavailable choice')
        press_any_key_to_continue()
        return
    clear()
    rs = wait(func)
    clear()
    print(rs)
    press_any_key_to_continue()
    interactive()


def select(choice):
    if choice == 'q':
        exit()
    availabes = {
        '1':PMT.do,
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
