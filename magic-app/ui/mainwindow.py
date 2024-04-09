# system import

# lib import
from PyQt5 import QtWidgets

# local import
import qt_tools
from .ui_mainwindow import Ui_MainWindow
from .data_dialog_window import DataDialogWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__ui.retranslateUi(self)

        # set events
        self.__ui.loginButton.clicked.connect(self.__on_login_button)
        self.__ui.openDataWindowButton.clicked.connect(self.__on_data_dialog_button)

        # set some ui elements to default
        self.__ui.stackedWidget.setCurrentIndex(0)

    def __on_login_button(self):
        login = self.__ui.loginEdit.text()
        password = self.__ui.passwordEdit.text()

        if login == "admin" and password == "admin": # TODO Store in config/db, add hash
            self.__ui.stackedWidget.setCurrentIndex(1)
        else:
            qt_tools.show_default_dialog("Wrong credentials")

    def __on_data_dialog_button(self):
        d = DataDialogWindow()
        d.exec()

    def closeEvent(self, event):
        print("On close")


