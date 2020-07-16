import math


class Vector:
    def __init__(self, x=0, y=0):
        self.__x = float('{:.2f}'.format(x))
        self.__y = float('{:.2f}'.format(y))

    def createVector(self, angle, length):
        __angle = self.convertToRadian(angle)

        self.__x = float('{:.2f}'.format(math.cos(__angle) * length))
        self.__y = float('{:.2f}'.format(math.sin(__angle) * length))

    def clear(self):
        self.__x = 0
        self.__y = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def length(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def __imul__(self, length):
        self.__x *= length
        self.__y *= length
        return self

    def __add__(self, vector):
        return Vector(self.__x + vector.x, self.__y + vector.y)

    def __sub__(self, vector):
        return Vector(self.__x - vector.x, self.__y - vector.y)

    @staticmethod
    def convertToRadian(a):
        return (a * math.pi) / 180

    @y.setter
    def y(self, value):
        self.__y = value