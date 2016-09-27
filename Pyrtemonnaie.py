import re
import sys
from collections import namedtuple
from datetime import date
from operator import attrgetter

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ui.Pyrtemonnaie_MainWindow_ui import Ui_MainWindow

Datapoint = namedtuple('Datapoint', ['Recipient', 'Date', 'Value', 'Comment'])

class Pyrtemonnaie(QMainWindow):
    def __init__(self):
        super(Pyrtemonnaie, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tv_dataset

        self.Pyrtemonnaie = []
        self.file_path = "database.dat"
        self.file_loaded = False

        self.ui.actionOpenPyrtemonnaie.triggered.connect(self.triggerOpenPyrtemonnaie)
        self.ui.actionSavePyrtemonnaie.triggered.connect(self.triggerSavePyrtemonnaie)
        self.ui.actionSaveAsCsv.triggered.connect(self.triggerSaveAsCsv)
        self.ui.actionSaveAsSqlite.triggered.connect(self.triggerSaveAsSqlite)
        self.ui.actionShowConfig.triggered.connect(self.triggerShowConfig)
        self.ui.actionAddDatapoint.triggered.connect(self.triggerAddDatapoint)
        self.ui.actionEditDatapoint.triggered.connect(self.triggerEditDatapoint)
        self.ui.actionDeleteDatapoint.triggered.connect(self.triggerDeleteDatapoint)
        self.ui.actionShowPyrtemonnaie.triggered.connect(self.triggerShowPyrtemonnaie)
        self.ui.actionExit.triggered.connect(self.triggerExit)
    
        self.show()

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

    def date_matches_regex(self, s):
        regex = re.compile(r'\d{2}\.\d{2}\.(\d{4}|\d{2})')
        return regex.match(s)

    def load_data_to_tv(self):
        self.ui.tv_dataset.setModel(QStandardItemModel())
        elements = len(self.Pyrtemonnaie)
        model = QStandardItemModel(elements, 4, self.ui.tv_dataset)
        model.setHorizontalHeaderLabels(["Recipient", "Date", "Value", "Comment"])
        for row in range(elements):
            item = QStandardItem(self.Pyrtemonnaie[row].Recipient)
            model.setItem(row, 0, item)
            item = QStandardItem(self.Pyrtemonnaie[row].Date.strftime("%d.%m.%Y"))
            model.setItem(row, 1, item)
            item = QStandardItem(str(self.Pyrtemonnaie[row].Value))
            model.setItem(row, 2, item)
            item = QStandardItem(self.Pyrtemonnaie[row].Comment)
            model.setItem(row, 3, item)
        self.ui.tv_dataset.setModel(model)

    def triggerOpenPyrtemonnaie(self):

        def _activate_menu():
            self.ui.menuPyrtemonnaie.setEnabled(True)
            self.file_loaded = True

        if len(self.Pyrtemonnaie) > 0:
            confirm = QMessageBox.warning(self, "Pyrtemonnaie", "Es sind bereits Daten geladen. Wenn Sie fortfahren werden Ihre Änderungen eventuell überschrieben!", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.file_loaded = False
                self.Pyrtemonnaie.clear()
            else:
                return            

        try:
            self.file_path = QFileDialog.getOpenFileName(self, "Open Pyrtemonnaie",  self.file_path)[0]
            file_object = open(self.file_path, "r")
            for line in file_object:
                if line.isspace() == False:
                    d = self.parse_line(line)
                    self.Pyrtemonnaie.append(d)
            file_object.close()
            _activate_menu()
            self.load_data_to_tv()
        except ValueError:
            QMessageBox.critical("Pyrtemonnaie", "Fehler beim Laden der Datei! Bitte überprüfen Sie den Dateiinhalt.", QMessageBox.Ok)
        except IndexError:
            QMessageBox.critical("Pyrtemonnaie", "Fehler beim Laden der Datei!\n'{line}\n' ist fehlerhaft.".format(line=line.rstrip()), QMessageBox.Ok)

    def print_datapoint(self, datapoint):
        return ("{recipient};{date};{value};{comment}".format(
            recipient=datapoint.Recipient, 
            date=datapoint.Date.strftime("%d.%m.%Y"),
            value=datapoint.Value,
            comment=datapoint.Comment
            ))

    def triggerSavePyrtemonnaie(self):
        try:
            save_path = QFileDialog.getSaveFileName(self, "Save Pyrtemonnaie", self.file_path)[0]
            file_object = open(save_path, "w")
            for datapoint in self.Pyrtemonnaie:
                file_object.write(self.print_datapoint(datapoint) + "\n")
            file_object.close()
        except ValueError:
            QMessageBox.critical("Pyrtemonnaie", "Datei {file} konnte nicht geschrieben werden!".format(file=save_path), QMessageBox.Ok)
        except FileNotFoundError:
            QMessageBox.critical("Pyrtemonnaie", "Datei {file} konnte nicht gefunden werden!".format(file=save_path), QMessageBox.Ok)

    def triggerSaveAsCsv(self):
        pass

    def triggerSaveAsSqlite(self):
        pass

    def triggerShowConfig(self):
        pass

    def triggerAddDatapoint(self):
        pass

    def triggerEditDatapoint(self):
        pass

    def triggerDeleteDatapoint(self):
        pass

    def triggerShowPyrtemonnaie(self):
        pass
    
    def triggerExit(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    ex = Pyrtemonnaie()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()