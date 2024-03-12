# lib import
from PyQt5 import QtWidgets


def show_default_dialog(text: str, title:str = "Information"):
    ms = QtWidgets.QMessageBox()
    ms.setWindowTitle(title)
    ms.setText(text)
    ms.exec()
