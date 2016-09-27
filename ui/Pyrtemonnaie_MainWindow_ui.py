# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tv_dataset = QtWidgets.QTableView(self.centralwidget)
        self.tv_dataset.setGridStyle(QtCore.Qt.DotLine)
        self.tv_dataset.setSortingEnabled(True)
        self.tv_dataset.setObjectName("tv_dataset")
        self.horizontalLayout.addWidget(self.tv_dataset)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuPyrtemonnaie_speichern_als = QtWidgets.QMenu(self.menuDatei)
        self.menuPyrtemonnaie_speichern_als.setObjectName("menuPyrtemonnaie_speichern_als")
        self.menuPyrtemonnaie = QtWidgets.QMenu(self.menubar)
        self.menuPyrtemonnaie.setObjectName("menuPyrtemonnaie")
        self.menuBerichte = QtWidgets.QMenu(self.menubar)
        self.menuBerichte.setEnabled(False)
        self.menuBerichte.setObjectName("menuBerichte")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPyrtemonnaie_ffnen = QtWidgets.QAction(MainWindow)
        self.actionPyrtemonnaie_ffnen.setObjectName("actionPyrtemonnaie_ffnen")
        self.actionPyrtemonnaie_speichern = QtWidgets.QAction(MainWindow)
        self.actionPyrtemonnaie_speichern.setObjectName("actionPyrtemonnaie_speichern")
        self.actionCsv = QtWidgets.QAction(MainWindow)
        self.actionCsv.setObjectName("actionCsv")
        self.actionSqlite = QtWidgets.QAction(MainWindow)
        self.actionSqlite.setObjectName("actionSqlite")
        self.actionKonfiguration_anzeigen = QtWidgets.QAction(MainWindow)
        self.actionKonfiguration_anzeigen.setObjectName("actionKonfiguration_anzeigen")
        self.actionBeenden = QtWidgets.QAction(MainWindow)
        self.actionBeenden.setObjectName("actionBeenden")
        self.actionDatenpunkt_hinzuf_gen = QtWidgets.QAction(MainWindow)
        self.actionDatenpunkt_hinzuf_gen.setObjectName("actionDatenpunkt_hinzuf_gen")
        self.actionDatenpunkt_bearbeiten = QtWidgets.QAction(MainWindow)
        self.actionDatenpunkt_bearbeiten.setObjectName("actionDatenpunkt_bearbeiten")
        self.actionDatenpunkt_l_schen = QtWidgets.QAction(MainWindow)
        self.actionDatenpunkt_l_schen.setObjectName("actionDatenpunkt_l_schen")
        self.actionPyrtemonnaie_anzeigen = QtWidgets.QAction(MainWindow)
        self.actionPyrtemonnaie_anzeigen.setObjectName("actionPyrtemonnaie_anzeigen")
        self.menuPyrtemonnaie_speichern_als.addAction(self.actionCsv)
        self.menuPyrtemonnaie_speichern_als.addAction(self.actionSqlite)
        self.menuDatei.addAction(self.actionPyrtemonnaie_ffnen)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionPyrtemonnaie_speichern)
        self.menuDatei.addAction(self.menuPyrtemonnaie_speichern_als.menuAction())
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionKonfiguration_anzeigen)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionBeenden)
        self.menuPyrtemonnaie.addAction(self.actionDatenpunkt_hinzuf_gen)
        self.menuPyrtemonnaie.addAction(self.actionDatenpunkt_bearbeiten)
        self.menuPyrtemonnaie.addAction(self.actionDatenpunkt_l_schen)
        self.menuPyrtemonnaie.addSeparator()
        self.menuPyrtemonnaie.addAction(self.actionPyrtemonnaie_anzeigen)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuPyrtemonnaie.menuAction())
        self.menubar.addAction(self.menuBerichte.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyrtemonnaie"))
        self.groupBox.setTitle(_translate("MainWindow", "Datensatz"))
        self.menuDatei.setTitle(_translate("MainWindow", "Da&tei"))
        self.menuPyrtemonnaie_speichern_als.setTitle(_translate("MainWindow", "Pyrtemonnaie speichern als"))
        self.menuPyrtemonnaie.setTitle(_translate("MainWindow", "&Pyrtemonnaie"))
        self.menuBerichte.setTitle(_translate("MainWindow", "Beri&chte"))
        self.actionPyrtemonnaie_ffnen.setText(_translate("MainWindow", "Pyrtemonnaie öffnen"))
        self.actionPyrtemonnaie_speichern.setText(_translate("MainWindow", "Pyrtemonnaie speichern"))
        self.actionCsv.setText(_translate("MainWindow", "csv"))
        self.actionSqlite.setText(_translate("MainWindow", "sqlite"))
        self.actionKonfiguration_anzeigen.setText(_translate("MainWindow", "Konfiguration anzeigen"))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden"))
        self.actionDatenpunkt_hinzuf_gen.setText(_translate("MainWindow", "Datenpunkt hinzufügen"))
        self.actionDatenpunkt_bearbeiten.setText(_translate("MainWindow", "Datenpunkt bearbeiten"))
        self.actionDatenpunkt_l_schen.setText(_translate("MainWindow", "Datenpunkt löschen"))
        self.actionPyrtemonnaie_anzeigen.setText(_translate("MainWindow", "Pyrtemonnaie anzeigen"))

