from PyQt5 import QtCore, QtGui, QtWidgets


class PaintBoard(QtWidgets.QFrame):

    def setBoard(self, board):
        self.board = board

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawTrackBalls(qp)
        self.drawBall(qp)
        self.drawSign(qp, event)
        qp.end()

    def drawBall(self, qp):
        if self.board.existBall:
            for ball in self.board.balls:
                color = (ball.color[0], ball.color[1], ball.color[2], ball.color[3])
                self.setPencil(qp, color, 5)
                qp.setBrush(QtGui.QColor.fromRgb(ball.color[0], ball.color[1], ball.color[2], ball.color[3]))
                qp.drawEllipse(ball.coords[0] - ball.radius, self.size().height() - ball.coords[1] - ball.radius,
                               ball.radius * 2, ball.radius * 2)

    def drawSign(self, qp, event):
        color = (60, 213, 200, 255)
        self.setPencil(qp, color, 5)
        passive = 0
        for ball in self.board.balls:
            if not ball.active:
                passive += 1

        if not self.board.existBall or passive == len(self.board.balls):
            qp.setFont(QtGui.QFont('Decorative', 80))
            qp.drawText(event.rect(), QtCore.Qt.AlignCenter, 'Press Space')

    def drawTrackBalls(self, qp):
        if self.board.existBall:
            for ball in self.board.balls:
                color = (ball.color[0], ball.color[1], ball.color[2], ball.color[3])
                self.setPencil(qp, color, 2)

                for i in range(len(ball.track) - 1):
                    startX = ball.track[i][0]
                    startY = ball.track[i][1]
                    endX = ball.track[i + 1][0]
                    endY = ball.track[i + 1][1]
                    qp.drawLine(startX, self.size().height() - startY, endX, self.size().height() - endY)

    @staticmethod
    def setPencil(qp, color, thickness):
        color = QtGui.QColor.fromRgb(color[0], color[1], color[2], color[3])
        pen = QtGui.QPen(color, thickness, QtCore.Qt.SolidLine)
        qp.setPen(pen)


if __name__ == "__main__":
    print('Module for Ball Simutator')
