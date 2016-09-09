#!/usr/bin/env python3

import operator

FILEPATH = "database.dat"
FILE_LOADED = False
MENU_FORMAT = "{0:2}->{1:5}"
MENU_OPTIONS = {
                "1": "set filepath",
                "2": "load file",
                "3": "dump file",
                "4": "edit value",
                "5": "save file",
                "q": "quit pyrtemonnaie"
}

def print_menu():
    print("{text:-^25}".format(text="pyrtemonnaie"))

    for option in sorted(MENU_OPTIONS, key=operator.itemgetter(0)):
        print(MENU_FORMAT.format(option, MENU_OPTIONS[option]))

def get_menu_input():
    choice = str(input("-> "))
    if(choice in MENU_OPTIONS.keys()):
        return choice
    else:
        return -1

print_menu()
choice = get_menu_input()