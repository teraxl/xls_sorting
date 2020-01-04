# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QRegion, QPalette, QColor, QFont
from PyQt5.QtWidgets import QProgressBar


class Ui_Form(object):
    def __init__(self):
        self.gridLayout = None
        self.sizePolicy = None
        self.verticalLayout = None
        self.font = None
        self.horizontalLayout = None
        self.horizontalLayout_2 = None
        self.horizontalLayout_3 = None
        self.label = None
        self.label_2 = None
        self.lineEdit = None
        self.lineEdit_2 = None
        self.spacerItem = None
        self.pushButton = None
        self.pushButton_2 = None
        self.pushButton_3 = None
        self.progress = None
        self.palette = None

    def setupUi(self, Form):
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())

        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.setSizePolicy(self.sizePolicy)
        Form.setWindowTitle("Общий отчет")
        Form.setStatusTip("")
        Form.setAccessibleName("")
        Form.setAccessibleDescription("")
        Form.setWindowFilePath("")
        Form.resize(588, 158)

        self.font = QtGui.QFont()
        self.font.setFamily("Segoe UI")
        self.font.setPointSize(10)
        self.font.setBold(True)

        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.label.setFont(self.font)
        self.label.setFixedSize(QtCore.QSize(118, 30))
        self.label.setStyleSheet(
            "QLabel {"
            "color: grey;"
            "font-size: 15px;"
            "}"
        )

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(self.font)
        self.label_2.setFixedSize(QtCore.QSize(118, 30))
        self.label_2.setStyleSheet(
            "QLabel {"
            "color: grey;"
            "font-size: 15px;"
            "}"
        )

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('Выберете файл отчета от ООО АР Катрон')
        self.lineEdit.setFont(self.font)
        self.lineEdit.setTextMargins(3, 0, 0, 0)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setFixedSize(QtCore.QSize(450, 32))
        self.palette = self.lineEdit.palette()
        self.palette.setColor(QPalette.PlaceholderText, QColor('#757575'))
        self.palette.setColor(QPalette.Text, QColor('#404040'))
        self.lineEdit.setPalette(self.palette)
        self.lineEdit.setStyleSheet(
            "QLineEdit {"
            "background-color: #e1e2e3;"
            "border: 2px solid grey;"
            "border-radius: 5px;"
            "border-width:2px;"
            "}"
        )

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText('Выберете файл отчета от ООО Титан Логистик')
        self.lineEdit_2.setFont(self.font)
        self.lineEdit_2.setTextMargins(5, 0, 0, 0)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setFixedSize(QtCore.QSize(450, 32))
        self.lineEdit_2.setPalette(self.palette)
        self.lineEdit_2.setStyleSheet(
            "QLineEdit {"
            "background-color: #e1e2e3;"
            "border: 2px solid grey;"
            "border-radius: 5px;"
            "border-width:2px;"
            "}")

        # Create Button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(self.font)
        self.pushButton.setSizePolicy(self.sizePolicy)
        self.pushButton.setFixedSize(QtCore.QSize(32, 32))
        self.palette = self.pushButton.palette()
        self.palette.setColor(QPalette.ButtonText, QColor('grey'))
        self.pushButton.setPalette(self.palette)
        self.pushButton.setStyleSheet(
            "QPushButton {"
            "background-color: #05B8CC;"
            "border: 2px solid grey;"
            "border-radius: 5px;"
            "border-width:2px;"
            "}")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(self.font)
        self.pushButton_2.setSizePolicy(self.sizePolicy)
        self.pushButton_2.setFixedSize(QtCore.QSize(32, 32))
        self.palette = self.pushButton_2.palette()
        self.palette.setColor(QPalette.ButtonText, QColor('grey'))
        self.pushButton_2.setPalette(self.palette)
        self.pushButton_2.setStyleSheet(
            "QPushButton {"
            "background-color: #05B8CC;"
            "border: 2px solid grey;"
            "border-radius: 5px;"
            "border-width:2px;"
            "}")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setSizePolicy(self.sizePolicy)
        self.pushButton_3.setFont(self.font)
        self.pushButton_3.setFixedSize(QtCore.QSize(self.lineEdit_2.size().width()/3, 30))
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setStyleSheet(
            "QPushButton {"
            "background-color: #05B8CC;"
            "border: 2px solid grey;"
            "border-radius: 5px;"
            "border-width:2px;"
            "}")

        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.progress = QProgressBar(Form)
        self.progress.setObjectName("progress")
        self.progress.setFont(self.font)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)
        self.progress.setFixedSize(455, 30)
        self.palette = self.progress.palette()
        self.palette.setColor(QPalette.Text, QColor('#353535'))
        self.progress.setPalette(self.palette)
        self.progress.setStyleSheet(
            "color: grey;"
            "border: 2px solid grey;"
            "border-radius: 5px;"
            "text-align: center;"
            "}"
            "QProgressBar::chunk {"
            "background-color: #05B8CC;"
            "width: 20px;}"
            "QProgressBar::chunk[urgent=true] {"
            "background-color: red;"
            "}"
        )
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.addWidget(self.progress)
        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setSpacing(5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "АР Картон"))
        self.label_2.setText(_translate("Form", "Титан-Логистик"))
        self.pushButton.setText(_translate("Form", "+"))
        self.pushButton_2.setText(_translate("Form", "+"))
        self.pushButton_3.setText(_translate("Form", "Сравнить файлы"))
