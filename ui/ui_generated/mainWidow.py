
from PyQt5 import QtCore, QtWidgets

from painter import PaintBoard
from .toolFrame import Ui_Tools

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.paintBall = PaintBoard(self.centralwidget)
        self.paintBall.setMinimumSize(QtCore.QSize(800, 800))
        self.paintBall.setMaximumSize(QtCore.QSize(800, 800))
        self.paintBall.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.paintBall.setFrameShadow(QtWidgets.QFrame.Raised)
        self.paintBall.setObjectName("paintBall")
        self.horizontalLayout.addWidget(self.paintBall)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.tools = QtWidgets.QWidget()
        self.tools.setObjectName("tools")
        self.uiTools = Ui_Tools()
        self.uiTools.setupUi(self.tools)
        self.horizontalLayout.addWidget(self.tools)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
