from PyQt5 import QtCore, QtWidgets

from mainWindow import Ui_MainWindow
from adapter import Adapter


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timerMove = QtCore.QBasicTimer()
        self.timerMove.start(10, self)

        self.timerInfo = QtCore.QBasicTimer()
        self.timerInfo.start(100, self)

        self.setChildrenFocusPolicy(QtCore.Qt.NoFocus)

        self.ui.frame.setGeometry(QtCore.QRect(25, 25, 750, 750))
        self.adapter = Adapter(self.ui.frame)

        self.ui.frameRight.setGeometry(QtCore.QRect(775, 25, 600, 750))

        self.ui.sld.valueChanged.connect(self.setStartSpeed)
        self.ui.sld.setRange(0, 20)
        self.ui.sld_grav.valueChanged.connect(self.setGravity)
        self.ui.sld_loss.valueChanged.connect(self.setLoss)
        self.ui.btAngle.clicked.connect(self.angleDialog)

        self.setTextParameters()
        self.loadStyleSheets()

    def loadStyleSheets(self):
        style = "static/style.css"
        with open(style, "r") as f:
            self.setStyleSheet(f.read())

    def setStartSpeed(self, speed):
        self.adapter.setStartSpeed(speed)
        self.setTextParameters()

    def setLoss(self, loss):
        self.adapter.setLoss(loss)
        self.setTextParameters()

    def setGravity(self, gravity):
        self.adapter.setGravity(gravity)
        self.setTextParameters()

    def angleDialog(self):
        f, ok = QtWidgets.QInputDialog.getText(self,
                                               'Choice angle', "Enter start degrees from 0 (to right) to 360")
        if ok:
            self.adapter.setStartAngle(f)
        self.setTextParameters()

    def setTextParameters(self):
        self.ui.lb_speed.setText('Start speed = ' + self.adapter.boardStartSpeedStr() + ' pxl/sec')
        self.ui.lb_grav.setText('Gravity = ' + self.adapter.boardGravityStr() + ' pxl/sec')
        self.ui.lb_angle.setText('Start angle = ' + self.adapter.boardStartAngleStr() + ' degrees')
        self.ui.lb_loss.setText('Loss of energy = ' + self.adapter.boardLoseStrProc() + ' %')

    def setTextSpeed(self):
        self.ui.lb_red.setText('SpeedRed = ' + self.adapter.speedBallStr(0) + ' pxl/sec')
        self.ui.lb_green.setText(
            'SpeedGreen = ' + self.adapter.speedBallStr(1) + ' pxl/sec')
        self.ui.lb_yellow.setText(
            'SpeedYellow = ' + self.adapter.speedBallStr(2) + ' pxl/sec')
        self.ui.lb_purple.setText(
            'SpeedPink = ' + self.adapter.speedBallStr(3) + ' pxl/sec')

    def timerEvent(self, event):
        if event.timerId() == self.timerMove.timerId():
            self.ui.frame.board.moveBall()
            self.update()

        if event.timerId() == self.timerInfo.timerId():
            if self.ui.frame.board.existBall:
                self.setTextSpeed()

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Space:
            self.ui.frame.board.createBall()
            self.update()

    def setChildrenFocusPolicy(self, policy):
        def recursiveSetChildFocusPolicy(parentQWidget):
            for childQWidget in parentQWidget.findChildren(QtWidgets.QWidget):
                childQWidget.setFocusPolicy(policy)
                recursiveSetChildFocusPolicy(childQWidget)

        recursiveSetChildFocusPolicy(self)
