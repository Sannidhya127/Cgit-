from colored import fg, bg, attr
import re
import readline
import difflib
from difflib import SequenceMatcher, get_close_matches, Differ
from pprint import pprint
import os
import sys
import shutil
import time as t
import pathlib
from colored import fg, bg, attr
import pyttsx3
from datetime import date
from datetime import time
from datetime import datetime
import subprocess
import win32con
import win32api
import winreg as reg


def BackUpFiles():
    try:
        os.mkdir(".cgit")
    except Exception:
        pass
    af = os.listdir()
    for i in af:
        try:
            file = open(i, "r")
            text = file.read()
            currentwd = os.getcwd()
            nfile = open(f"{currentwd}\.cgit\{i}", "w")
            ntext = nfile.write(text)
        except PermissionError:
            print("Please run the program as administrator to track all files")


def Initialize():
    cgit = os.path.exists(".cgit")
    if cgit == True:
        print("Reinitialized repository")
    else:
        os.mkdir(".cgit")
        os.mkdir(".cgit\commits")
        print("Initialized empty repository")


def statusChecker():
    pass


def commit(commitMsg):
    Msg = comd[14::]
    file = open("commits.txt", "a")
    text = file.write(Msg)
    file.close()
    print("Commited succesfully")


if __name__ == "__main__":
    while True:
        d = os.getcwd()
        # comd = input(f"{fg('green_1')}{d}: {attr('reset')}")
        comd = input(f"{d}: ")
        if comd == "cgit add --a":
            BackUpFiles()
        elif comd == "cgit init":
            Initialize()
        elif comd == "cgit status":
            statusChecker()
        elif "cgit commit -m" in comd:
            commit(comd)
        elif comd == "exit":
            exit()
