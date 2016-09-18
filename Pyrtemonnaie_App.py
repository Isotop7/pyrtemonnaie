import operator
import os
import platform
import re
import tkinter
import tkinter.messagebox
from collections import namedtuple
from datetime import date
from datetime import datetime
from operator import attrgetter

Datapoint = namedtuple('Datapoint', ['Recipient', 'Date', 'Value', 'Comment'])

class Pyrtemonnaie_App(tkinter.Frame):

    ############## UI ##############

    def __init__(self, master=None):
        self.Pyrtemonnaie = []
        self.file_path = "database.dat"
        self.file_loaded = False

        tkinter.Frame.__init__(self, master)
        
        self.menuBar =  tkinter.Menu(master)
        self.createMenuBar()
        master.config(menu=self.menuBar)

        #self.createSetFilePathDialog()
        #self.pack()

    def createMenuBar(self):
        self.menuFile = tkinter.Menu(self.menuBar, tearoff=False)
        self.menuFile.add_command(label="load pyrtemonnaie", command=self.load_file_handler)
        self.menuFile.add_command(label="save")
        self.menuFile.add_command(label="save as")
        self.menuFile.add_separator()
        self.menuFile.add_command(label="dump config", command=self.dump_config_handler)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="quit", command=self.quit)

        self.menuPyrtemonnaie = tkinter.Menu(self.menuBar, tearoff=False)
        self.menuPyrtemonnaie.add_command(label="dump pyrtemonnaie", command=self.dump_pyrtemonnaie_handler)
        self.menuPyrtemonnaie.add_separator()
        self.menuPyrtemonnaie.add_command(label="add value")
        self.menuPyrtemonnaie.add_command(label="edit value")
        self.menuPyrtemonnaie.add_command(label="delete value")

        self.menuBar.add_cascade(label="file", menu=self.menuFile)
        self.menuBar.add_cascade(label="pyrtemonnaie", menu=self.menuPyrtemonnaie, state="disabled")

############## LOGIC ##############

    def dump_config_handler(self):
        tkinter.messagebox.showinfo("pyrtemonnaie - config", "filepath: {filepath}".format(filepath=self.file_path))
        

    def load_file_handler(self):

        def _activate_menu():
            self.menuBar.entryconfigure(2, state="active")
            self.file_loaded = True

        if len(self.Pyrtemonnaie) > 0:
            if tkinter.messagebox.askyesno("pyrtemonnaie", "Some datapoints are already loaded. If you continue, changes will be overwritten!"):
                self.file_loaded = False
            else:
                return            

        try:
            file_object = open(self.file_path, "r")
            for line in file_object:
                if line.isspace() == False:
                    d = self.parse_line(line)
                    self.Pyrtemonnaie.append(d)
            file_object.close()
            print("  -> file loaded ...")
            _activate_menu()
        except ValueError:
            tkinter.messagebox.showerror("pyrtemonnaie", "error loading file! please check its contents")
            print("  -> error loading file! please check its contents")
        except IndexError:
            tkinter.messagebox.showerror("pyrtemonnaie", "error loading file!\n'{line}' has missing arguments".format(line=line.rstrip()))
            print("  -> error loading file!\n'{line}' has missing arguments".format(line=line.rstrip()))
        except FileNotFoundError:
            tkinter.messagebox.showerror("pyrtemonnaie", "file {path} is not found. Add datapoints and save to create it.".format(path=self.file_path))
            input("  -> file {path} is not found. Add datapoints and save to create it.".format(path=self.file_path))
            _activate_menu()  


    def date_matches_regex(self, s):
        regex = re.compile(r'\d{2}\.\d{2}\.(\d{4}|\d{2})')
        return regex.match(s)

    def parse_line(self, s):
        def parse_line_date(s_date):
            try:
                if self.date_matches_regex(s_date):
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

    def print_datapoint(self, datapoint):
        return ("{recipient};{date};{value};{comment}".format(
            recipient=datapoint.Recipient, 
            date=datapoint.Date.strftime("%d.%m.%Y"),
            value=datapoint.Value,
            comment=datapoint.Comment
            ))

    def dump_pyrtemonnaie_handler(self):
        listbox_datapoints = tkinter.Listbox(self.master)
        listbox_datapoints.pack(fill="both", expand="true", side="left")
        scrollbar_datapoints = tkinter.Scrollbar(self.master)
        scrollbar_datapoints.pack(fill="y", side="left")
        for datapoint in self.Pyrtemonnaie:
            listbox_datapoints.insert("end", self.print_datapoint(datapoint))

        listbox_datapoints["yscrollcommand"] = scrollbar_datapoints.set
        scrollbar_datapoints["command"] = listbox_datapoints.yview

root = tkinter.Tk()
app = Pyrtemonnaie_App(root)
Pyrtemonnaie_App.mainloop(app)
