import math

from vector import Vector
from reflector import Reflector


class Ball:
    def __init__(self, X, Y, f, R, speed, color):
        self.coords = [X, Y]
        self.f = f
        self.radius = R
        self.color = color
        self.track = [[X, Y] for i in range(60)]
        self.active = True
        self.vector = Vector()
        self.vector.createVector(self.f, speed)

        self.reflector = Reflector(self)

    def move(self):
        self.coords[1] += self.vector.y
        self.coords[0] += self.vector.x

    def back(self):
        self.coords[1] -= self.vector.y
        self.coords[0] -= self.vector.x

    def gravity(self, gravity):
        self.vector.y -= gravity

    def reflectionWall(self, a, loss):
        self.reflector.reflectionWall(a)
        self.lossSpeed(loss)

    def reflectionBall(self, ball, loss):
        self.reflector.reflectionBall(ball)
        self.lossSpeed(loss)

    def lossSpeed(self, loss):
        self.vector *= (1 - loss)
        self.checkMin()

    def checkMin(self):
        if self.speedBall() < 0.002:
            self.vector.clear()
            self.active = False
        else:
            self.active = True

    def updateTrack(self):
        trackCopy = self.track
        self.track = []
        coord = [self.coords[0], self.coords[1]]
        self.track.append(coord)
        for i in range(len(trackCopy) - 1):
            self.track.append(trackCopy[i])

    def mass(self):
        return 0.01 * math.pi * (self.radius ** 2)

    def speedBall(self):
        return float('{:.2f}'.format(self.vector.length()))


if __name__ == "__main__":
    print('Module for Ball Simulator')
