#!/usr/bin/env python3

import operator
import os
import platform
import re
from collections import namedtuple
from datetime import date
from datetime import datetime
from operator import attrgetter

Datapoint = namedtuple('Datapoint', ['Recipient', 'Date', 'Value', 'Comment'])
FILE_LOADED = False
FILE_PATH = "database.dat"
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

def set_filepath():
    try:
        path = str(input("full path to file: "))
        if path.isspace():
            raise ValueError
        elif len(path) == 0:
            raise ValueError
        elif os.path.isfile(path):
            print("  -> filepath set ...")
            return path
    except ValueError:
        input("  -> error! path invalid!")

def date_matches_regex(s):
    regex = re.compile(r'\d{2}\.\d{2}\.(\d{4}|\d{2})')
    return regex.match(s)

def parse_line(s):
    def parse_line_date(s_date):
        try:
            if date_matches_regex(s_date):
                s_date = s_date.split(".")
                return date(int(s_date[2]), int(s_date[1]), int(s_date[0]))
            else:
                raise ValueError
        except ValueError and TypeError:
            return date.today()

    def parse_line_value(s_value):
        if float(s_value) < 0:
            return 0.0
        else:
            return float(s_value)

    def parse_line_comment(s_comment):
        if ";" in s_comment:
            return ""
        else:
            return s_comment.rstrip()

    try:
        s = s.split(";")
        if len(s) == 4:
            return Datapoint(s[0], parse_line_date(s[1]), parse_line_value(s[2]), parse_line_comment(s[3]))
        else:
            raise IndexError
    except IndexError:
        return Datapoint("", date.today(), 0.0, "")

def load_file(pyrtemonnaie):
    global FILE_PATH

    if len(pyrtemonnaie) > 0:
        print("  -> warning! some datapoints are already loaded. If you continue, changes will be overwritten!")
        confirm_load = ""

        while not(confirm_load == "y" or confirm_load == "n"):
            confirm_load = str(input("  -> press y to continue, n to abort: "))
            if confirm_load == "n":
                return True

    try:
        file_object = open(FILE_PATH, "r")
        for line in file_object:
            if line.isspace() == False:
                d = parse_line(line)
                pyrtemonnaie.append(d)
        file_object.close()
        print("  -> file loaded ...")
        return True
    except ValueError:
        print("  -> error loading file! please check its contents")
    except IndexError:
        print("  -> error loading file!\n'{line}' has missing arguments".format(line=line.rstrip()))
    except FileNotFoundError:
        input("  -> file {path} is not found. Add datapoints and save to create it.".format(path=FILE_PATH))
        return True                

def print_datapoint(datapoint):
    return ("{recipient};{date};{value};{comment}".format(
            recipient=datapoint.Recipient, 
            date=datapoint.Date.strftime("%d.%m.%Y"),
            value=datapoint.Value,
            comment=datapoint.Comment
            ))

def dump_datapoints(pyrtemonnaie):
    print()
    print("{text:-^25}".format(text="file content"))
    print()
    for datapoint in pyrtemonnaie:
        print(print_datapoint(datapoint))
    print()

def add_value(pyrtemonnaie):
    new_datapoint = Datapoint("", date.today(), 0.0, "")

    def refresh_and_print_header():
        refresh_screen()
        print("{text:-^25}".format(text="add value"))
        print()
        print(ADD_VALUE_FORMAT.format("1", "recipient", new_datapoint.Recipient))
        print(ADD_VALUE_FORMAT.format("2", "date", new_datapoint.Date.strftime("%d.%m.%Y")))
        print(ADD_VALUE_FORMAT.format("3", "value", new_datapoint.Value))
        print(ADD_VALUE_FORMAT.format("4", "comment", new_datapoint.Comment))
        print()
        print(MENU_FORMAT.format("a", "abort"))
        print(MENU_FORMAT.format("s", "save"))

    def save_add_value(pyrtemonnaie):
        pyrtemonnaie.append(new_datapoint)
        pyrtemonnaie.sort(key=attrgetter('Date'))
        return

    def edit_property(datapoint, val_index):
        if val_index == "1":
            datapoint = datapoint._replace(Recipient=str(input("  recipient -> ")))
        elif val_index == "2":
            d = input("  date -> ")
            if date_matches_regex(d):
                d = d.split(".")
                datapoint = datapoint._replace(Date=date(int(d[2]), int(d[1]), int(d[0])))
            else:
                raise ValueError            
        elif val_index == "3":
            datapoint = datapoint._replace(Value=float(input("  value -> ")))
        elif val_index == "4":
            datapoint = datapoint._replace(Comment=str(input("  comment -> ")))
        return datapoint
    
    while True:
        refresh_and_print_header()
        try:
            select_property = str(input("  -> index of property to be editted: "))
            if select_property == "a":
                return pyrtemonnaie
            elif select_property == "s":
                save_add_value(pyrtemonnaie)
                return pyrtemonnaie
            elif 0 < int(select_property) <= 4:
                new_datapoint = edit_property(new_datapoint, select_property)
            else:
                raise ValueError
        except ValueError or TypeError:
            input("  -> error! invalid input!")
            return pyrtemonnaie

def get_datapoint_choice(pyrtemonnaie):
    try:
        for idx, datapoint in enumerate(pyrtemonnaie):
            print(MENU_FORMAT.format(str(idx+1), print_datapoint(datapoint)))
        print()
    except ValueError:
        print("  -> error! invalid datapoint!")
        return -1
        
    try:
        select_datapoint = str(input("  -> index of datapoint to be editted, any other key to quit: "))
        select_datapoint = int(select_datapoint)
        if select_datapoint > len(pyrtemonnaie):
            return -1
        else:
            return select_datapoint
    except ValueError:
        return 0

def edit_value(pyrtemonnaie):
    def refresh_and_print_header():
        refresh_screen()
        print("{text:-^25}".format(text="edit value"))
        print()
    
    while True:
        refresh_and_print_header()
        select_datapoint = get_datapoint_choice(pyrtemonnaie)
        if select_datapoint == -1:
            print("  -> error! invalid input!")
            return pyrtemonnaie
        elif select_datapoint == 0:
            return pyrtemonnaie

        refresh_and_print_header()
        datapoint = pyrtemonnaie[(select_datapoint-1)]
        print(MENU_FORMAT.format("1", datapoint.Recipient))
        print(MENU_FORMAT.format("2", datapoint.Date.strftime("%d.%m.%Y")))
        print(MENU_FORMAT.format("3", datapoint.Value))
        print(MENU_FORMAT.format("4", datapoint.Comment))
        print()
        print(MENU_FORMAT.format("a", "abort"))
        print()

        try:
            select_property = int(input("   -> index of property to be editted: "))
            if select_property > 4:
                raise ValueError
        except ValueError:
            input("   -> error! invalid input! press any key to continue ...")
            continue

        new_property = str(input("   new value -> "))

        try:
            if select_property == 1:
                datapoint = datapoint._replace(Recipient=new_property)
                print("   -> recipient was changed to: {recipient}".format(recipient=new_property))
            elif select_property == 2:
                if date_matches_regex(new_property):
                    d = new_property.split(".")
                    datapoint = datapoint._replace(Date=date(int(d[2]), int(d[1]), int(d[0])))
                    print("   -> date was changed to: {date}".format(date=new_property))
                else:
                    raise ValueError            
            elif select_property == 3:
                datapoint = datapoint._replace(Value=float(new_property))
                print("   -> value was changed to: {value}".format(value=new_property))
            elif select_property == 4:
                datapoint = datapoint._replace(Comment=new_property)
                print("   -> comment was changed to:\n{comment}".format(comment=new_property))

            pyrtemonnaie[(select_datapoint-1)] = datapoint
            input("   -> datapoint was changed! press any key to continue ...")
            
        except ValueError:
            print("   -> error! invalid input!")

def delete_value(pyrtemonnaie):

    refresh_screen()
    print("{text:-^25}".format(text="delete value"))
    print()

    datapoint_choice = get_datapoint_choice(pyrtemonnaie)
    if datapoint_choice == -1:
        return
    else:
        d = pyrtemonnaie.Datapoint(datapoint_choice-1) 
        print("  Following object is going to be deleted: {obj}".format(obj=d.to_String()))
        ans = input("  (y/n) -> ")
        if ans == "y":
            pass
        else:
            return

def save_file(pyrtemonnaie):
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
            for datapoint in pyrtemonnaie.Datapoints:
                file_object.write(datapoint.to_String() + "\n")
            file_object.close()
        except ValueError:
            input("  -> error! could not write to file {file}! press any key to continue ...".format(file=FILE_PATH))
            return
    if select_save_option == 2:
        pass
    

def print_config(pyrtemonnaie):
    print(CONFIG_FORMAT.format("path", pyrtemonnaie.Path))

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

def run_menu_choice(val, Pyrtemonnaie):
    global FILE_LOADED
    global FILE_PATH

    try:
        if val == -1:
            raise ValueError
        elif val == "1":
            FILE_PATH = set_filepath()
        elif val == "2":
            FILE_LOADED = load_file(Pyrtemonnaie)
        elif val == "3":
            if FILE_LOADED:
                dump_datapoints(Pyrtemonnaie)
            else:
                print_error_file_not_loaded()
        elif val == "4":
            if FILE_LOADED:
                Pyrtemonnaie = add_value(Pyrtemonnaie)
            else:
                print_error_file_not_loaded()
        elif val == "5":
            if FILE_LOADED:
                Pyrtemonnaie = edit_value(Pyrtemonnaie)
            else:
                print_error_file_not_loaded()
        elif val == "6":
            if FILE_LOADED:
                delete_value(pyrtemonnaie)
            else:
                print_error_file_not_loaded()
        elif val == "7":
            if FILE_LOADED:
                save_file(pyrtemonnaie)
            else:
                print_error_file_not_loaded()
        elif val == "9":
            print_config(pyrtemonnaie)
        elif val == "q":
            exit(0)
        return Pyrtemonnaie
    except ValueError:
        print("error! input was invalid")

# main

def main():
    Pyrtemonnaie = []
    refresh_screen()
    while True:
        print_menu()
        Pyrtemonnaie = run_menu_choice(get_menu_input(), Pyrtemonnaie)
        input("press any key to continue ...")
        refresh_screen()

if __name__ == '__main__': 
    main()