#!/usr/bin/env python
# coding=utf-8

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton
from PyQt5.QtCore import Qt
import sys
from GuiCount import Ui_Form
import ArKarton
from Titan import Titan
from Report import UnionReport


class MyTitan(QtWidgets.QWidget):

    def __init__(self):
        super(MyTitan, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_file_dialog_arkarton)
        self.ui.pushButton_2.clicked.connect(self.openFileDialogTitan)
        self.ui.pushButton_3.clicked.connect(self.CreateReport)

    def visable_button(self):
        if (self.ui.lineEdit.text() and self.ui.lineEdit_2.text()) != "":
            self.ui.pushButton_3.setEnabled(True)
        else:
            self.ui.pushButton_3.setEnabled(False)

    def load_file_arkarton(self, file):
        xl = ArKarton.ArKarton(file, self.ui.progress)
        sp = str(file).split("/")
        self.ui.progress.setFormat(sp[int(len(sp)) - 1] + " загружен --> " + "%p%")

        if not xl.read_xls() != 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("Внимание!!!")
            msg.setText("Выбранный вами файл не является файлом\n"
                        "созданным ООО \"АР-Картон\"\n"
                        "Желаете выбрать файл снова?\n")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()

            if msg.exec() == QMessageBox.Ok:
                self.open_file_dialog_arkarton()
            else:
                pass
        else:
            self.listArKarton = xl.read_xls()

        self.visable_button()

    def open_file_dialog_arkarton(self):
        dialog = QFileDialog(self)
        filename = dialog.getOpenFileName(self,
                                          "Выберете файл от АО АР Картон",
                                          "", "ArKarton (*.xls)",
                                          options=dialog.options())[0]
        if not filename == '':
            self.ui.lineEdit.setText(filename)
            self.load_file_arkarton(filename)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Внимание!!!")
            msg.setText("Файл не был выбран\n"
                        "Желаете выбрать файл снова?\n")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()

            if msg.exec() == QMessageBox.Ok:
                self.open_file_dialog_arkarton()
            else:
                pass

            return False

    def load_file_titan(self, file):
        xl = Titan(file, self.ui.progress)
        sp = str(file).split("/")
        self.ui.progress.setFormat(sp[int(len(sp)) - 1] + " загружен --> " + "%p%")

        if not xl.read_xlsx() != 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("Внимание!!!")
            msg.setText("Выбранный вами файл не является файлом\n"
                        "созданным ООО \"ТИТАН ЛОГИСТИК\"\n"
                        "Желаете выбрать файл снова?\n")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()

            if msg.exec() == QMessageBox.Ok:
                self.openFileDialogTitan()
            else:
                pass
        else:
            self.listTitan = xl.read_xlsx()

        self.visable_button()

    def openFileDialogTitan(self):
        dialog = QFileDialog(self)
        filename = dialog.getOpenFileName(self,
                                          "Выберете файл от ООО Титан Логистик",
                                          "", "Титан Логистик(*.xlsx)",
                                          options=dialog.options())[0]
        if not filename == '':
            self.ui.lineEdit_2.setText(filename)
            self.load_file_titan(filename)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Внимание!!!")
            msg.setText("Файл не был выбран\n"
                        "Желаете выбрать файл снова?\n")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()

            if msg.exec() == QMessageBox.Ok:
                self.openFileDialogTitan()
            else:
                pass
            return False

    def CreateReport(self):
        ur = UnionReport(ar_karton=self.listArKarton, titan=self.listTitan)
        ur.Union()


app = QtWidgets.QApplication([])
application = MyTitan()
application.setWindowFlags(
    Qt.Window |
    Qt.WindowMinimizeButtonHint |
    Qt.WindowCloseButtonHint
)
application.show()

sys.exit(app.exec())
