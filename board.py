import math

from physicalObjects import Ball


class Board:

    def __init__(self, size):
        self.size = size
        self.gravity = 0
        self.loss = float('{:.2f}'.format(0))
        self.startF = 0
        self.startSpeed = 0
        self.balls = []

    def createBall(self, x, y, R, color=(255, 0, 0, 255)):
        ball = Ball(x, y, R, self.startF, self.startSpeed, color)
        if not self.checkCollision(ball):
            self.balls.append(ball)

    def clearBoard(self):
        self.balls = []

    def moveBall(self):
        for ball in self.balls:
            ball.move()
            self.checkCollision(ball)
            ball.updateTrack()
            ball.gravity(self.gravity)

    def checkCollision(self, ball):
        wallResult = self.checkWallCollision(ball)
        ballResult = self.checkBallsCollision(ball)
        return any([wallResult, ballResult])

    def checkWallCollision(self, ball):
        if ball.coords[1] > self.size().height() - ball.radius or ball.coords[1] < ball.radius:
            ball.back()
            ball.reflectionWall(0, self.loss)
            ball.move()
            return True

        elif ball.coords[0] < ball.radius or ball.coords[0] > self.size().width() - ball.radius:
            ball.back()
            ball.reflectionWall(90, self.loss)
            ball.move()
            return True

    def checkBallsCollision(self, ball):
        for b in self.balls:
            if b is not ball:
                if self.direct(ball, b) <= ball.radius + b.radius:
                    ball.back()
                    ball.reflectionBall(b, self.loss)
                    ball.move()
                    return True

    @staticmethod
    def direct(ballOne, ballTwo):
        return math.sqrt((ballOne.coords[0] - ballTwo.coords[0]) ** 2 + (ballOne.coords[1] - ballTwo.coords[1]) ** 2)