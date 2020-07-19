from PyQt5 import QtWidgets
from interface import Interface
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Interface()
    application.show()
    sys.exit(app.exec())
