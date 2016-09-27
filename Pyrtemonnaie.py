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

        self.ui.actionPyrtemonnaie_ffnen.triggered.connect(self.triggerOpenPyrtemonnaie)
        self.ui.actionPyrtemonnaie_speichern.triggered.connect(self.triggerSavePyrtemonnaie)
        self.ui.actionKonfiguration_anzeigen.triggered.connect(self.triggerShowConfig)
        self.ui.actionDatenpunkt_hinzuf_gen.triggered.connect(self.triggerAddDatapoint)
        self.ui.actionDatenpunkt_bearbeiten.triggered.connect(self.triggerEditDatapoint)
        self.ui.actionDatenpunkt_l_schen.triggered.connect(self.triggerDeleteDatapoint)
        self.ui.actionPyrtemonnaie_anzeigen.triggered.connect(self.triggerShowPyrtemonnaie)
        self.ui.actionBeenden.triggered.connect(self.triggerBeenden)
    

        self.show()

    def triggerOpenPyrtemonnaie(self):
        pass

    def triggerSavePyrtemonnaie(self):
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
    
    def triggerClose(self):
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Pyrtemonnaie()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()