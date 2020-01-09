# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

import m_image


class Ui_Form(object):
    def __init__(self):
        pass

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(329, 246)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.label.setGeometry(0, 0, 50, 50)
        self.image = QPixmap(m_image.icon_app)
        self.label.setPixmap(self.image)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(23)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.textBrowser = QtWidgets.QTextBrowser()
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        # self.pushButton = QtWidgets.QPushButton()
        # self.pushButton.setObjectName("pushButton")
        # self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.label, 0, 0)
        self.gridLayout.addLayout(self.verticalLayout, 1, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Об авторе"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Программа предназначена для сравнения содержимого двух файлов отчетов</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> от ООО &quot;АР Картон&quot; и ООО &quot;Титан Логистик&quot;</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Автор: Муга А.В.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">email: muga.alexandr@yandex.ru</p></body></html>"))
        # self.pushButton.setText(_translate("Form", "ОК"))


class AboutMe(QtWidgets.QWidget):

    def __init__(self):
        super(AboutMe, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)


