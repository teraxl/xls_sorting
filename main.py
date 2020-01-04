#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton, QWidget, QStyleFactory, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
import sys

import m_image
from GuiCount import Ui_Form
from ArKarton import ArKarton
from Titan import Titan
from Report import UnionReport


class MyTitan(QtWidgets.QWidget):

    def __init__(self):
        super(MyTitan, self).__init__()
        self.list_ar_karton = None
        self.list_titan = None
        self.__create_report = None

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_file_dialog_arkarton)
        self.ui.pushButton_2.clicked.connect(self.open_file_dialog_titan)
        self.ui.pushButton_3.clicked.connect(self.create_report)

        self.__titan = None
        self.__arkarton = None

    def visable_button(self):
        if (self.ui.lineEdit.text() and self.ui.lineEdit_2.text()) != "":
            self.ui.pushButton_3.setEnabled(True)
        else:
            self.ui.pushButton_3.setEnabled(False)

    def load_file_arkarton(self, file):
        self.__arkarton = ArKarton(file, self.ui.progress)
        sp = str(file).split("/")
        self.ui.progress.setFormat(sp[int(len(sp)) - 1] + " загружен --> " + "%p%")
        self.__arkarton.read_xls()
        self.list_ar_karton = self.__arkarton.get_data()

        if not self.list_ar_karton != 0:
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

        self.visable_button()

    def open_file_dialog_arkarton(self):
        dialog = QFileDialog(self)
        filename = dialog.getOpenFileName(
            self, "Выберете файл от АО АР Картон",
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
        self.__titan = Titan(file, self.ui.progress)
        sp = str(file).split("/")
        self.ui.progress.setFormat(sp[int(len(sp)) - 1] + " загружен --> " + "%p%")
        self.__titan.read_xlsx()
        self.list_titan = self.__titan.get_data()

        if not self.list_ar_karton != 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("Внимание!!!")
            msg.setText("Выбранный вами файл не является файлом\n"
                        "созданным ООО \"ТИТАН ЛОГИСТИК\"\n"
                        "Желаете выбрать файл снова?\n")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()

            if msg.exec() == QMessageBox.Ok:
                self.open_file_dialog_titan()
            else:
                pass

        self.visable_button()

    def open_file_dialog_titan(self):
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
                self.open_file_dialog_titan()
            else:
                pass
            return False

    def create_report(self):
        self.__create_report = UnionReport(ar_karton=self.list_ar_karton, titan=self.list_titan, progress=self.ui.progress)
        sp = str(self.__create_report.get_name).split("/")
        self.ui.progress.setFormat(sp[int(len(sp)) - 1] + " был сформирован --> " + "%p%")
        self.ui.progress.setStyleSheet(
            "border: 2px solid grey;"
            "border-radius: 5px;"
            "text-align: center;"
            "}"
            "QProgressBar::chunk {"
            "background-color: #00ff00;"
            "width: 20px;}"
            "QProgressBar::chunk[urgent=true] {"
            "background-color: red;"
            "}"
        )
        self.__create_report.Union()
        self.__create_report.create_xls()

        self.ui.pushButton_3.setDisabled(True)
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

        self.image = QPixmap(m_image.icon_app)

        self.label = QLabel()
        self.label.setPixmap(self.image)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        wg = QtWidgets.QWidget(self)
        wg.setLayout(self.layout)
        wg.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)
        wg.setWindowModality(Qt.ApplicationModal)
        wg.activateWindow()
        wg.resize(200, 400)
        wg.show()


app = QtWidgets.QApplication([])
application = MyTitan()
application.setWindowIcon(QIcon(QPixmap(m_image.icon_app)))
application.setWindowFlags(
    Qt.Window |
    Qt.WindowMinimizeButtonHint |
    Qt.WindowCloseButtonHint
)
application.show()
sys.exit(app.exec())
