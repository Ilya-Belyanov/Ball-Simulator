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
        self.angle = self.convertToRadian(self.f)
        self.tg = math.tan(self.angle)

        self.deltaX =  self.speed /  math.sqrt(1 + self.tg ** 2)
        self.deltaY =  abs(self.tg) * self.deltaX

        self.deltaX = float('{:.2f}'.format(self.deltaX))
        self.deltaY = float('{:.2f}'.format(self.deltaY))

        self.deltaX = self.checkSign(math.cos(self.angle), self.deltaX)
        self.deltaY = self.checkSign(math.sin(self.angle), self.deltaY)

    def changeDirection(self,a,loss):
        angle = self.convertToRadian(a)

        Yfdop1 = self.deltaX * math.sin(angle)
        # Projection sign
        Yfdop1 = - Yfdop1

        Xf = self.deltaX * math.cos(angle) + self.deltaY * math.sin(angle)
        Yf = Yfdop1 + self.deltaY * math.cos(angle)

        # Reflection
        Yf = -Yf

        Xdop1 = Xf * math.cos(angle)
        Xdop2 = Yf * math.sin(angle)

        Ydop1 = Xf * math.sin(angle)
        Ydop2 = Yf * math.cos(angle)

        # Projection sign
        Xdop2 = -Xdop2

        self.deltaX = Xdop1 + Xdop2
        self.deltaY = Ydop1 + Ydop2

        self.lossSpeed(loss)

    def lossSpeed(self,loss):
        '''Losses during scattering'''
        self.deltaX *= (1 - loss)
        self.deltaY *= (1 - loss)
        self.checkMin()

    def checkMin(self):
        if self.speedBall() < 0.002 :
            self.deltaX = 0
            self.deltaY = 0
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
        speed = math.sqrt(self.deltaX ** 2 + self.deltaY ** 2)
        speed = float('{:.2f}'.format(speed))
        return speed

    def move(self,direction):
        self.coords[1] += self.deltaY * direction
        self.coords[0] += self.deltaX * direction

    @staticmethod
    def convertToRadian(a):
        return  (a * math.pi) / 180

    @staticmethod
    def checkSign(function,delta):
        if function < 0:
           return -delta
        else:
           return delta


if __name__ == "__main__":
    print('Module for Ball Simutator')

