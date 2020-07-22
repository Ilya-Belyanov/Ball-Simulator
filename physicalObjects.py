import math
from abc import ABC, abstractmethod

from vector import Vector
from reflector import Reflector


class PhysicalObject(ABC):
    def __init__(self, f, speed, color):
        self.f = f
        self.color = color
        self.active = True
        self.vector = Vector()
        self.vector.createVector(self.f, speed)

        self.reflector = Reflector(self)

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def back(self):
        pass

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
        if self.speed() < 0.002:
            self.vector.clear()
            self.active = False
        else:
            self.active = True

    def speed(self):
        return float('{:.2f}'.format(self.vector.length()))

    @abstractmethod
    def mass(self):
        pass


class Ball(PhysicalObject):
    def __init__(self, X, Y, R, f, speed, color):
        super().__init__(f, speed, color)
        self.coords = [X, Y]
        self.radius = R
        self.track = [[X, Y] for i in range(60)]

    def move(self):
        self.coords[1] += self.vector.y
        self.coords[0] += self.vector.x

    def back(self):
        self.coords[1] -= self.vector.y
        self.coords[0] -= self.vector.x

    def updateTrack(self):
        trackCopy = self.track
        self.track = []
        coord = [self.coords[0], self.coords[1]]
        self.track.append(coord)
        for i in range(len(trackCopy) - 1):
            self.track.append(trackCopy[i])

    def mass(self):
        return math.pi * (self.radius ** 2)


if __name__ == "__main__":
    print('Module for Ball Simulator')
