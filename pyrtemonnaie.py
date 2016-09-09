#!/usr/bin/env python3

import operator
import os

FILEPATH = "database.dat"
FILE_LOADED = False
MENU_FORMAT = "{0:2}-> {1:5}"
CONFIG_FORMAT = "{0:10}: {1:20}"
MENU_OPTIONS = {
                "1": "set filepath",
                "2": "load file",
                "3": "dump file",
                "4": "edit value",
                "5": "save file",
                "9": "print config",
                "q": "quit pyrtemonnaie"
}

def print_menu():
    print("{text:-^25}".format(text="pyrtemonnaie"))

    for option in sorted(MENU_OPTIONS, key=operator.itemgetter(0)):
        print(MENU_FORMAT.format(option, MENU_OPTIONS[option]))

def get_menu_input():
    menu_choice = str(input("  -> "))
    if menu_choice in MENU_OPTIONS.keys() :
        return menu_choice
    else:
        return -1

def set_filepath():
    path = str(input("full path to file: "))
    if os.path.isfile(path):
        global FILEPATH 
        FILEPATH = path
    print_config()

def load_file():
    pass

def dump_file():
    pass

def edit_value():
    pass

def save_file():
    pass

def print_config():
    print(CONFIG_FORMAT.format("path", FILEPATH))
    print()
    input("press any key to continue...")

def run_menu_choice(val):
    if val == -1:
        print("error! input was invalid")
    elif val == "1":
        set_filepath()
    elif val == "2":
        load_file()
    elif val == "3":
        dump_file()
    elif val == "4":
        edit_value()
    elif val == "5":
        save_file()
    elif val == "9":
        print_config()
    elif val == "q":
        exit(0)

os.system("clear") #dirty
while True:
    print_menu()
    run_menu_choice(get_menu_input())
    os.system("clear") #dirty