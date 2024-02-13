# system import
import sys

# lib import
from PyQt5 import QtWidgets

# local import
from ui import MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
