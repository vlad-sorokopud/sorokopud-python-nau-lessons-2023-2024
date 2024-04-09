# system import
import random

# lib import
import pandas as pd
from PyQt5 import QtWidgets

# local import
from .ui_data_dialog_window import Ui_Dialog


class DataDialogWindow(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)
        self.__ui.retranslateUi(self)

        # set events
        self.__ui.loadButton.clicked.connect(self.__on_load_button)

        # crate variables
        self.__df = None
        self.__columns = []

        # test initialize
        self.__load_data('../notebooks/titanic.csv')

    #----------------------- events

    def __on_load_button(self):
        path, format_option = QtWidgets.QFileDialog.getOpenFileName(self, "Select data file", "",
                                                         "All Files (*);;Text Files (*.csv)")
        if path != '':
            self.__load_data(path)

    #----------------------- logic

    def __load_data(self, f):
        self.__df = pd.read_csv(f)
        self.__columns.clear()

        for c in self.__df.columns:
            column = {
                "name": c,
                "color": f"#{(hex(random.randrange(0, 2**24)))[2:]}"
            }

            self.__columns.append(column)

            l = QtWidgets.QLabel()
            l.setText(c)
            print(column["color"])
            l.setStyleSheet("color:\"" + column["color"]+"\"")

            self.__ui.columns_container.addWidget(l)


