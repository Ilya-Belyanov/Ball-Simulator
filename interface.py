from PyQt5 import QtCore, QtWidgets

from ui.ui_generated.mainWidow import Ui_MainWindow
from ui.ui_generated.parametersFrame import Ui_Parameters
from ui.ui_generated.toolFrame import Ui_Tools
from painter import PaintBoard
from adapter import Adapter


class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timerMove = QtCore.QBasicTimer()
        self.timerMove.start(10, self)

        self.timerInfo = QtCore.QBasicTimer()
        self.timerInfo.start(100, self)

        self.setChildrenFocusPolicy(QtCore.Qt.NoFocus)

        self.connectMainFrame()
        self.adapter = Adapter(self.ui.paintBall)

        self.panelParameters = self.ui.uiTools.uiParameters
        self.panelParameters.slSpeed.valueChanged.connect(self.setStartSpeed)
        self.panelParameters.slSpeed.setRange(0, 20)
        self.panelParameters.slGravity.valueChanged.connect(self.setGravity)
        self.panelParameters.slLoss.valueChanged.connect(self.setLoss)
        self.panelParameters.btAngle.clicked.connect(self.angleDialog)

        self.setTextParameters()
        self.loadStyleSheets()

    def connectMainFrame(self):
        self.ui.paintBall = PaintBoard(self.ui.centralwidget)
        self.ui.paintBall.setMinimumSize(QtCore.QSize(800, 800))
        self.ui.paintBall.setMaximumSize(QtCore.QSize(800, 800))
        self.ui.paintBall.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ui.paintBall.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ui.paintBall.setObjectName("paintBall")
        self.ui.horizontalLayout.replaceWidget(self.ui.frame, self.ui.paintBall)
        self.ui.frame.setVisible(False)

        self.ui.tools = QtWidgets.QWidget()
        self.ui.tools.setObjectName("tools")
        self.ui.uiTools = Ui_Tools()
        self.ui.uiTools.setupUi(self.ui.tools)
        self.ui.horizontalLayout.addWidget(self.ui.tools)

        self.connectToolFrame()

    def connectToolFrame(self):
        self.ui.uiTools.tabWidget.clear()
        self.ui.uiTools.parameters = QtWidgets.QWidget()
        self.ui.uiTools.parameters.setObjectName("tools")
        self.ui.uiTools.uiParameters = Ui_Parameters()
        self.ui.uiTools.uiParameters.setupUi(self.ui.uiTools.parameters)
        self.ui.uiTools.tabWidget.insertTab(0, self.ui.uiTools.parameters, "Tools")

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
        self.panelParameters.lbSpeed.setText('Start speed = ' + self.adapter.boardStartSpeedStr() + ' pxl/sec')
        self.panelParameters.lbGravity.setText('Gravity = ' + self.adapter.boardGravityStr() + ' pxl/sec')
        self.panelParameters.lbAngle.setText('Start angle = ' + self.adapter.boardStartAngleStr() + ' degrees')
        self.panelParameters.lbLoss.setText('Loss of energy = ' + self.adapter.boardLoseStrProc() + ' %')

    def timerEvent(self, event):
        if event.timerId() == self.timerMove.timerId():
            self.adapter.board.moveBall()
            self.update()

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Space:
            self.adapter.board.createBall()
            self.update()

    def setChildrenFocusPolicy(self, policy):
        def recursiveSetChildFocusPolicy(parentQWidget):
            for childQWidget in parentQWidget.findChildren(QtWidgets.QWidget):
                childQWidget.setFocusPolicy(policy)
                recursiveSetChildFocusPolicy(childQWidget)

        recursiveSetChildFocusPolicy(self)
