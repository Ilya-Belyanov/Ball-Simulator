from board import Board


class Adapter:
    def __init__(self, painter):
        self.painter = painter
        self.board = Board(self.painter.size)
        self.painter.setBoard(self.board)

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