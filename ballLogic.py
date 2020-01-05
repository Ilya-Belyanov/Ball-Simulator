from PyQt5 import QtCore, QtGui ,QtWidgets
from ballClass import Ball
import random
import math

class PaintBall(QtWidgets.QFrame):
    '''Window of drawing'''
    RAD_45 = 0.785
    RAD_60 = 1.047
    RAD_30 = 0.524
    def __init__(self, parent):
        super().__init__(parent)
        self.existBall = False
        self.countBall = 4

    def createBall(self):
        self.listBall = []
        speed = 5  # pi/10 мс
        #x = random.randint(R1, self.size().width()- R1)
        #y = random.randint(R2, self.size().height() - R2)
        radius = ((10,10),(5,5),(10,10),(30,30))
        coords = ((100,100),(600,100),(600,400),(660,600))
        colors = ((255,0,0,255),(0,255,0,255),(0,0,255,255),(0,0,0,255))
        for i in range(self.countBall):
            R1 = radius[i][0]
            R2 = radius[i][1]
            x = coords[i][0]
            y = coords[i][1]
            color = colors[i]
            f = random.randint(0, 360)
            ball = Ball(x,y,f,R1,R2,speed,color)
            self.listBall.append(ball)

        self.existBall = True

    def moveBall(self):
        if self.existBall:
            for ball in self.listBall:
                ball.coords[1] += ball.newY
                ball.coords[0] += ball.newX

                if ball.coords[1] >= self.size().height() - ball.radius[1] or ball.coords[1] < ball.radius[1]:
                    ball.coords[1] -= ball.newY
                    ball.coords[0] -= ball.newX
                    # Simplification of calculations
                    ball.newY = - ball.newY
                    #a = 0
                    #self.changeDirection(a,ball)

                elif ball.coords[0] < ball.radius[0] or ball.coords[0] >= self.size().width() - ball.radius[0]:
                    ball.coords[1] -= ball.newY
                    ball.coords[0] -= ball.newX
                    # Simplification of calculations
                    ball.newX = - ball.newX
                    #a = 90
                    #self.changeDirection(a,ball)


            # Point of intersection with -60 degrees border up for first ball
            Y1 = - (math.tan(PaintBall.RAD_60)) * (self.listBall[0].coords[0] + self.listBall[0].radius[0] * math.cos(PaintBall.RAD_30)) + \
                self.size().height()

            if  self.listBall[0].coords[1] + self.listBall[0].radius[1] * math.cos(PaintBall.RAD_60) >= Y1 :
                self.listBall[0].coords[1] -= self.listBall[0].newY
                self.listBall[0].coords[0] -= self.listBall[0].newX
                a = -60
                self.changeDirection(a,self.listBall[0])

            # Point of intersection with -60 degrees border down for second ball
            Y2 = - (math.tan(PaintBall.RAD_60)) * (
                        self.listBall[1].coords[0] - self.listBall[1].radius[0] * math.cos(PaintBall.RAD_30)) + \
                 self.size().height()

            if  self.listBall[1].coords[1] - self.listBall[1].radius[1] * math.cos(PaintBall.RAD_60) <= Y2 :
                self.listBall[1].coords[1] -= self.listBall[1].newY
                self.listBall[1].coords[0] -= self.listBall[1].newX
                a = -60
                self.changeDirection(a,self.listBall[1])

            # Point of intersection with -45 degrees border up for second ball
            Y2 = - (math.tan(PaintBall.RAD_45)) * (
                        self.listBall[1].coords[0] + self.listBall[1].radius[0] * math.cos(PaintBall.RAD_45)) + \
                 self.size().height()

            if  self.listBall[1].coords[1] + self.listBall[1].radius[1] * math.cos(PaintBall.RAD_45) >= Y2 :
                self.listBall[1].coords[1] -= self.listBall[1].newY
                self.listBall[1].coords[0] -= self.listBall[1].newX
                a = -45
                self.changeDirection(a,self.listBall[1])

            # Point of intersection with -45 degrees border down for third ball
            Y3 = - (math.tan(PaintBall.RAD_45)) * (
                        self.listBall[2].coords[0] - self.listBall[2].radius[0] * math.cos(PaintBall.RAD_45)) + \
                 self.size().height()

            if self.listBall[2].coords[1] - self.listBall[2].radius[1] * math.cos(PaintBall.RAD_45) <= Y3:
                 self.listBall[2].coords[1] -= self.listBall[2].newY
                 self.listBall[2].coords[0] -= self.listBall[2].newX
                 a = -45
                 self.changeDirection(a, self.listBall[2])

            # Point of intersection with -30 degrees border up for third ball
            Y3 = - (math.tan(PaintBall.RAD_30)) * (
                        self.listBall[2].coords[0] + self.listBall[2].radius[0] * math.cos(PaintBall.RAD_60)) + \
                 self.size().height()

            if self.listBall[2].coords[1] + self.listBall[2].radius[1] * math.cos(PaintBall.RAD_30) >= Y3:
                 self.listBall[2].coords[1] -= self.listBall[2].newY
                 self.listBall[2].coords[0] -= self.listBall[2].newX
                 a = -30
                 self.changeDirection(a, self.listBall[2])

            # Point of intersection with -30 degrees border down for fourth ball
            Y4 = - (math.tan(PaintBall.RAD_30)) * (
                    self.listBall[3].coords[0] - self.listBall[3].radius[0] * math.cos(PaintBall.RAD_60)) + \
                 self.size().height()

            if self.listBall[3].coords[1] - self.listBall[3].radius[1] * math.cos(PaintBall.RAD_30) <= Y4:
                 self.listBall[3].coords[1] -= self.listBall[3].newY
                 self.listBall[3].coords[0] -= self.listBall[3].newX
                 a = -30
                 self.changeDirection(a, self.listBall[3])

            for ball in self.listBall:
                ball.updateTrack()

    def changeDirection(self,a,ball):
        angle = (a * math.pi) / 180

        Yfdop1 = ball.newX * math.sin(angle)
        # Projection sign
        Yfdop1 = - Yfdop1

        Xf = ball.newX * math.cos(angle) + ball.newY * math.sin(angle)
        Yf = Yfdop1 + ball.newY * math.cos(angle)

        # Reflection
        Yf = -Yf

        Xdop1 = Xf * math.cos(angle)
        Xdop2 = Yf * math.sin(angle)

        Ydop1 = Xf * math.sin(angle)
        Ydop2 = Yf * math.cos(angle)

        # Projection sign
        Xdop2 = -Xdop2

        ball.newX = Xdop1 + Xdop2
        ball.newY = Ydop1 + Ydop2

    def paintEvent(self, event):
        ''' Draw all elements'''
        qp = QtGui.QPainter()
        size = self.size()
        qp.begin(self)
        self.drawBall(qp)
        self.drawLimitLine(qp,event)
        self.drawTrackBalls(qp)
        qp.end()

    def drawBall(self,qp):
        if self.existBall:
            for ball in self.listBall:
                ballColor = ball.color
                color = QtGui.QColor.fromRgb(ballColor[0], ballColor[1], ballColor[2], ballColor[3])
                pen = QtGui.QPen(color, 5, QtCore.Qt.SolidLine)
                qp.setPen(pen)
                qp.setBrush(color)
                qp.drawEllipse(ball.coords[0] - ball.radius[0],self.size().height() - ball.coords[1] - ball.radius[1], ball.radius[0]*2, ball.radius[1]*2)

    def drawLimitLine(self,qp,event):
        color = QtGui.QColor.fromRgb(100, 100, 100, 255)
        pen = QtGui.QPen(color, 5, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        if not self.existBall:
            qp.setFont( QtGui.QFont('Decorative',100))
            qp.drawText(event.rect(),QtCore.Qt.AlignCenter,'Press Space')


        qp.setBrush(QtGui.QColor.fromRgb(0,0,0,0))
        qp.drawRect(0,0,self.size().width() -1,self.size().height()-1)
        # -45 degress
        qp.drawLine(0, 0,self.size().width(),self.size().height())
        # -60 degress
        qp.drawLine(0, 0, - self.size().height()/math.tan(- PaintBall.RAD_60), self.size().height())
        # -30 degress
        qp.drawLine(0, 0, self.size().width(),self.size().height() - self.size().width() *(1 + math.tan(- PaintBall.RAD_30)))

    def drawTrackBalls(self,qp):
        if self.existBall:
            for ball in self.listBall:
                ballColor = ball.color
                color = QtGui.QColor.fromRgb(ballColor[0], ballColor[1], ballColor[2], ballColor[3])
                pen = QtGui.QPen(color, 2, QtCore.Qt.SolidLine)
                qp.setPen(pen)
                for i in range(len(ball.listTrack) - 1):
                    startX = ball.listTrack[i][0]
                    startY = ball.listTrack[i][1]
                    endX = ball.listTrack[i + 1][0]
                    endY = ball.listTrack[i + 1][1]
                    qp.drawLine(startX,self.size().height() - startY,endX,self.size().height() - endY)

if __name__ == "__main__":
    print('Module for Ball Simutator')