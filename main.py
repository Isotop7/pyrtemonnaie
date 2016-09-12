#!/usr/bin/env python3

import operator
import os
import platform
from Datapoint import Datapoint
from Pyrtemonnaie import Pyrtemonnaie

FILE_PATH = "database.dat"
FILE_LOADED = False
MENU_FORMAT = "{0:2}-> {1:5}"
ADD_VALUE_FORMAT = "{0:2}) {1:10} -> {2:20}"
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

def set_filepath(pyrtemonnaie):
    try:
        path = str(input("full path to file: "))
        if path.isspace():
            raise ValueError
        elif len(path) == 0:
            raise ValueError
        elif os.path.isfile(path):
            pyrtemonnaie.Path = path
            print("  -> filepath set ...")
    except ValueError:
        input("  -> error! path invalid!")

def load_file(pyrtemonnaie):
    global FILE_LOADED

    if pyrtemonnaie.Count > 0:
        print("  -> warning! some datapoints are already loaded. If you continue, changes will be overwritten!")
        confirm_load = ""

        while not(confirm_load == "y" or confirm_load == "n"):
            confirm_load = str(input("  -> press y to continue, n to abort :"))
            if confirm_load == "n":
                return

    try:
        file_object = open(FILE_PATH, "r")
        for line in file_object:
            if line.isspace() == False:
                pyrtemonnaie.add_datapoint(line)
        file_object.close()
        print("  -> file loaded ...")
        FILE_LOADED = True
    except ValueError:
        print("  -> error loading file! please check its contents")
    except IndexError:
        print("  -> error loading file!\n'{line}' has missing arguments".format(line=line.rstrip()))
    except FileNotFoundError:
        input("  -> file {path} is not found. Add datapoints and save to create it.".format(path=FILE_PATH))
        FILE_LOADED = True                

def dump_datapoints(pyrtemonnaie):
    print()
    print("{text:-^25}".format(text="file content"))
    print()
    for datapoint in pyrtemonnaie.Datapoints:
        print(datapoint.to_String())
    print()

def add_value(pyrtemonnaie):
    new_datapoint = Datapoint()

    def refresh_and_print_header():
        refresh_screen()
        print("{text:-^25}".format(text="add value"))
        print()
        print(ADD_VALUE_FORMAT.format("1", "recipient", new_datapoint.Recipient))
        print(ADD_VALUE_FORMAT.format("2", "date", new_datapoint.Date))
        print(ADD_VALUE_FORMAT.format("3", "value", new_datapoint.Value))
        print(ADD_VALUE_FORMAT.format("4", "comment", new_datapoint.Comment))
        print()
        print(MENU_FORMAT.format("a", "abort"))
        print(MENU_FORMAT.format("s", "save"))

    def save_add_value(pyrtemonnaie):
        pyrtemonnaie.add_datapoint(new_datapoint)
        pyrtemonnaie.sort_by_date()
        return

    def edit_property(val_index):
        if val_index == "1":
            new_datapoint.Recipient = str(input("  recipient -> "))
        elif val_index == "2":
            new_datapoint.Date = str(input("  date -> "))
        elif val_index == "3":
            new_datapoint.Value = float(input("  value -> "))
        elif val_index == "4":
            new_datapoint.Comment = str(input("  comment -> "))
        else:
            return
    
    while True:
        refresh_and_print_header()
        try:
            select_property = str(input("  -> index of property to be editted: "))
            if select_property == "a":
                return
            elif select_property == "s":
                save_add_value(pyrtemonnaie)
                return
            elif 0 < int(select_property) <= 4:
                edit_property(select_property)
            else:
                raise ValueError
        except ValueError:
            input("  -> error! invalid input!")

def get_datapoint_choice(pyrtemonnaie):
    try:
        for datapoint in pyrtemonnaie.Datapoints:
            print(MENU_FORMAT.format(DATAPOINTS.index(datapoint)+1, datapoint.to_String()))
        print()
    except ValueError:
        print("  -> error! invalid datapoint!")
        return -1
        
    try:
        select_datapoint = str(input("  -> index of datapoint to be editted, any other key to quit: "))
        select_datapoint = int(select_datapoint)
        if select_datapoint > pyrtemonnaie.Count:
            raise ValueError
        else:
            return select_datapoint
    except ValueError:
        return -1

def edit_value():
    def refresh_and_print_header():
        refresh_screen()
        print("{text:-^25}".format(text="edit value"))
        print()
    
    while True:
        refresh_and_print_header()
        select_datapoint = get_datapoint_choice()
        if select_datapoint == -1:
            print("  -> error! invalid input!")
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
            input("  -> error! invalid input! press any key to continue ...")
            continue

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
    global DATAPOINTS

    refresh_screen()
    print("{text:-^25}".format(text="delete value"))
    print()

    datapoint_choice = get_datapoint_choice()
    if datapoint_choice == -1:
        return
    else:
        d = DATAPOINTS[datapoint_choice-1]
        print("  Following object is going to be deleted: {obj}".format(obj=d.to_String()))
        ans = input("  (y/n) -> ")
        if ans == "y":
            DATAPOINTS.remove(d)
        else:
            return

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
    sys = platform.system()
    if sys == "Linux":
        os.system("clear")
    elif sys == "Windows":
        os.system("cls")
    elif sys == "Darwin":
        os.system("clear")
    else:
        pass    

def run_menu_choice(val, pyrtemonnaie):
    if val == -1:
        print("error! input was invalid")
    elif val == "1":
        set_filepath()
    elif val == "2":
        load_file()
    elif val == "3":
        if FILE_LOADED:
            dump_datapoints()
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

def main():
    refresh_screen()
    pyrtemonnaie = Pyrtemonnaie()
    while True:
        print_menu()
        run_menu_choice(get_menu_input(), pyrtemonnaie)
        input("press any key to continue ...")
        refresh_screen()

if __name__ == '__main__': 
    main()