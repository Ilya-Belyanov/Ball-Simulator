from board import Board


class Adapter:
    def __init__(self, painter):
        self.painter = painter
        self.board = Board(self.painter.size)
        self.painter.setBoard(self.board)

    def setStartBoard(self):
        self.board.clearBoard()
        radius = (10, 10, 30, 30, 10)
        coords = [[i, i] for i in range(20, 800, 100)]
        colors = ((255, 0, 0, 255), (0, 255, 0, 255), (242, 245, 26, 255), (190, 0, 255, 255), (255, 255, 255, 255))
        for i in range(3):
            self.board.createBall(coords[i][0], coords[i][1], radius[i], colors[i])

    def moveBall(self):
        self.board.moveBall()

    def setStartSpeed(self, speed):
        self.board.startSpeed = float('{:.5f}'.format(speed / 3))

    def setLoss(self, loss):
        self.board.loss = float('{:.2f}'.format(loss / 100))

    def setGravity(self, gravity):
        self.board.gravity = gravity / 100

    def setStartAngle(self, angle):
        try:
            self.board.startF = float(angle)
        except ValueError:
            pass

    def speedBallStr(self, number):
        return str(int(self.board.balls[number].speed() * 100))

    def boardLoseStrProc(self):
        return str(int(self.board.loss * 100))

    def boardStartAngleStr(self):
        return str(self.board.startF)

    def boardGravityStr(self):
        return str(int(self.board.gravity * 100))

    def boardStartSpeedStr(self):
        return str(int(self.board.startSpeed * 100))