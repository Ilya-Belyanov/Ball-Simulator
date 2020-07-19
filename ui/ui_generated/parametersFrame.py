# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Code\Python\Ball-Simulator\ui\parametersFrame.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Parameters(object):
    def setupUi(self, Parameters):
        Parameters.setObjectName("Parameters")
        Parameters.resize(472, 647)
        Parameters.setMaximumSize(QtCore.QSize(472, 1000))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Parameters)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbBorderOne = QtWidgets.QLabel(Parameters)
        self.lbBorderOne.setObjectName("lbBorderOne")
        self.verticalLayout_2.addWidget(self.lbBorderOne)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slSpeed = QtWidgets.QSlider(Parameters)
        self.slSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.slSpeed.setObjectName("slSpeed")
        self.horizontalLayout.addWidget(self.slSpeed)
        self.lbSpeed = QtWidgets.QLabel(Parameters)
        self.lbSpeed.setMinimumSize(QtCore.QSize(200, 0))
        self.lbSpeed.setObjectName("lbSpeed")
        self.horizontalLayout.addWidget(self.lbSpeed)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btAngle = QtWidgets.QPushButton(Parameters)
        self.btAngle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btAngle.setObjectName("btAngle")
        self.horizontalLayout_2.addWidget(self.btAngle)
        self.lbAngle = QtWidgets.QLabel(Parameters)
        self.lbAngle.setMinimumSize(QtCore.QSize(200, 0))
        self.lbAngle.setObjectName("lbAngle")
        self.horizontalLayout_2.addWidget(self.lbAngle)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lbBorderTwo = QtWidgets.QLabel(Parameters)
        self.lbBorderTwo.setObjectName("lbBorderTwo")
        self.verticalLayout_2.addWidget(self.lbBorderTwo)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.slGravity = QtWidgets.QSlider(Parameters)
        self.slGravity.setOrientation(QtCore.Qt.Horizontal)
        self.slGravity.setObjectName("slGravity")
        self.horizontalLayout_3.addWidget(self.slGravity)
        self.lbGravity = QtWidgets.QLabel(Parameters)
        self.lbGravity.setMinimumSize(QtCore.QSize(200, 0))
        self.lbGravity.setObjectName("lbGravity")
        self.horizontalLayout_3.addWidget(self.lbGravity)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.slLoss = QtWidgets.QSlider(Parameters)
        self.slLoss.setOrientation(QtCore.Qt.Horizontal)
        self.slLoss.setObjectName("slLoss")
        self.horizontalLayout_4.addWidget(self.slLoss)
        self.lbLoss = QtWidgets.QLabel(Parameters)
        self.lbLoss.setMinimumSize(QtCore.QSize(200, 0))
        self.lbLoss.setObjectName("lbLoss")
        self.horizontalLayout_4.addWidget(self.lbLoss)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.lbBorderReload = QtWidgets.QLabel(Parameters)
        self.lbBorderReload.setObjectName("lbBorderReload")
        self.verticalLayout_2.addWidget(self.lbBorderReload)

        self.retranslateUi(Parameters)
        QtCore.QMetaObject.connectSlotsByName(Parameters)

    def retranslateUi(self, Parameters):
        _translate = QtCore.QCoreApplication.translate
        Parameters.setWindowTitle(_translate("Parameters", "Form"))
        self.lbBorderOne.setText(_translate("Parameters", "Start parameters "))
        self.lbSpeed.setText(_translate("Parameters", "Start speed = 0 pxl/sec "))
        self.btAngle.setText(_translate("Parameters", "Choise angle"))
        self.lbAngle.setText(_translate("Parameters", "Start angle = 0 degrees "))
        self.lbBorderTwo.setText(_translate("Parameters", "Current parameters of environment"))
        self.lbGravity.setText(_translate("Parameters", "Gravity = 0 pxl/sec "))
        self.lbLoss.setText(_translate("Parameters", "Loss of speed = 0 %"))
        self.lbBorderReload.setText(_translate("Parameters", "Press \"Space\" for reload!"))
