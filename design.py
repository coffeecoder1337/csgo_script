# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 220)
        MainWindow.setMinimumSize(QSize(540, 220))
        MainWindow.setMaximumSize(QSize(540, 220))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color: #fff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(155, 60, 230, 50))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 25px;\n"
"background-color: rgb(41, 91, 255);\n"
"color: #fff;\n"
"font-size: 20px;\n"
"text-transform: uppercase;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(125, 130, 290, 30))
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        MainWindow.setProperty("test", QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0447\u0430\u0442\u044c", None))
        self.label.setText("")
    # retranslateUi

