# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chose_course.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_course(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(866, 934)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-180, 20, 1061, 921))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1653656807_23-celes-club-p-fon-raznotsvetnie-klyaksi-krasivie-24.jpg"))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(610, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(0, 40, 291, 21))
        self.progressBar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.910448 rgba(167, 71, 184, 255));")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(530, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(110, 90, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")
        self.label_lessons = QtWidgets.QLabel(Form)
        self.label_lessons.setGeometry(QtCore.QRect(160, 140, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_lessons.setFont(font)
        self.label_lessons.setObjectName("label_lessons")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(290, 40, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_foto1 = QtWidgets.QLabel(Form)
        self.label_foto1.setGeometry(QtCore.QRect(40, 190, 221, 141))
        self.label_foto1.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.label_foto1.setText("")
        self.label_foto1.setObjectName("label_foto1")
        self.label_name_les1 = QtWidgets.QLabel(Form)
        self.label_name_les1.setGeometry(QtCore.QRect(290, 190, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_name_les1.setFont(font)
        self.label_name_les1.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.label_name_les1.setText("")
        self.label_name_les1.setObjectName("label_name_les1")
        self.pushButton_watch_1 = QtWidgets.QPushButton(Form)
        self.pushButton_watch_1.setGeometry(QtCore.QRect(290, 270, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        self.pushButton_watch_1.setFont(font)
        self.pushButton_watch_1.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.pushButton_watch_1.setObjectName("pushButton_watch_1")
        self.pushButton_send1 = QtWidgets.QPushButton(Form)
        self.pushButton_send1.setGeometry(QtCore.QRect(530, 270, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send1.setFont(font)
        self.pushButton_send1.setStyleSheet("background-color: rgba(170, 170, 255, 160)")
        self.pushButton_send1.setObjectName("pushButton_send1")
        self.pushButton_send2 = QtWidgets.QPushButton(Form)
        self.pushButton_send2.setGeometry(QtCore.QRect(530, 460, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send2.setFont(font)
        self.pushButton_send2.setStyleSheet("background-color: rgba(170, 170, 255, 160)")
        self.pushButton_send2.setObjectName("pushButton_send2")
        self.label_name_les2 = QtWidgets.QLabel(Form)
        self.label_name_les2.setGeometry(QtCore.QRect(290, 380, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_name_les2.setFont(font)
        self.label_name_les2.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.label_name_les2.setText("")
        self.label_name_les2.setObjectName("label_name_les2")
        self.label_foto2 = QtWidgets.QLabel(Form)
        self.label_foto2.setGeometry(QtCore.QRect(40, 380, 221, 141))
        self.label_foto2.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.label_foto2.setText("")
        self.label_foto2.setObjectName("label_foto2")
        self.pushButton_watch_2 = QtWidgets.QPushButton(Form)
        self.pushButton_watch_2.setGeometry(QtCore.QRect(290, 460, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        self.pushButton_watch_2.setFont(font)
        self.pushButton_watch_2.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.pushButton_watch_2.setObjectName("pushButton_watch_2")
        self.pushButton_send3 = QtWidgets.QPushButton(Form)
        self.pushButton_send3.setGeometry(QtCore.QRect(530, 650, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send3.setFont(font)
        self.pushButton_send3.setStyleSheet("background-color: rgba(170, 170, 255, 160)")
        self.pushButton_send3.setObjectName("pushButton_send3")
        self.label_name_les3 = QtWidgets.QLabel(Form)
        self.label_name_les3.setGeometry(QtCore.QRect(290, 570, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_name_les3.setFont(font)
        self.label_name_les3.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.label_name_les3.setText("")
        self.label_name_les3.setObjectName("label_name_les3")
        self.label_foto3 = QtWidgets.QLabel(Form)
        self.label_foto3.setGeometry(QtCore.QRect(40, 570, 221, 141))
        self.label_foto3.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.label_foto3.setText("")
        self.label_foto3.setObjectName("label_foto3")
        self.pushButton_watch_3 = QtWidgets.QPushButton(Form)
        self.pushButton_watch_3.setGeometry(QtCore.QRect(290, 650, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        self.pushButton_watch_3.setFont(font)
        self.pushButton_watch_3.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.pushButton_watch_3.setObjectName("pushButton_watch_3")
        self.pushButton_send4 = QtWidgets.QPushButton(Form)
        self.pushButton_send4.setGeometry(QtCore.QRect(530, 840, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send4.setFont(font)
        self.pushButton_send4.setStyleSheet("background-color: rgba(170, 170, 255, 160)")
        self.pushButton_send4.setObjectName("pushButton_send4")
        self.label_name_les4 = QtWidgets.QLabel(Form)
        self.label_name_les4.setGeometry(QtCore.QRect(290, 760, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_name_les4.setFont(font)
        self.label_name_les4.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.label_name_les4.setText("")
        self.label_name_les4.setObjectName("label_name_les4")
        self.label_foto4 = QtWidgets.QLabel(Form)
        self.label_foto4.setGeometry(QtCore.QRect(40, 760, 221, 141))
        self.label_foto4.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.label_foto4.setText("")
        self.label_foto4.setObjectName("label_foto4")
        self.pushButton_watch_4 = QtWidgets.QPushButton(Form)
        self.pushButton_watch_4.setGeometry(QtCore.QRect(290, 840, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        self.pushButton_watch_4.setFont(font)
        self.pushButton_watch_4.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.pushButton_watch_4.setObjectName("pushButton_watch_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Form", "login:"))
        self.label_lessons.setText(_translate("Form", "Уроки"))
        self.label_5.setText(_translate("Form", "С момента покупки прошло:"))
        self.label_6.setText(_translate("Form", "времени прохождения"))
        self.pushButton_watch_1.setText(_translate("Form", "Смотреть видео"))
        self.pushButton_send1.setText(_translate("Form", "Сдать работу"))
        self.pushButton_send2.setText(_translate("Form", "Сдать работу"))
        self.pushButton_watch_2.setText(_translate("Form", "Смотреть видео"))
        self.pushButton_send3.setText(_translate("Form", "Сдать работу"))
        self.pushButton_watch_3.setText(_translate("Form", "Смотреть видео"))
        self.pushButton_send4.setText(_translate("Form", "Сдать работу"))
        self.pushButton_watch_4.setText(_translate("Form", "Смотреть видео"))