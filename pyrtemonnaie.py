#!/usr/bin/env python3

import operator
import os
from Datapoint import Datapoint

FILE_PATH = "database.dat"
FILE_LOADED = False
DATAPOINTS = []
MENU_FORMAT = "{0:2}-> {1:5}"
CONFIG_FORMAT = "{0:10}: {1:20}"
MENU_OPTIONS = {
                "1": "set filepath",
                "2": "load file",
                "3": "dump pyrtemonnaie",
                "4": "add value",
                "5": "edit value",
                "6": "delete value",
                "7": "save file",
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
    global DATAPOINTS
    global FILE_LOADED

    if len(DATAPOINTS) > 0:
        print("""  -> warning! some datapoints are already loaded.
        if you contine, changes will be overwritten!""")
        confirm_load = ""

        while not(confirm_load == "y" or confirm_load == "n"):
            confirm_load = str(input("  -> press y to continue, n to abort :"))
            if confirm_load == "n":
                return

    try:
        file_object = open(FILE_PATH, "r")
        for line in file_object:
            d = Datapoint()
            d.parse(line)
            DATAPOINTS.append(d)
        file_object.close()
        print("  -> file loaded ...")
        FILE_LOADED = True
    except ValueError:
        print("  -> error loading file! please check its contents")
    except IndexError:
        print("  -> error loading file!\n'{line}' has missing arguments".format(line=line.rstrip()))

def dump_file():
    print()
    print("{text:-^25}".format(text="file content"))
    print()
    for datapoint in DATAPOINTS:
        print(datapoint.to_String())
    print()

def add_value():
    pass

def edit_value():
    def refresh_and_print_header():
        refresh_screen()
        print("{text:-^25}".format(text="datapoints"))
        print()
    
    while True:
        refresh_and_print_header()
        try:
            for datapoint in DATAPOINTS:
                print(MENU_FORMAT.format(DATAPOINTS.index(datapoint)+1, datapoint.to_String()))
            print()
        except ValueError:
            print("  -> error! invalid datapoint!")
            return
        
        try:
            select_datapoint = str(input("  -> index of datapoint to be editted, any other key to quit: "))
            if select_datapoint == "q":
                return
            else:
                select_datapoint = int(select_datapoint)
            if select_datapoint > len(DATAPOINTS):
                raise ValueError
        except ValueError:
            return

        refresh_and_print_header()
        datapoint = DATAPOINTS[select_datapoint-1]
        print(MENU_FORMAT.format("1", datapoint.Recipient))
        print(MENU_FORMAT.format("2", datapoint.Date))
        print(MENU_FORMAT.format("3", datapoint.Value))
        print(MENU_FORMAT.format("4", datapoint.Comment))
        print(MENU_FORMAT.format("a", "abort"))
        print()

        try:
            select_property = int(input("  -> index of property to be editted: "))
            if select_property > 4:
                raise ValueError
        except ValueError:
            print("  -> error! invalid input!")
            input("  -> datapoint was changed! press any key to continue ...")
            return

        datapoint_split = datapoint.to_String().split(";")
        new_property = str(input("     {old_value} -> ".format(old_value=datapoint_split[select_property-1]))).strip()

        try:
            if select_property == 1:
                datapoint.Recipient = new_property
                print("  -> recipient was changed to: {recipient}".format(recipient=new_property))
            if select_property == 2:
                datapoint.Date = new_property
                print("  -> date was changed to: {date}".format(date=new_property))
            if select_property == 3:
                datapoint.Value = new_property
                print("  -> value was changed to: {value}".format(value=new_property))
            if select_property == 4:
                datapoint.Comment = new_property
                print("  -> comment was changed to:\n{comment}".format(comment=new_property))

            DATAPOINTS[select_datapoint-1] = datapoint
            input("  -> datapoint was changed! press any key to continue ...")
            
        except ValueError:
            print("  -> error! invalid input!")

def delete_value():
    pass

def save_file():
    refresh_screen()
    print("{text:-^25}".format(text="save pyrtemonnaie"))
    print()
    print(MENU_FORMAT.format("1", "save"))
    print(MENU_FORMAT.format("2", "save as"))
    print(MENU_FORMAT.format("a", "abort"))

    try:
        select_save_option = str(input("  -> save option: ")) 
        if select_save_option == "a":
            return
        else:
            select_save_option = int(select_save_option)
        if select_save_option > 2:
            raise ValueError
    except ValueError:
        input("  -> error! invalid input! press any key to continue ...")
        return
    
    if select_save_option == 1:
        try:
            file_object = open(FILE_PATH, "w")
            for datapoint in DATAPOINTS:
                file_object.write(datapoint.to_String() + "\n")
            file_object.close()
        except ValueError:
            input("  -> error! could not write to file {file}! press any key to continue ...".format(file=FILE_PATH))
            return
    if select_save_option == 2:
        pass
    

def print_config():
    print(CONFIG_FORMAT.format("path", FILE_PATH))

def print_error_file_not_loaded():
    print("  -> error! you have to load a file first. return to the main menu and hit load a file.")

def refresh_screen():
    os.system("clear") #dirty

def run_menu_choice(val):
    if val == -1:
        print("error! input was invalid")
    elif val == "1":
        set_filepath()
    elif val == "2":
        load_file()
    elif val == "3":
        if FILE_LOADED:
            dump_file()
        else:
            print_error_file_not_loaded()
    elif val == "4":
        if FILE_LOADED:
            add_value()
        else:
            print_error_file_not_loaded()
    elif val == "5":
        if FILE_LOADED:
            edit_value()
        else:
            print_error_file_not_loaded()
    elif val == "6":
        if FILE_LOADED:
            delete_value()
        else:
            print_error_file_not_loaded()
    elif val == "7":
        if FILE_LOADED:
            save_file()
        else:
            print_error_file_not_loaded()
    elif val == "9":
        print_config()
    elif val == "q":
        exit(0)

# main

refresh_screen()
while True:
    print_menu()
    run_menu_choice(get_menu_input())
    input("press any key to continue ...")
    refresh_screen()