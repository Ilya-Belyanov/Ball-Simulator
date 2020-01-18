from PyQt5 import QtCore, QtWidgets
from ballLogic import PaintBall

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        '''Create central Window'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = PaintBall(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.frameRight = QtWidgets.QFrame(self.centralwidget)

        self.lb_border = QtWidgets.QLabel('Current speed of balls')
        self.lb_border.setObjectName("lb_border")
        self.sld = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sld_grav = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sld_loss = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.lb_red = QtWidgets.QLabel()
        self.lb_red.setObjectName("lb_red")
        self.lb_green = QtWidgets.QLabel()
        self.lb_green.setObjectName("lb_green")
        self.lb_yellow = QtWidgets.QLabel()
        self.lb_yellow.setObjectName("lb_yellow")
        self.lb_purple = QtWidgets.QLabel()
        self.lb_purple.setObjectName("lb_purple")
        self.lb_border1 = QtWidgets.QLabel('Start parameters of balls')
        self.lb_border1.setObjectName("lb_border")
        self.lb_speed = QtWidgets.QLabel()
        self.lb_angle = QtWidgets.QLabel()
        self.lb_border2 = QtWidgets.QLabel('Current parameters of environment')
        self.lb_border2.setObjectName("lb_border")
        self.lb_grav = QtWidgets.QLabel()
        self.lb_loss = QtWidgets.QLabel()
        self.lb_reload = QtWidgets.QLabel('Press "Space" for reload!')
        self.lb_reload.setObjectName("lb_border")


        self.btAngle = QtWidgets.QPushButton('Choice angle')
        self.btAngle.setObjectName("btAngle")
        
        
        self.hbox_up = QtWidgets.QHBoxLayout()
        self.hbox_down = QtWidgets.QHBoxLayout()
        self.hbox_speed = QtWidgets.QHBoxLayout()
        self.hbox_grav = QtWidgets.QHBoxLayout()
        self.hbox_loss = QtWidgets.QHBoxLayout()
        self.hbox_angle = QtWidgets.QHBoxLayout()
        
        self.hbox_up.addWidget(self.lb_red)
        self.hbox_up.addWidget(self.lb_green)
        self.hbox_down.addWidget(self.lb_yellow)
        self.hbox_down.addWidget(self.lb_purple)
        self.hbox_speed.addWidget(self.sld)
        self.hbox_speed.addWidget(self.lb_speed)
        self.hbox_angle.addWidget(self.btAngle)
        self.hbox_angle.addWidget(self.lb_angle)
        self.hbox_grav.addWidget(self.sld_grav)
        self.hbox_grav.addWidget(self.lb_grav)
        self.hbox_loss.addWidget(self.sld_loss)
        self.hbox_loss.addWidget(self.lb_loss)

        self.vbox = QtWidgets.QVBoxLayout(self.frameRight)
        self.vbox.setSpacing(5)
        self.vbox.addWidget(self.lb_border)
        self.vbox.addLayout(self.hbox_up)
        self.vbox.addLayout(self.hbox_down)
        self.vbox.addWidget(self.lb_border1)
        self.vbox.addLayout(self.hbox_speed)
        self.vbox.addLayout(self.hbox_angle)
        self.vbox.addWidget(self.lb_border2)
        self.vbox.addLayout(self.hbox_grav)
        self.vbox.addLayout(self.hbox_loss)
        self.vbox.addWidget(self.lb_reload)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)


        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.loadStyleSheets()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ball Simulation"))

    def loadStyleSheets(self):
        style = "static/style.css"
        with open(style, "r") as f:
            self.frameRight.setStyleSheet(f.read())

if __name__ == "__main__":
    print('Module for Ball Simutator')