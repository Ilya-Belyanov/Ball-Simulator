from PyQt5 import QtCore, QtGui ,QtWidgets
from ballClass import Ball
import random
import math

class Board():
    RAD_45 = 0.785
    RAD_60 = 1.047
    RAD_30 = 0.524
    def __init__(self,size):
        self.size = size
        self.existBall = False
        self.countBall = 4
        self.gravity = 0
        self.loss = 0
        self.loss = float('{:.2f}'.format(self.loss))
        self.startF = 0
        self.startSpeed = 0
        self.listBall = []

    def createBall(self):
        self.listBall = []
        speed = self.startSpeed # pi/10 мс
        radius = ((10,10),(5,5),(10,10),(30,30))
        coords = ((100,500),(600,100),(600,300),(660,600))
        colors = ((255,0,0,255),(0,255,0,255),(242,245,26,255),(190,0,255,255))
        f = self.startF
        for i in range(self.countBall):
            R1 = radius[i][0]
            R2 = radius[i][1]
            x = coords[i][0]
            y = coords[i][1]
            color = colors[i]
            # f = random.randint(0, 360)
            ball = Ball(x,y,f,R1,R2,speed,color)
            self.listBall.append(ball)

        self.existBall = True

    def moveBall(self):
        if self.existBall:
            for ball in self.listBall:
                ball.coords[1] += ball.newY
                ball.coords[0] += ball.newX

                if ball.coords[1] > self.size().height() - ball.radius[1] or ball.coords[1] < ball.radius[1]:
                    ball.coords[1] -= ball.newY
                    ball.coords[0] -= ball.newX
                    # Simplification of calculations
                    ball.newY = - ball.newY
                    ball.lossSpeed(self.loss)
                    #f = 0
                    #ball.changeDirection(f, self.loss)

                if ball.coords[0] < ball.radius[0] or ball.coords[0] > self.size().width() - ball.radius[0]:
                    ball.coords[1] -= ball.newY
                    ball.coords[0] -= ball.newX
                    # Simplification of calculations
                    ball.newX = - ball.newX
                    ball.lossSpeed(self.loss)
                    #f = 90
                    #ball.changeDirection(f, self.loss)

            self.checkLimitLine(self.listBall[0],PaintBall.RAD_60,1,-60)

            self.checkLimitLine(self.listBall[1], PaintBall.RAD_60, -1, -60)
            self.checkLimitLine(self.listBall[1], PaintBall.RAD_45, 1, -45)

            self.checkLimitLine(self.listBall[2], PaintBall.RAD_45, -1, -45)
            self.checkLimitLine(self.listBall[2], PaintBall.RAD_30, 1, -30)

            self.checkLimitLine(self.listBall[3], PaintBall.RAD_30, -1, -30)

            for ball in self.listBall:
                ball.updateTrack()
                ball.newY -= self.gravity

    def checkLimitLine(self,ball,RAD,position,f):
        # Point of intersection with f degrees border up or down for balls
        # if position == 1 -> border is up , else position == -1 and border is down
        Y = - (math.tan(RAD)) * (
                ball.coords[0] +  position * ball.radius[0] * math.cos(RAD)) + \
             self.size().height()

        if position * (ball.coords[1] + position * ball.radius[1] * math.cos(RAD)) > (position * Y):
            ball.coords[1] -=  ball.newY
            ball.coords[0] -=  ball.newX
            ball.changeDirection(f, self.loss)

class PaintBall(QtWidgets.QFrame):
    '''Window of drawing'''
    RAD_45 = 0.785
    RAD_60 = 1.047
    RAD_30 = 0.524

    def createBoard(self):
        self.board = Board(self.size)
        
    def paintEvent(self, event):
        ''' Draw all elements'''
        qp = QtGui.QPainter()
        size = self.size()
        qp.begin(self)
        self.drawBall(qp)
        self.drawLimitLine(qp)
        self.drawSign(qp,event)
        self.drawTrackBalls(qp)
        qp.end()

    def drawBall(self,qp):
        if self.board.existBall:
            for ball in self.board.listBall:
                ballColor = ball.color
                color = QtGui.QColor.fromRgb(ballColor[0], ballColor[1], ballColor[2], ballColor[3])
                pen = QtGui.QPen(color, 5, QtCore.Qt.SolidLine)
                qp.setPen(pen)
                qp.setBrush(color)
                qp.drawEllipse(ball.coords[0] - ball.radius[0],self.size().height() - ball.coords[1] - ball.radius[1], ball.radius[0]*2, ball.radius[1]*2)

    def drawLimitLine(self,qp):
        color = QtGui.QColor.fromRgb(60, 213, 200, 255)
        pen = QtGui.QPen(color, 5, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        # -45 degress
        qp.drawLine(0, 0,self.size().width(),self.size().height())
        # -60 degress
        qp.drawLine(0, 0, - self.size().height()/math.tan(- PaintBall.RAD_60), self.size().height())
        # -30 degress
        qp.drawLine(0, 0, self.size().width(),self.size().height() - self.size().width() *(1 + math.tan(- PaintBall.RAD_30)))

    def drawSign(self,qp,event):
        color = QtGui.QColor.fromRgb(60, 213, 200, 255)
        pen = QtGui.QPen(color, 5, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        passive = 0
        for ball in self.board.listBall:
            if not ball.active:
                passive += 1

        if not self.board.existBall or passive == len(self.board.listBall):
            qp.setFont(QtGui.QFont('Decorative', 80))
            qp.drawText(event.rect(), QtCore.Qt.AlignCenter, 'Press Space')

    def drawTrackBalls(self,qp):
        if self.board.existBall:
            for ball in self.board.listBall:
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