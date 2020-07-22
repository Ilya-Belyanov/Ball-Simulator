import math

from physicalObjects import Ball


class Board:

    def __init__(self, size):
        self.size = size
        self.existBall = False
        self.countBall = 4
        self.gravity = 0
        self.loss = float('{:.2f}'.format(0))
        self.startF = 0
        self.startSpeed = 0
        self.balls = []

    def createBall(self):
        self.balls = []
        speed = self.startSpeed  # pi/10 мс
        radius = (10, 10, 30, 30)
        coords = ((100, 491), (600, 500), (100, 300), (660, 600))
        colors = ((255, 0, 0, 255), (0, 255, 0, 255), (242, 245, 26, 255), (190, 0, 255, 255))
        f = self.startF
        for i in range(self.countBall):
            R = radius[i]
            x = coords[i][0]
            y = coords[i][1]
            color = colors[i]
            ball = Ball(x, y, R, f, speed, color)
            self.balls.append(ball)

        self.existBall = True

    def moveBall(self):
        if self.existBall:
            for ball in self.balls:
                ball.move()
                self.checkWallCollision(ball)
                self.checkBallsCollision(ball)
                ball.updateTrack()
                ball.gravity(self.gravity)

    def checkWallCollision(self, ball):
        if ball.coords[1] > self.size().height() - ball.radius or ball.coords[1] < ball.radius:
            ball.back()
            ball.reflectionWall(0, self.loss)

        if ball.coords[0] < ball.radius or ball.coords[0] > self.size().width() - ball.radius:
            ball.back()
            ball.reflectionWall(90, self.loss)

    def checkBallsCollision(self, ball):
        for b in self.balls:
            if b is not ball:
                if self.direct(ball, b) <= ball.radius + b.radius:
                    ball.back()
                    ball.reflectionBall(b, self.loss)
                    ball.move()

    @staticmethod
    def direct(ballOne, ballTwo):
        return math.sqrt((ballOne.coords[0] - ballTwo.coords[0]) ** 2 + (ballOne.coords[1] - ballTwo.coords[1]) ** 2)