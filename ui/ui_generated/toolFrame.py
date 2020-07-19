# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Code\Python\Ball-Simulator\ui\toolFrame.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from .parametersFrame import Ui_Parameters

class Ui_Tools(object):
    def setupUi(self, Tools):
        Tools.setObjectName("Tools")
        Tools.resize(472, 647)
        Tools.setMinimumSize(QtCore.QSize(472, 647))
        Tools.setMaximumSize(QtCore.QSize(472, 1000))
        self.gridLayout = QtWidgets.QGridLayout(Tools)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Tools)
        self.tabWidget.setObjectName("tabWidget")

        self.parameters = QtWidgets.QWidget()
        self.parameters.setObjectName("tools")
        self.uiParameters = Ui_Parameters()
        self.uiParameters.setupUi(self.parameters)
        self.tabWidget.addTab(self.parameters, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Tools)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Tools)

    def retranslateUi(self, Tools):
        _translate = QtCore.QCoreApplication.translate
        Tools.setWindowTitle(_translate("Tools", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parameters), _translate("Tools", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Tools", "Tab 2"))
