# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courses.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 745)
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo1 = QtWidgets.QLabel(self.centralwidget)
        self.photo1.setGeometry(QtCore.QRect(30, 60, 211, 131))
        self.photo1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.photo1.setText("")
        self.photo1.setObjectName("photo1")
        self.podrobnee1 = QtWidgets.QPushButton(self.centralwidget)
        self.podrobnee1.setGeometry(QtCore.QRect(352, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.podrobnee1.setFont(font)
        self.podrobnee1.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.podrobnee1.setObjectName("podrobnee1")
        self.opis1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.opis1.setGeometry(QtCore.QRect(270, 60, 331, 91))
        self.opis1.setObjectName("opis1")
        self.oplata1 = QtWidgets.QPushButton(self.centralwidget)
        self.oplata1.setGeometry(QtCore.QRect(470, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.oplata1.setFont(font)
        self.oplata1.setStyleSheet("background-color: rgb(213, 214, 255);")
        self.oplata1.setObjectName("oplata1")
        self.oplata2 = QtWidgets.QPushButton(self.centralwidget)
        self.oplata2.setGeometry(QtCore.QRect(468, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.oplata2.setFont(font)
        self.oplata2.setStyleSheet("background-color: rgb(213, 214, 255);")
        self.oplata2.setObjectName("oplata2")
        self.photo2 = QtWidgets.QLabel(self.centralwidget)
        self.photo2.setGeometry(QtCore.QRect(28, 280, 211, 131))
        self.photo2.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.photo2.setText("")
        self.photo2.setObjectName("photo2")
        self.opis2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.opis2.setGeometry(QtCore.QRect(268, 280, 331, 91))
        self.opis2.setObjectName("opis2")
        self.podrobnee2 = QtWidgets.QPushButton(self.centralwidget)
        self.podrobnee2.setGeometry(QtCore.QRect(350, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.podrobnee2.setFont(font)
        self.podrobnee2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.podrobnee2.setObjectName("podrobnee2")
        self.oplata3 = QtWidgets.QPushButton(self.centralwidget)
        self.oplata3.setGeometry(QtCore.QRect(468, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.oplata3.setFont(font)
        self.oplata3.setStyleSheet("background-color: rgb(213, 214, 255);")
        self.oplata3.setObjectName("oplata3")
        self.photo3 = QtWidgets.QLabel(self.centralwidget)
        self.photo3.setGeometry(QtCore.QRect(28, 510, 211, 131))
        self.photo3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.photo3.setText("")
        self.photo3.setObjectName("photo3")
        self.opis3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.opis3.setGeometry(QtCore.QRect(268, 510, 331, 91))
        self.opis3.setObjectName("opis3")
        self.podrobnee3 = QtWidgets.QPushButton(self.centralwidget)
        self.podrobnee3.setGeometry(QtCore.QRect(350, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.podrobnee3.setFont(font)
        self.podrobnee3.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.podrobnee3.setObjectName("podrobnee3")
        self.name1 = QtWidgets.QLabel(self.centralwidget)
        self.name1.setGeometry(QtCore.QRect(30, 20, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name1.setFont(font)
        self.name1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name1.setText("")
        self.name1.setObjectName("name1")
        self.name2 = QtWidgets.QLabel(self.centralwidget)
        self.name2.setGeometry(QtCore.QRect(30, 240, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name2.setFont(font)
        self.name2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name2.setText("")
        self.name2.setObjectName("name2")
        self.name3 = QtWidgets.QLabel(self.centralwidget)
        self.name3.setGeometry(QtCore.QRect(30, 460, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name3.setFont(font)
        self.name3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name3.setText("")
        self.name3.setObjectName("name3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, -90, 751, 831))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("1653656807_23-celes-club-p-fon-raznotsvetnie-klyaksi-krasivie-24.jpg"))
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.photo1.raise_()
        self.podrobnee1.raise_()
        self.opis1.raise_()
        self.oplata1.raise_()
        self.oplata2.raise_()
        self.photo2.raise_()
        self.opis2.raise_()
        self.podrobnee2.raise_()
        self.oplata3.raise_()
        self.photo3.raise_()
        self.opis3.raise_()
        self.podrobnee3.raise_()
        self.name1.raise_()
        self.name2.raise_()
        self.name3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.podrobnee1.setText(_translate("MainWindow", "Подробнее"))
        self.oplata1.setText(_translate("MainWindow", "Оплатить"))
        self.oplata2.setText(_translate("MainWindow", "Оплатить"))
        self.podrobnee2.setText(_translate("MainWindow", "Подробнее"))
        self.oplata3.setText(_translate("MainWindow", "Оплатить"))
        self.podrobnee3.setText(_translate("MainWindow", "Подробнее"))
