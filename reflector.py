import math

from vector import Vector


class Reflector:
    def __init__(self, ball):
        self.ball = ball

    def reflectionWall(self, wall):
        angle = self.convertToRadian(wall)

        Yfdop1 = self.ball.vector.x * math.sin(angle)
        # Projection sign
        Yfdop1 = - Yfdop1

        Xf = self.ball.vector.x * math.cos(angle) + self.ball.vector.y * math.sin(angle)
        Yf = Yfdop1 + self.ball.vector.y * math.cos(angle)

        # Reflection
        Yf = -Yf

        Xdop1 = Xf * math.cos(angle)
        Xdop2 = Yf * math.sin(angle)

        Ydop1 = Xf * math.sin(angle)
        Ydop2 = Yf * math.cos(angle)

        # Projection sign
        Xdop2 = -Xdop2
        self.ball.vector = Vector(Xdop1 + Xdop2, Ydop1 + Ydop2)

    def reflectionBall(self, ball):
        copyBall = ball.vector
        self.ball.vector = self.ball.vector - copyBall

        angleCollision = math.atan2(ball.coords[1] - self.ball.coords[1], ball.coords[0] - self.ball.coords[0])

        speedCollisionAlong = (self.ball.vector.x * math.cos(angleCollision)) \
                              + (self.ball.vector.y * math.sin(angleCollision))

        speedCollisionOrt = - self.ball.vector.x * math.sin(angleCollision) \
                            + self.ball.vector.y * math.cos(angleCollision)

        newSpeedSelf = (self.ball.mass() - ball.mass()) * speedCollisionAlong / (self.ball.mass() + ball.mass())
        newSpeedOther = 2 * self.ball.mass() * speedCollisionAlong / (self.ball.mass() + ball.mass())

        self.ball.vector = Vector(newSpeedSelf * math.cos(angleCollision) - speedCollisionOrt * math.sin(angleCollision),
                                  newSpeedSelf * math.sin(angleCollision) + speedCollisionOrt * math.cos(angleCollision))
        ball.vector = Vector(newSpeedOther * math.cos(angleCollision),
                             newSpeedOther * math.sin(angleCollision))

        self.ball.vector = self.ball.vector + copyBall
        ball.vector = ball.vector + copyBall

    @staticmethod
    def convertToRadian(a):
        return (a * math.pi) / 180
