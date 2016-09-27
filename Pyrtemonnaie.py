import re
import sys
from collections import namedtuple
from datetime import date
from operator import attrgetter

from PyQt5 import QtCore, QtGui, QtWidgets

from ui.Pyrtemonnaie_MainWindow_ui import Ui_MainWindow

Datapoint = namedtuple('Datapoint', ['Recipient', 'Date', 'Value', 'Comment'])

class Pyrtemonnaie(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pyrtemonnaie, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

    def triggerOpenPyrtemonnaie(self):
        pass

    def triggerSavePyrtemonnaie(self):
        pass

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
    app = QtWidgets.QApplication(sys.argv)
    ex = Pyrtemonnaie()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()