import math

from physicalObjects import Ball


class Board:

    def __init__(self, size):
        self.size = size
        self.countBall = 5
        self.gravity = 0
        self.loss = float('{:.2f}'.format(0))
        self.startF = 0
        self.startSpeed = 0
        self.balls = []

    def createBall(self):
        self.balls = []
        speed = self.startSpeed  # pi/10 мс
        radius = (10, 10, 30, 30, 10)
        coords = [[i, i] for i in range(20, 800, 100)]
        colors = ((255, 0, 0, 255), (0, 255, 0, 255), (242, 245, 26, 255), (190, 0, 255, 255), (255, 255, 255, 255))
        f = self.startF
        for i in range(self.countBall):
            R = radius[i]
            x = coords[i][0]
            y = coords[i][1]
            color = colors[i]
            ball = Ball(x, y, R, f, speed, color)
            self.balls.append(ball)

    def moveBall(self):
        for ball in self.balls:
            self.checkCollision(ball)
            ball.move()
            self.checkCollision(ball)
            ball.updateTrack()
            ball.gravity(self.gravity)

    def checkCollision(self, ball):
        self.checkWallCollision(ball)
        self.checkBallsCollision(ball)

    def checkWallCollision(self, ball):
        if ball.coords[1] > self.size().height() - ball.radius or ball.coords[1] < ball.radius:
            ball.back()
            ball.reflectionWall(0, self.loss)
            ball.move()

        elif ball.coords[0] < ball.radius or ball.coords[0] > self.size().width() - ball.radius:
            ball.back()
            ball.reflectionWall(90, self.loss)
            ball.move()

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