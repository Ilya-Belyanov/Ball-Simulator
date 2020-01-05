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

from PyQt5 import  QtCore,QtWidgets
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
        self.ui.frame.setGeometry(QtCore.QRect(100, 25, 850, 850))

    def timerEvent(self, event):
        if event.timerId() == self.timerMove.timerId():
            self.ui.frame.moveBall()
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

app=QtWidgets.QApplication([])
application=MyWindow()
application.show()
sys.exit(app.exec())