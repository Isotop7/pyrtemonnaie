#!/usr/bin/env python3

FILEPATH = "database.dat"
FILE_LOADED = False

def print_menu():
    menu_format = "{0:2}->{1:5}"
    print("{text:-^25}".format(text="pyrtemonnaie"))
    print(menu_format.format("1", "set filepath"))
    print(menu_format.format("2", "load file"))
    if(FILE_LOADED):
        print(menu_format.format("3", "dump file"))
        print(menu_format.format("4", "edit value"))
        print(menu_format.format("5", "save file"))
    print()
    print(menu_format.format("q", "quit pyrtemonnaie"))

print_menu()