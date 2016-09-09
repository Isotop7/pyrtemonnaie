#!/usr/bin/env python3

import operator
import os

FILE_PATH = "database.dat"
FILE_LOADED = False
FILE_CONTENT = ""
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
        global FILE_PATH 
        FILE_PATH = path
    print("  -> filepath set ...")

def load_file():
    global FILE_CONTENT
    file_object = open(FILE_PATH, "r")
    for line in file_object:
        FILE_CONTENT = FILE_CONTENT + line
    file_object.close()
    print("  -> file loaded ...")

def dump_file():
    print()
    print("{text:-^25}".format(text="file content"))
    print()
    print(FILE_CONTENT)
    print()

def edit_value():
    pass

def save_file():
    pass

def print_config():
    print(CONFIG_FORMAT.format("path", FILE_PATH))

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
    input("press any key to continue ...")
    os.system("clear") #dirty