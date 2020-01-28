import math

class Ball():
    def __init__(self,X,Y,f,R1,R2,speed,color):
        self.color = color
        self.coords = [X,Y]
        self.radius = [R1,R2]
        self.speed = speed
        self.f = f
        self.listTrack = [[X,Y] for i in range(60)]
        self.active = True
        self.projectionSpeed()

    def projectionSpeed(self):
        '''Count projection of speed on X and Y axis'''
        self.angle = (self.f * math.pi) / 180
        self.tg = math.tan(self.angle)

        self.newX =  self.speed /  math.sqrt(1 + self.tg ** 2)
        self.newY =  abs(self.tg) * self.newX

        self.newX = float('{:.2f}'.format(self.newX))
        self.newY = float('{:.2f}'.format(self.newY))

        if math.cos(self.angle)< 0:
           self.newX = - self.newX
        if math.sin(self.angle) < 0:
           self.newY = - self.newY

    def changeDirection(self,a,loss):
        angle = (a * math.pi) / 180

        Yfdop1 = self.newX * math.sin(angle)
        # Projection sign
        Yfdop1 = - Yfdop1

        Xf = self.newX * math.cos(angle) + self.newY * math.sin(angle)
        Yf = Yfdop1 + self.newY * math.cos(angle)

        # Reflection
        Yf = -Yf

        Xdop1 = Xf * math.cos(angle)
        Xdop2 = Yf * math.sin(angle)

        Ydop1 = Xf * math.sin(angle)
        Ydop2 = Yf * math.cos(angle)

        # Projection sign
        Xdop2 = -Xdop2

        self.newX = Xdop1 + Xdop2
        self.newY = Ydop1 + Ydop2

        self.lossSpeed(loss)

    def lossSpeed(self,loss):
        '''Losses during scattering'''
        self.newX *= (1 - loss)
        self.newY *= (1 - loss)
        self.checkMin()

    def checkMin(self):
        if self.speedBall() < 0.002 :
            self.newX = 0
            self.newY = 0
            self.active = False
        else:
            self.active = True

    def updateTrack(self):
        oldTrack =  self.listTrack
        self.listTrack = []
        x = self.coords[0]
        y = self.coords[1]
        coord = [x,y]
        self.listTrack.append(coord)
        for i in range(len(oldTrack) - 1):
            self.listTrack.append(oldTrack[i])

    def speedBall(self):
        speed = math.sqrt(self.newX ** 2 + self.newY ** 2)
        speed = float('{:.2f}'.format(speed))
        return speed

if __name__ == "__main__":
    print('Module for Ball Simutator')

