from PyQt5 import  QtCore, QtGui, QtWidgets
from ballWindow import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        '''Create main Window'''
        super(MyWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timerMove = QtCore.QBasicTimer()
        self.timerMove.start(10, self)

        self.timerInfo = QtCore.QBasicTimer()
        self.timerInfo.start(100, self)
        
        self.setChildrenFocusPolicy(QtCore.Qt.NoFocus)
        self.ui.frame.setGeometry(QtCore.QRect(25, 25, 750, 750))
        self.ui.frame.createBoard()
        self.ui.frameRight.setGeometry(QtCore.QRect(775, 25, 600, 750))

        self.ui.sld.valueChanged.connect(self.setStartSpeed)
        self.ui.sld_grav.valueChanged.connect(self.setGravity)
        self.ui.sld_loss.valueChanged.connect(self.setLoss)
        self.ui.btAngle.clicked.connect(self.angleDialog)

        self.setTextParameters()
        self.loadStyleSheets()

    def loadStyleSheets(self):
        style = "static/style.css"
        with open(style, "r") as f:
            self.setStyleSheet(f.read())
        
    def setStartSpeed(self,speed):
        self.ui.frame.board.startSpeed = speed / 3
        self.ui.frame.board.startSpeed = float('{:.5f}'.format(self.ui.frame.board.startSpeed))
        self.setTextParameters()

    def setLoss(self,loss):
        '''Set share of losse during scattering'''
        self.ui.frame.board.loss = loss / 100
        self.ui.frame.board.loss = float('{:.2f}'.format(self.ui.frame.board.loss))
        self.setTextParameters()

    def setGravity(self,gravity):
        self.ui.frame.board.gravity = gravity / 100
        self.setTextParameters()
    
    def angleDialog(self):
        f,ok = QtWidgets.QInputDialog.getText(self,
                                    'Choise angle',"Enter start degrees from 0 (to rigth) to 360")
        if ok:
            try:
                self.ui.frame.board.startF = float(f)
            except ValueError:
                pass
        self.setTextParameters()
            
    def setTextParameters(self):
        self.ui.lb_speed.setText('Start speed = ' + str(int(self.ui.frame.board.startSpeed*100)) + ' pxl/sec')
        self.ui.lb_grav.setText('Gravity = ' + str(int(self.ui.frame.board.gravity*100)) + ' pxl/sec')
        self.ui.lb_angle.setText('Start angle = ' + str(self.ui.frame.board.startF) + ' degrees')
        self.ui.lb_loss.setText('Loss of energy = ' + str(int(self.ui.frame.board.loss * 100)) + ' %')

    def setTextSpeed(self):
        self.ui.lb_red.setText('SpeedRed = ' + str(int(self.ui.frame.board.listBall[0].speedBall()*100)) + ' pxl/sec')
        self.ui.lb_green.setText('SpeedGreen = ' + str(int(self.ui.frame.board.listBall[1].speedBall()*100)) + ' pxl/sec')
        self.ui.lb_yellow.setText('SpeedYellow = ' + str(int(self.ui.frame.board.listBall[2].speedBall()*100)) + ' pxl/sec')
        self.ui.lb_purple.setText('SpeedPink = ' + str(int(self.ui.frame.board.listBall[3].speedBall()*100)) + ' pxl/sec')

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
        '''Focus on the main Window'''
        def recursiveSetChildFocusPolicy(parentQWidget):
            for childQWidget in parentQWidget.findChildren(QtWidgets.QWidget):
                childQWidget.setFocusPolicy(policy)
                recursiveSetChildFocusPolicy(childQWidget)

        recursiveSetChildFocusPolicy(self)
