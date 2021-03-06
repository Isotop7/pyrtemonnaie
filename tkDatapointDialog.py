from tkinter import Toplevel, Frame, Button, ACTIVE, LEFT

class Dialog(Toplevel):

    def __init__(self, parent, title=None, datapoint=None):
        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body, datapoint)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)

    def body(self, master, datapoint):
        pass

    def buttonbox(self):
        box = Frame(self)

        btn = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        btn.pack(side=LEFT, padx=5, pady=5)
        btn = Button(box, text="Cancel", width=10, command=self.cancel)
        btn.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set()
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def validate(self):
        return 1

    def apply(self):
        pass