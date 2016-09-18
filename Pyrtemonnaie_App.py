import operator
import os
import platform
import re
import tkinter
import tkinter.messagebox
import tkSimpleDialog
from collections import namedtuple
from datetime import date
from datetime import datetime
from operator import attrgetter

Datapoint = namedtuple('Datapoint', ['Recipient', 'Date', 'Value', 'Comment'])

class datapoint_ui(tkSimpleDialog.Dialog):
    def body(self, master, datapoint):

        lblfrm_main = tkinter.LabelFrame(master, pady=6, padx=10)
        lblfrm_main.pack()

        lbl_recipient = tkinter.Label(lblfrm_main, text="recipient:", pady=6)
        lbl_recipient.grid(row=0, column=0, sticky="w")
        lbl_date = tkinter.Label(lblfrm_main, text="date:", pady=6)
        lbl_date.grid(row=1, column=0, sticky="w")
        lbl_value = tkinter.Label(lblfrm_main, text="value:", pady=6)
        lbl_value.grid(row=2, column=0, sticky="w")
        lbl_comment = tkinter.Label(lblfrm_main, text="comment:", pady=6)
        lbl_comment.grid(row=3, column=0, sticky="w")

        var_recipient = tkinter.StringVar()
        if datapoint:
            var_recipient.set(datapoint.Recipient)
        else:
            var_recipient.set("")
        self.entry_recipient = tkinter.Entry(lblfrm_main, textvariable=var_recipient)
        self.entry_recipient.grid(row=0, column=1)

        var_date = tkinter.StringVar()
        if datapoint:
            var_date.set(datapoint.Date.strftime("%d.%m.%Y"))
        else:
            var_date.set("")
        self.entry_date = tkinter.Entry(lblfrm_main, textvariable=var_date)
        self.entry_date.grid(row=1, column=1)

        var_value = tkinter.StringVar()
        if datapoint:
            var_value.set(datapoint.Value) 
        else:
            var_value.set("")
        self.entry_value = tkinter.Entry(lblfrm_main, textvariable=var_value)
        self.entry_value.grid(row=2, column=1)

        var_comment = tkinter.StringVar()
        if datapoint:
            var_comment.set(datapoint.Comment) 
        else:
            var_comment.set("")
        self.entry_comment = tkinter.Entry(lblfrm_main, textvariable=var_comment)
        self.entry_comment.grid(row=3, column=1)

        return self.entry_recipient

    def apply(self):
        self.result = self.entry_recipient.get(), self.entry_date.get(), self.entry_value.get(), self.entry_comment.get()

class Pyrtemonnaie_App(tkinter.Frame):

    ############## UI ##############

    def __init__(self, master=None):
        self.Pyrtemonnaie = []
        self.file_path = "database.dat"
        self.file_loaded = False

        tkinter.Frame.__init__(self, master)
        
        self.pack_propagate(0)
        self.menuBar =  tkinter.Menu(master)
        self.createMenuBar()
        master.config(menu=self.menuBar)

        self.listbox_datapoints = tkinter.Listbox(self.master)
        self.listbox_datapoints.pack(fill="both", expand="true", side="left")
        self.scrollbar_datapoints = tkinter.Scrollbar(self.master)
        self.scrollbar_datapoints.pack(fill="y", side="left")

        self.pack()

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
        self.menuPyrtemonnaie.add_command(label="add value", command=self.add_value_handler)
        self.menuPyrtemonnaie.add_command(label="edit value", command=self.edit_value_handler)
        self.menuPyrtemonnaie.add_command(label="delete value")

        self.menuBar.add_cascade(label="file", menu=self.menuFile)
        self.menuBar.add_cascade(label="pyrtemonnaie", menu=self.menuPyrtemonnaie, state="disabled")

############## LOGIC ##############

    def dump_config_handler(self):
        tkinter.messagebox.showinfo("pyrtemonnaie - config", "filepath: {filepath}".format(filepath=self.file_path))

    def date_matches_regex(self, s):
        regex = re.compile(r'\d{2}\.\d{2}\.(\d{4}|\d{2})')
        return regex.match(s)

    def add_value_handler(self):
        new_datapoint = Datapoint("", date.today(), 0.0, "")
        inputView = datapoint_ui(self, title="pyrtemonnaie")
        try:
            new_datapoint = new_datapoint._replace(Recipient=str(inputView.result[0]))
            d = str(inputView.result[1])
            if self.date_matches_regex(d):
                d = d.split(".")
                new_datapoint = new_datapoint._replace(Date=date(int(d[2]), int(d[1]), int(d[0])))
            else:
                raise ValueError            
            new_datapoint = new_datapoint._replace(Value=float(inputView.result[2]))
            new_datapoint = new_datapoint._replace(Comment=str(inputView.result[3]))

            self.Pyrtemonnaie.append(new_datapoint)
            self.Pyrtemonnaie.sort(key=attrgetter('Date'))
            self.dump_pyrtemonnaie_handler()
        except TypeError:
            pass
        except ValueError:
            tkinter.messagebox.showerror("pyrtemonnaie", "invalid value!")

    def edit_value_handler(self):
        try:
            datapoint_idx = self.listbox_datapoints.curselection()[0]
            datapoint = self.Pyrtemonnaie[datapoint_idx]
            inputView = datapoint_ui(self, title="pyrtemonnaie", datapoint=datapoint)
            
            datapoint = datapoint._replace(Recipient=str(inputView.result[0]))
            d = str(inputView.result[1])
            if self.date_matches_regex(d):
                d = d.split(".")
                datapoint = datapoint._replace(Date=date(int(d[2]), int(d[1]), int(d[0])))
            else:
                raise ValueError            
            datapoint = datapoint._replace(Value=float(inputView.result[2]))
            datapoint = datapoint._replace(Comment=str(inputView.result[3]))

            self.Pyrtemonnaie.remove(self.Pyrtemonnaie[datapoint_idx])
            self.Pyrtemonnaie.append(datapoint)
            self.Pyrtemonnaie.sort(key=attrgetter('Date'))
            self.dump_pyrtemonnaie_handler()
        except TypeError:
            pass
        except ValueError:
            tkinter.messagebox.showerror("pyrtemonnaie", "invalid value!")
        except IndexError:
            tkinter.messagebox.showerror("pyrtemonnaie", "No datapoint selected!")

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
            self.dump_pyrtemonnaie_handler()
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
        self.listbox_datapoints.delete(0, self.listbox_datapoints.size())
        for datapoint in self.Pyrtemonnaie:
            self.listbox_datapoints.insert("end", self.print_datapoint(datapoint))

        self.listbox_datapoints["yscrollcommand"] = self.scrollbar_datapoints.set
        self.scrollbar_datapoints["command"] = self.listbox_datapoints.yview

root = tkinter.Tk(className='Pyrtemonnaie')
app = Pyrtemonnaie_App(root)
Pyrtemonnaie_App.mainloop(app)