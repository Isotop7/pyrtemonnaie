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
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tv_dataset = QtWidgets.QTableView(self.centralwidget)
        self.tv_dataset.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tv_dataset.setAlternatingRowColors(True)
        self.tv_dataset.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tv_dataset.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tv_dataset.setGridStyle(QtCore.Qt.DotLine)
        self.tv_dataset.setSortingEnabled(False)
        self.tv_dataset.setObjectName("tv_dataset")
        self.horizontalLayout.addWidget(self.tv_dataset)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbl_DataSet_Recipient = QtWidgets.QLabel(self.groupBox)
        self.lbl_DataSet_Recipient.setMinimumSize(QtCore.QSize(79, 0))
        self.lbl_DataSet_Recipient.setObjectName("lbl_DataSet_Recipient")
        self.horizontalLayout_8.addWidget(self.lbl_DataSet_Recipient)
        self.le_DataSet_Recipient = QtWidgets.QLineEdit(self.groupBox)
        self.le_DataSet_Recipient.setMinimumSize(QtCore.QSize(0, 0))
        self.le_DataSet_Recipient.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_DataSet_Recipient.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_DataSet_Recipient.setReadOnly(True)
        self.le_DataSet_Recipient.setObjectName("le_DataSet_Recipient")
        self.horizontalLayout_8.addWidget(self.le_DataSet_Recipient)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbl_DataSet_Date = QtWidgets.QLabel(self.groupBox)
        self.lbl_DataSet_Date.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_DataSet_Date.setObjectName("lbl_DataSet_Date")
        self.horizontalLayout_9.addWidget(self.lbl_DataSet_Date)
        self.le_DataSet_Date = QtWidgets.QLineEdit(self.groupBox)
        self.le_DataSet_Date.setReadOnly(True)
        self.le_DataSet_Date.setObjectName("le_DataSet_Date")
        self.horizontalLayout_9.addWidget(self.le_DataSet_Date)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbl_DataSet_Value = QtWidgets.QLabel(self.groupBox)
        self.lbl_DataSet_Value.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_DataSet_Value.setObjectName("lbl_DataSet_Value")
        self.horizontalLayout_10.addWidget(self.lbl_DataSet_Value)
        self.le_DataSet_Value = QtWidgets.QLineEdit(self.groupBox)
        self.le_DataSet_Value.setReadOnly(True)
        self.le_DataSet_Value.setObjectName("le_DataSet_Value")
        self.horizontalLayout_10.addWidget(self.le_DataSet_Value)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbl_DataSet_Comment = QtWidgets.QLabel(self.groupBox)
        self.lbl_DataSet_Comment.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_DataSet_Comment.setObjectName("lbl_DataSet_Comment")
        self.horizontalLayout_11.addWidget(self.lbl_DataSet_Comment)
        self.le_DataSet_Comment = QtWidgets.QLineEdit(self.groupBox)
        self.le_DataSet_Comment.setReadOnly(True)
        self.le_DataSet_Comment.setObjectName("le_DataSet_Comment")
        self.horizontalLayout_11.addWidget(self.le_DataSet_Comment)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(False)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabNew = QtWidgets.QWidget()
        self.tabNew.setObjectName("tabNew")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabNew)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.bbox_New = QtWidgets.QDialogButtonBox(self.tabNew)
        self.bbox_New.setStandardButtons(QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.Save)
        self.bbox_New.setCenterButtons(False)
        self.bbox_New.setObjectName("bbox_New")
        self.horizontalLayout_7.addWidget(self.bbox_New)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 7, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_New_Value = QtWidgets.QLabel(self.tabNew)
        self.label_New_Value.setMinimumSize(QtCore.QSize(80, 0))
        self.label_New_Value.setObjectName("label_New_Value")
        self.horizontalLayout_5.addWidget(self.label_New_Value)
        self.le_New_Value = QtWidgets.QLineEdit(self.tabNew)
        self.le_New_Value.setCursorPosition(0)
        self.le_New_Value.setObjectName("le_New_Value")
        self.horizontalLayout_5.addWidget(self.le_New_Value)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_New_Comment = QtWidgets.QLabel(self.tabNew)
        self.label_New_Comment.setMinimumSize(QtCore.QSize(80, 0))
        self.label_New_Comment.setObjectName("label_New_Comment")
        self.horizontalLayout_6.addWidget(self.label_New_Comment)
        self.le_New_Comment = QtWidgets.QLineEdit(self.tabNew)
        self.le_New_Comment.setCursorPosition(0)
        self.le_New_Comment.setObjectName("le_New_Comment")
        self.horizontalLayout_6.addWidget(self.le_New_Comment)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_New_Date = QtWidgets.QLabel(self.tabNew)
        self.label_New_Date.setMinimumSize(QtCore.QSize(80, 0))
        self.label_New_Date.setObjectName("label_New_Date")
        self.horizontalLayout_4.addWidget(self.label_New_Date)
        self.le_New_Date = QtWidgets.QLineEdit(self.tabNew)
        self.le_New_Date.setCursorPosition(0)
        self.le_New_Date.setObjectName("le_New_Date")
        self.horizontalLayout_4.addWidget(self.le_New_Date)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_New_Recipient = QtWidgets.QLabel(self.tabNew)
        self.lbl_New_Recipient.setMinimumSize(QtCore.QSize(79, 0))
        self.lbl_New_Recipient.setObjectName("lbl_New_Recipient")
        self.horizontalLayout_3.addWidget(self.lbl_New_Recipient)
        self.le_New_Recipient = QtWidgets.QLineEdit(self.tabNew)
        self.le_New_Recipient.setFrame(True)
        self.le_New_Recipient.setCursorPosition(0)
        self.le_New_Recipient.setPlaceholderText("")
        self.le_New_Recipient.setClearButtonEnabled(False)
        self.le_New_Recipient.setObjectName("le_New_Recipient")
        self.horizontalLayout_3.addWidget(self.le_New_Recipient)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabNew, "")
        self.tabEdit = QtWidgets.QWidget()
        self.tabEdit.setObjectName("tabEdit")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabEdit)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lbl_Edit_DataSet = QtWidgets.QLabel(self.tabEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Edit_DataSet.sizePolicy().hasHeightForWidth())
        self.lbl_Edit_DataSet.setSizePolicy(sizePolicy)
        self.lbl_Edit_DataSet.setObjectName("lbl_Edit_DataSet")
        self.horizontalLayout_12.addWidget(self.lbl_Edit_DataSet)
        self.cb_Edit_Dataset = QtWidgets.QComboBox(self.tabEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_Edit_Dataset.sizePolicy().hasHeightForWidth())
        self.cb_Edit_Dataset.setSizePolicy(sizePolicy)
        self.cb_Edit_Dataset.setObjectName("cb_Edit_Dataset")
        self.horizontalLayout_12.addWidget(self.cb_Edit_Dataset)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lbl_Edit_Property = QtWidgets.QLabel(self.tabEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Edit_Property.sizePolicy().hasHeightForWidth())
        self.lbl_Edit_Property.setSizePolicy(sizePolicy)
        self.lbl_Edit_Property.setObjectName("lbl_Edit_Property")
        self.horizontalLayout_13.addWidget(self.lbl_Edit_Property)
        self.cb_Edit_Property = QtWidgets.QComboBox(self.tabEdit)
        self.cb_Edit_Property.setObjectName("cb_Edit_Property")
        self.horizontalLayout_13.addWidget(self.cb_Edit_Property)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lbl_Edit_Property_Old = QtWidgets.QLabel(self.tabEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Edit_Property_Old.sizePolicy().hasHeightForWidth())
        self.lbl_Edit_Property_Old.setSizePolicy(sizePolicy)
        self.lbl_Edit_Property_Old.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_Edit_Property_Old.setObjectName("lbl_Edit_Property_Old")
        self.horizontalLayout_15.addWidget(self.lbl_Edit_Property_Old)
        self.le_Edit_Property_Old = QtWidgets.QLineEdit(self.tabEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Edit_Property_Old.sizePolicy().hasHeightForWidth())
        self.le_Edit_Property_Old.setSizePolicy(sizePolicy)
        self.le_Edit_Property_Old.setReadOnly(True)
        self.le_Edit_Property_Old.setObjectName("le_Edit_Property_Old")
        self.horizontalLayout_15.addWidget(self.le_Edit_Property_Old)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lbl_Edit_Property_New = QtWidgets.QLabel(self.tabEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Edit_Property_New.sizePolicy().hasHeightForWidth())
        self.lbl_Edit_Property_New.setSizePolicy(sizePolicy)
        self.lbl_Edit_Property_New.setObjectName("lbl_Edit_Property_New")
        self.horizontalLayout_16.addWidget(self.lbl_Edit_Property_New)
        self.le_Edit_Property_New = QtWidgets.QLineEdit(self.tabEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Edit_Property_New.sizePolicy().hasHeightForWidth())
        self.le_Edit_Property_New.setSizePolicy(sizePolicy)
        self.le_Edit_Property_New.setObjectName("le_Edit_Property_New")
        self.horizontalLayout_16.addWidget(self.le_Edit_Property_New)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.bbox_Edit = QtWidgets.QDialogButtonBox(self.tabEdit)
        self.bbox_Edit.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.bbox_Edit.setObjectName("bbox_Edit")
        self.verticalLayout_7.addWidget(self.bbox_Edit)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tabEdit, "")
        self.tabDelete = QtWidgets.QWidget()
        self.tabDelete.setObjectName("tabDelete")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tabDelete)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lbl_Delete_DataSet = QtWidgets.QLabel(self.tabDelete)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Delete_DataSet.sizePolicy().hasHeightForWidth())
        self.lbl_Delete_DataSet.setSizePolicy(sizePolicy)
        self.lbl_Delete_DataSet.setObjectName("lbl_Delete_DataSet")
        self.horizontalLayout_17.addWidget(self.lbl_Delete_DataSet)
        self.cb_Delete_Dataset = QtWidgets.QComboBox(self.tabDelete)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_Delete_Dataset.sizePolicy().hasHeightForWidth())
        self.cb_Delete_Dataset.setSizePolicy(sizePolicy)
        self.cb_Delete_Dataset.setObjectName("cb_Delete_Dataset")
        self.horizontalLayout_17.addWidget(self.cb_Delete_Dataset)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.bbox_Delete = QtWidgets.QDialogButtonBox(self.tabDelete)
        self.bbox_Delete.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.bbox_Delete.setCenterButtons(True)
        self.bbox_Delete.setObjectName("bbox_Delete")
        self.verticalLayout_11.addWidget(self.bbox_Delete)
        self.verticalLayout_9.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tabDelete, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSavePyrtemonnaieAs = QtWidgets.QMenu(self.menuFile)
        self.menuSavePyrtemonnaieAs.setObjectName("menuSavePyrtemonnaieAs")
        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setEnabled(False)
        self.menuReports.setObjectName("menuReports")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenPyrtemonnaie = QtWidgets.QAction(MainWindow)
        self.actionOpenPyrtemonnaie.setObjectName("actionOpenPyrtemonnaie")
        self.actionSavePyrtemonnaie = QtWidgets.QAction(MainWindow)
        self.actionSavePyrtemonnaie.setObjectName("actionSavePyrtemonnaie")
        self.actionSaveAsCsv = QtWidgets.QAction(MainWindow)
        self.actionSaveAsCsv.setObjectName("actionSaveAsCsv")
        self.actionSaveAsSqlite = QtWidgets.QAction(MainWindow)
        self.actionSaveAsSqlite.setObjectName("actionSaveAsSqlite")
        self.actionShowConfig = QtWidgets.QAction(MainWindow)
        self.actionShowConfig.setObjectName("actionShowConfig")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAddDatapoint = QtWidgets.QAction(MainWindow)
        self.actionAddDatapoint.setEnabled(True)
        self.actionAddDatapoint.setObjectName("actionAddDatapoint")
        self.actionEditDatapoint = QtWidgets.QAction(MainWindow)
        self.actionEditDatapoint.setObjectName("actionEditDatapoint")
        self.actionDeleteDatapoint = QtWidgets.QAction(MainWindow)
        self.actionDeleteDatapoint.setObjectName("actionDeleteDatapoint")
        self.actionShowPyrtemonnaie = QtWidgets.QAction(MainWindow)
        self.actionShowPyrtemonnaie.setObjectName("actionShowPyrtemonnaie")
        self.menuSavePyrtemonnaieAs.addAction(self.actionSaveAsCsv)
        self.menuSavePyrtemonnaieAs.addAction(self.actionSaveAsSqlite)
        self.menuFile.addAction(self.actionOpenPyrtemonnaie)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSavePyrtemonnaie)
        self.menuFile.addAction(self.menuSavePyrtemonnaieAs.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionShowConfig)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.le_New_Recipient, self.le_New_Date)
        MainWindow.setTabOrder(self.le_New_Date, self.le_New_Value)
        MainWindow.setTabOrder(self.le_New_Value, self.le_New_Comment)
        MainWindow.setTabOrder(self.le_New_Comment, self.tv_dataset)
        MainWindow.setTabOrder(self.tv_dataset, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.le_DataSet_Recipient)
        MainWindow.setTabOrder(self.le_DataSet_Recipient, self.le_DataSet_Date)
        MainWindow.setTabOrder(self.le_DataSet_Date, self.le_DataSet_Value)
        MainWindow.setTabOrder(self.le_DataSet_Value, self.le_DataSet_Comment)
        MainWindow.setTabOrder(self.le_DataSet_Comment, self.cb_Edit_Dataset)
        MainWindow.setTabOrder(self.cb_Edit_Dataset, self.cb_Edit_Property)
        MainWindow.setTabOrder(self.cb_Edit_Property, self.le_Edit_Property_Old)
        MainWindow.setTabOrder(self.le_Edit_Property_Old, self.le_Edit_Property_New)
        MainWindow.setTabOrder(self.le_Edit_Property_New, self.cb_Delete_Dataset)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyrtemonnaie"))
        self.groupBox.setTitle(_translate("MainWindow", "Datensatz"))
        self.lbl_DataSet_Recipient.setText(_translate("MainWindow", "Recipient:"))
        self.lbl_DataSet_Date.setText(_translate("MainWindow", "Date:"))
        self.lbl_DataSet_Value.setText(_translate("MainWindow", "Value:"))
        self.lbl_DataSet_Comment.setText(_translate("MainWindow", "Comment:"))
        self.label_New_Value.setText(_translate("MainWindow", "Value"))
        self.label_New_Comment.setText(_translate("MainWindow", "Comment:"))
        self.label_New_Date.setText(_translate("MainWindow", "Date:"))
        self.lbl_New_Recipient.setText(_translate("MainWindow", "Recipient:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNew), _translate("MainWindow", "New"))
        self.lbl_Edit_DataSet.setText(_translate("MainWindow", "Dataset"))
        self.lbl_Edit_Property.setText(_translate("MainWindow", "Property"))
        self.lbl_Edit_Property_Old.setText(_translate("MainWindow", "Old value:"))
        self.lbl_Edit_Property_New.setText(_translate("MainWindow", "New value:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEdit), _translate("MainWindow", "Edit"))
        self.lbl_Delete_DataSet.setText(_translate("MainWindow", "Dataset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDelete), _translate("MainWindow", "Delete"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuSavePyrtemonnaieAs.setTitle(_translate("MainWindow", "Save &Pyrtemonnaie as"))
        self.menuReports.setTitle(_translate("MainWindow", "Beri&chte"))
        self.actionOpenPyrtemonnaie.setText(_translate("MainWindow", "&Open Pyrtemonnaie"))
        self.actionOpenPyrtemonnaie.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSavePyrtemonnaie.setText(_translate("MainWindow", "&Save Pyrtemonnaie"))
        self.actionSavePyrtemonnaie.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAsCsv.setText(_translate("MainWindow", "&csv"))
        self.actionSaveAsSqlite.setText(_translate("MainWindow", "&sqlite"))
        self.actionShowConfig.setText(_translate("MainWindow", "Show &configuration"))
        self.actionShowConfig.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.actionExit.setText(_translate("MainWindow", "&Quit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAddDatapoint.setText(_translate("MainWindow", "Datenpunkt hinzufügen"))
        self.actionEditDatapoint.setText(_translate("MainWindow", "Datenpunkt bearbeiten"))
        self.actionDeleteDatapoint.setText(_translate("MainWindow", "Datenpunkt löschen"))
        self.actionShowPyrtemonnaie.setText(_translate("MainWindow", "Pyrtemonnaie anzeigen"))

