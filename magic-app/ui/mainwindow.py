# system import

# lib import
from PyQt5 import QtWidgets

# local import
from .ui_mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__ui.retranslateUi(self)

        # set events
        self.__ui.readButton.clicked.connect(self.__on_read_button)

    def __on_read_button(self):
        text = self.__ui.inputTextEdit.toPlainText()
        self.__ui.readTextLabel.setText(f"Input text: [{text}]")


