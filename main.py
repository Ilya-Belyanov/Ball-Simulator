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
from PyQt5 import QtWidgets
from ballConnect import MyWindow
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
