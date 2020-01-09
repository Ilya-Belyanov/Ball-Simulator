'''
                The Reflection algorithm on the example of Balls.
1) Coordinate system: Axis OX directed from left to right, axis OY directed from buttom to top.
Y
^
.
.
.
.
.-------------->X
2) The Ball has start coordinate of centre (x,y), start direction angle in degrees (f), X-axis radius (R1),
Y-axis radius (R2) and speed in pi/10ms(speed).
3) Speed splits into speed along the X-axis (newX) and along Y-axis (newY). So newX^2 + newY^2 = speed^2
4) Surface angle counts down counterclockwise
                         /-f---                -- a\
                    ---/---- f - is possitive  -----\---  a - is negative

5) The Reflection algorithm is in ballWindow.py (changeDirection(a,ball)), where a -angle of reflection and
ball - reflecting ball. Algorithm based on projection on sufface of reflection, changing of vertical speed and
return back to main X-Y basis.

'''

from PyQt5 import  QtCore, QtGui, QtWidgets
from ballWindow import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        '''Create main Window'''
        super(MyWindow,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.timerMove = QtCore.QBasicTimer()
        self.timerMove.start(10, self)
        
        self.setChildrenFocusPolicy(QtCore.Qt.NoFocus)
        self.ui.frame.setGeometry(QtCore.QRect(25, 25, 850, 850))
        self.ui.frameRight.setGeometry(QtCore.QRect(875, 25, 600, 400))

        self.ui.sld.valueChanged.connect(self.setStartSpeed)
        self.ui.sld_grav.valueChanged.connect(self.setGravity)
        self.ui.sld_loss.valueChanged.connect(self.setLoss)
        self.ui.bt_angle.clicked.connect(self.angleDialog)

        self.setTextParameters()
        self.setStyleProgramm()
    
    def setStyleProgramm(self):
        self.ui.frame.setStyleSheet('background-color: rgb(50,50,50)')
        self.ui.lb_red.setStyleSheet('color: rgb(170,0,0)')
        self.ui.lb_green.setStyleSheet('color: rgb(0,170,0)')
        self.ui.lb_blue.setStyleSheet('color: rgb(0,0,170)')
        self.ui.lb_dark.setStyleSheet('color: rgb(0,0,0)')
        self.ui.lb_border1.setFont(QtGui.QFont('Lucida Bright', 10))
        self.ui.lb_border1.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.ui.lb_border2.setFont(QtGui.QFont('Lucida Bright', 10))
        self.ui.lb_border2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.ui.frameRight.setStyleSheet('background-color: rgb(200,200,200)')
        
    def setStartSpeed(self,speed):
        self.ui.frame.startSpeed = speed / 2
        self.setTextParameters()

    def setLoss(self,loss):
        '''Set share of losse during scattering'''
        self.ui.frame.loss = loss / 100
        self.ui.frame.loss = float('{:.2f}'.format(self.ui.frame.loss))
        self.setTextParameters()

    def setGravity(self,gravity):
        self.ui.frame.gravity = gravity / 500
        self.setTextParameters()
    
    def angleDialog(self):
        f,ok=QtWidgets.QInputDialog.getText(self,
                                    'Choise angle',"Enter start degrees from 0 (to rigth) to 360")

        if ok:
            try:
                self.ui.frame.startF = int(f)
            except ValueError:
                self.ui.frame.startF = 0
        self.setTextParameters()
            
    def setTextParameters(self):
        self.ui.lb_speed.setText('Start speed = ' + str(self.ui.frame.startSpeed) + ' pi/10ms')
        self.ui.lb_grav.setText('Gravity = ' + str(self.ui.frame.gravity) + ' pi/10ms')
        self.ui.lb_angle.setText('Start angle = ' + str(self.ui.frame.startF) + ' degrees')
        self.ui.lb_loss.setText('Loss of energy = ' + str(int(self.ui.frame.loss * 100)) + ' %')

    def setTextSpeed(self):
        self.ui.lb_red.setText('SpeedRed = ' + str(self.ui.frame.listBall[0].speedBall()) + ' pi/10ms')
        self.ui.lb_green.setText('SpeedGreen = ' + str(self.ui.frame.listBall[1].speedBall()) + ' pi/10ms')
        self.ui.lb_blue.setText('SpeedBlue = ' + str(self.ui.frame.listBall[2].speedBall()) + ' pi/10ms')
        self.ui.lb_dark.setText('SpeedDark = ' + str(self.ui.frame.listBall[3].speedBall()) + ' pi/10ms')

    def timerEvent(self, event):
        if event.timerId() == self.timerMove.timerId():
            self.ui.frame.moveBall()
            if self.ui.frame.existBall:
                self.setTextSpeed()
            self.update()

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Space:
            self.ui.frame.createBall()
            self.update()


    def setChildrenFocusPolicy(self, policy):
        '''Focus on the main Window'''
        def recursiveSetChildFocusPolicy(parentQWidget):
            for childQWidget in parentQWidget.findChildren(QtWidgets.QWidget):
                childQWidget.setFocusPolicy(policy)
                recursiveSetChildFocusPolicy(childQWidget)

        recursiveSetChildFocusPolicy(self)


if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    application=MyWindow()
    application.show()
    sys.exit(app.exec())