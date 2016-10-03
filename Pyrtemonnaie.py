import re
import sys
from collections import namedtuple
from datetime import date
from operator import attrgetter

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import (QStandardItemModel, QStandardItem, QRegExpValidator)

from ui.Pyrtemonnaie_MainWindow_ui import Ui_MainWindow

Datapoint = namedtuple('Datapoint', ['Recipient', 'Date', 'Value', 'Comment'])

class Pyrtemonnaie(QMainWindow):
    def __init__(self):
        super(Pyrtemonnaie, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Pyrtemonnaie = []
        self.file_path = "database.dat"
        self.file_loaded = False

        self.ui.actionOpenPyrtemonnaie.triggered.connect(self.triggerOpenPyrtemonnaie)
        self.ui.actionSavePyrtemonnaie.triggered.connect(self.triggerSavePyrtemonnaie)
        self.ui.actionSaveAsCsv.triggered.connect(self.triggerSaveAsCsv)
        self.ui.actionSaveAsSqlite.triggered.connect(self.triggerSaveAsSqlite)
        self.ui.actionShowConfig.triggered.connect(self.triggerShowConfig)
        self.ui.actionExit.triggered.connect(self.triggerExit)

        self.ui.bbox_New.button(QDialogButtonBox.Save).clicked.connect(self.triggerNewDatapointSave)
        self.ui.bbox_New.button(QDialogButtonBox.Reset).clicked.connect(self.triggerNewDatapointReset)

        self.ui.bbox_Edit.button(QDialogButtonBox.Save).clicked.connect(self.triggerEditDatapointSave)
        self.ui.cb_Edit_Property.currentIndexChanged.connect(self.triggerEditDatapointChanged)
        self.ui.cb_Edit_Dataset.currentIndexChanged.connect(self.triggerEditDatapointChanged)

        self.ui.tabWidget.currentChanged.connect(self.triggerTabViewChange)
    
        self.show()

    def strToDatapoint(self, s):
        try:
            s_split = s.split("=")
            Recipient = s_split[1].split(",")[0].strip("'")
            Date = s_split[2]
            Date = Date[Date.find("(")+1:Date.rfind(")")]
            Date = date(int(Date.split(",")[0].strip()), int(Date.split(",")[1].strip()), int(Date.split(",")[2].strip()))
            Value = float(s_split[3][0:s_split[3].find(",")])
            Comment = s_split[4][1:-2]
            return Datapoint(Recipient, Date, Value, Comment)
        except Exception as w:
            print(w)

    def parse_line_date(self, s_date):
        try:
            if self.date_matches_regex(s_date):
                s_date = s_date.split(".")
                return date(int(s_date[2]), int(s_date[1]), int(s_date[0]))
            else:
                raise ValueError
        except ValueError and TypeError:
            return date.today()

    def parse_line(self, s):
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
                return Datapoint(s[0], self.parse_line_date(s[1]), parse_line_value(s[2]), parse_line_comment(s[3]))
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
            self.ui.tabWidget.setEnabled(True)
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
            QMessageBox.critical(self, "Pyrtemonnaie", "Fehler beim Laden der Datei! Bitte überprüfen Sie den Dateiinhalt.", QMessageBox.Ok)
        except IndexError:
            QMessageBox.critical(self, "Pyrtemonnaie", "Fehler beim Laden der Datei!\n'{line}\n' ist fehlerhaft.".format(line=line.rstrip()), QMessageBox.Ok)

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
            QMessageBox.critical(self, "Pyrtemonnaie", "Datei {file} konnte nicht geschrieben werden!".format(file=save_path), QMessageBox.Ok)
        except FileNotFoundError:
            QMessageBox.critical(self, "Pyrtemonnaie", "Datei {file} konnte nicht gefunden werden!".format(file=save_path), QMessageBox.Ok)

    def triggerSaveAsCsv(self):
        pass

    def triggerSaveAsSqlite(self):
        pass

    def triggerShowConfig(self):
        QMessageBox.information(self,"Pyrtemonnaie", "Dateipfad: {filepath}".format(filepath=self.file_path), QMessageBox.Ok)

    def triggerNewDatapointSave(self):
        new_datapoint = Datapoint("", date.today(), 0.0, "")
        try:
            new_recipient = self.ui.le_New_Recipient.text()
            new_date = self.ui.le_New_Date.text()
            new_value = self.ui.le_New_Value.text()
            new_comment = self.ui.le_New_Comment.text()
            new_datapoint = new_datapoint._replace(Recipient=str(new_recipient))
            d = str(new_date)
            if self.date_matches_regex(d):
                d = d.split(".")
                new_datapoint = new_datapoint._replace(Date=date(int(d[2]), int(d[1]), int(d[0])))
            else:
                raise ValueError            
            new_datapoint = new_datapoint._replace(Value=float(new_value))
            new_datapoint = new_datapoint._replace(Comment=str(new_comment))

            self.Pyrtemonnaie.append(new_datapoint)
            self.Pyrtemonnaie.sort(key=attrgetter('Date'))
            self.load_data_to_tv()
        except TypeError:
            pass
        except ValueError:
            QMessageBox.critical(self, "Pyrtemonnaie", "Fehlerhafte Eingabe!", QMessageBox.Ok)


    def triggerNewDatapointReset(self):
        self.ui.le_New_Recipient.setText("")
        self.ui.le_New_Date.setText("")
        self.ui.le_New_Value.setText("")
        self.ui.le_New_Comment.setText("")

    def triggerEditDatapointChanged(self):
        try:
            current_element = self.ui.cb_Edit_Dataset.currentText()
            idx = self.Pyrtemonnaie.index(self.strToDatapoint(current_element))
            prop = self.ui.cb_Edit_Property.currentText()
            if prop == "Recipient" or prop == "Comment":
                self.ui.le_Edit_Property_Old.setText(getattr(self.Pyrtemonnaie[idx], prop))
            elif prop == "Date":
                self.ui.le_Edit_Property_Old.setText(self.Pyrtemonnaie[idx].Date.strftime("%d.%m.%Y"))
            elif prop == "Value":
                self.ui.le_Edit_Property_Old.setText(str(self.Pyrtemonnaie[idx].Value))
        except ValueError:
            print("object {ob} not found".format(ob=current_element))

    def triggerEditDatapointLoad(self):
        def fillPropertyFormData():
            self.ui.cb_Edit_Property.clear()
            for prop in Datapoint._fields:
                self.ui.cb_Edit_Property.addItem(prop)

        self.ui.cb_Edit_Property.currentIndexChanged.disconnect()
        self.ui.cb_Edit_Dataset.currentIndexChanged.disconnect()

        self.ui.cb_Edit_Dataset.clear()
        fillPropertyFormData()
        for element in self.Pyrtemonnaie:
            self.ui.cb_Edit_Dataset.addItem(str(element))

        self.ui.cb_Edit_Property.currentIndexChanged.connect(self.triggerEditDatapointChanged)
        self.ui.cb_Edit_Dataset.currentIndexChanged.connect(self.triggerEditDatapointChanged)
        self.triggerEditDatapointChanged()     

    def triggerTabViewChange(self):
        active_element = self.ui.tabWidget.indexOf(self.ui.tabWidget.currentWidget())
        if active_element == 0:
            self.triggerNewDatapointReset()
        elif active_element == 1:
            self.triggerEditDatapointLoad()
        elif active_element == 2:
            print("delete")

    def triggerEditDatapointSave(self):
        try:
            datapoint = self.strToDatapoint(self.ui.cb_Edit_Dataset.currentText())
            datapoint_idx = self.Pyrtemonnaie.index(datapoint)
            prop = self.ui.cb_Edit_Property.currentText()

            if prop == "Recipient" or prop == "Comment":
                datapoint = datapoint._replace(**{prop: self.ui.le_Edit_Property_New.text()})
            elif prop == "Value":
                datapoint = datapoint._replace(**{prop: float(self.ui.le_Edit_Property_New.text())})
            elif prop == "Date":
                date_string = self.ui.le_Edit_Property_New.text()
                if self.date_matches_regex(date_string):
                    datapoint = datapoint._replace(**{prop: self.parse_line_date(date_string)})
                else:
                    raise ValueError

            self.Pyrtemonnaie[datapoint_idx] = datapoint

            self.ui.le_Edit_Property_New.setText("")

            self.load_data_to_tv()
            self.triggerEditDatapointLoad()
        except ValueError:
            QMessageBox.critical(self, "Pyrtemonnaie", "Invalid input \"{value}\" for property \"{prop}\"!".format(value=self.ui.le_Edit_Property_New.text(), prop=prop), QMessageBox.Ok)
        except Exception as e:
            print(e)

    def triggerDeleteDatapointOk(self):
        pass

    def triggerShowPyrtemonnaie(self):
        pass

    def triggerFillDetailView(self):
        pass
    
    def triggerExit(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    ex = Pyrtemonnaie()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()