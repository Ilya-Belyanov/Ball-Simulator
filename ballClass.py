import math

class Ball():
    def __init__(self,X,Y,f,R1,R2,speed,color):
        self.color = color
        self.coords = [X,Y]
        self.radius = [R1,R2]
        self.speed = speed
        self.f = f
        x = X
        y = Y
        self.listTrack = [[x,y] for i in range(100)]
        self.active = True
        self.projectionSpeed()

    def projectionSpeed(self):
        '''Count projection of speed on X and Y axis'''
        self.angle = (self.f * math.pi) / 180
        self.tg = math.sin(self.angle) / math.cos(self.angle)

        self.newX = self.speed /  math.sqrt(1 + self.tg ** 2)
        self.newY =  abs(self.tg) * self.newX
        if math.cos(self.angle)< 0:
            self.newX = - self.newX
        if math.sin(self.angle) < 0:
            self.newY = - self.newY
        if self.f == 90 or self.f == 270:
            self.newX = 0

        if self.f == 0 or self.f == 180:
            self.newY = 0

    def updateTrack(self):
        oldTrack =  self.listTrack
        self.listTrack = []

        x = self.coords[0]
        y = self.coords[1]
        coord = [x,y]
        self.listTrack.append(coord)
        for i in range(len(oldTrack) - 1):
            self.listTrack.append(oldTrack[i])

    def checkMin(self):
        if self.speedBall() <= 0.05 :
            self.newX = 0
            self.newY = 0
            self.active = False
        else:
            self.active = True
    
    def speedBall(self):
        speed = math.sqrt(self.newX ** 2 + self.newY ** 2)
        speed = float('{:.2f}'.format(speed))
        return speed

if __name__ == "__main__":
    print('Module for Ball Simutator')

