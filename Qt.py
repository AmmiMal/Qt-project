import sys
import sqlite3
import datetime
import csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QHeaderView, QMessageBox, QLabel, \
    QFileDialog, QLineEdit, QSizePolicy
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from input import Ui_Form_in
from choice import Ui_Form_choice
from viewing import Ui_Form_view
from loginin import Ui_Form_logg
from courses import Ui_MainWindow
from detailed import Ui_Form
from Oplata import Ui_Form_oplata
from authorization import Ui_Form_logining
from chose_course import Ui_Form_course


class Input(QWidget, Ui_Form_in, Ui_MainWindow):
    def __init__(self):
        super(Input, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.pushButton_avtor.clicked.connect(self.avt)
        self.pushButton_learning.clicked.connect(self.learn)

    def avt(self):
        self.closeForm()
        self.Avt = Avtoriz()
        self.Avt.show()

    def learn(self):
        self.closeForm()
        self.Course = Courses(self)
        self.Course.show()

    def closeForm(self):
        self.close()


class Avtoriz(QWidget, Ui_Form_logg):
    def __init__(self):
        super(Avtoriz, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.lineEdit_pas.setEchoMode(QLineEdit.Password)
        self.pushButton_inp.clicked.connect(self.next)

    def next(self):
        self.log = self.lineEdit_log.text()
        self.pas = self.lineEdit_pas.text()
        if self.log == 'admin':
            self.con = sqlite3.connect("project_qt.sqlite")
            self.cur = self.con.cursor()
            res = self.cur.execute("""SELECT * FROM FinishedWorks""").fetchall()
            with open('Ready_works.csv', 'w', newline='', encoding="utf8") as f:
                writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow(['id', 'урок', 'логин', 'работа'])
                for d in res:
                    d = list(d)
                    pic = d[-1].split("/")[-1]
                    d[-1] = pic
                    writer.writerow(d)
            self.closeForm()
            self.choice = Choice()
            self.choice.show()
        else:
            self.con = sqlite3.connect("project_qt.sqlite")
            self.cur = self.con.cursor()
            self.result = self.cur.execute("""SELECT course FROM PurchasedCourses
                     WHERE login = ?""", (self.log,)).fetchall()
            self.res = self.cur.execute("""SELECT password FROM UserData
                     WHERE login = ?""", (self.log,)).fetchall()
            if self.pas == self.res[0][0]:
                self.closeForm()
                self.course = Course(self.result[0][0], self.log)
                self.course.show()
            else:
                mes1 = QMessageBox()
                mes1.setWindowTitle('')
                mes1.setText("Неверный пароль")
                mes1.setStandardButtons(QMessageBox.Cancel)
                mes1.exec_()

    def closeForm(self):
        self.close()


class Choice(QWidget, Ui_Form_choice):
    def __init__(self):
        super(Choice, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.pushButton_choice.clicked.connect(self.next)

    def next(self):
        self.n = self.spinBox_choice.text()
        self.closeForm()
        self.view = Viewing(self.n)
        self.view.show()

    def closeForm(self):
        self.close()


class Viewing(QWidget, Ui_Form_view):
    def __init__(self, mes):
        super(Viewing, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.n = mes
        self.con = sqlite3.connect("project_qt.sqlite")
        self.cur = self.con.cursor()
        self.result = self.cur.execute("""SELECT work FROM FinishedWorks
                             WHERE id = ?""", (self.n,)).fetchall()
        self.label_photo.setScaledContents(True)
        self.label_photo.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label_photo.setPixmap(QPixmap(self.result[0][0].split("/")[-1]))
        self.pushButton_close.clicked.connect(self.closeForm)

    def closeForm(self):
        self.close()


class Courses(QMainWindow, Ui_MainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Courses, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.con = sqlite3.connect("project_qt.sqlite")
        cur = self.con.cursor()
        result = cur.execute("""SELECT name FROM Courses""").fetchall()
        self.name1.setText(result[0][0])
        self.name2.setText(result[1][0])
        self.name3.setText(result[2][0])
        self.result = cur.execute("""SELECT description, photo FROM Courses""").fetchall()
        self.opis1.setReadOnly(True)
        self.opis2.setReadOnly(True)
        self.opis3.setReadOnly(True)
        self.opis1.appendPlainText(self.result[0][0])
        self.opis2.appendPlainText(self.result[1][0])
        self.opis3.appendPlainText(self.result[2][0])
        self.photo1.setScaledContents(True)
        self.photo1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.photo2.setScaledContents(True)
        self.photo2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.photo3.setScaledContents(True)
        self.photo3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.photo1.setPixmap(QPixmap(self.result[0][1]))
        self.photo2.setPixmap(QPixmap(self.result[1][1]))
        self.photo3.setPixmap(QPixmap(self.result[2][1]))
        self.podrobnee1.clicked.connect(self.res_)
        self.podrobnee2.clicked.connect(self.res_)
        self.podrobnee3.clicked.connect(self.res_)
        self.oplata1.clicked.connect(self.oplata)
        self.oplata2.clicked.connect(self.oplata)
        self.oplata3.clicked.connect(self.oplata)

    def res_(self):
        if self.sender() == self.podrobnee1:
            self.mes = '1'
        if self.sender() == self.podrobnee2:
            self.mes = '2'
        if self.sender() == self.podrobnee3:
            self.mes = '3'
        self.Detailed = Detailed(self.mes)
        self.Detailed.show()

    def oplata(self):
        if self.sender() == self.oplata1:
            self.mes = 'Watercolor'
        if self.sender() == self.oplata2:
            self.mes = 'Drawing'
        if self.sender() == self.oplata3:
            self.mes = 'Oilpainting'
        self.Oplata = Oplata(self.mes)
        self.Oplata.show()
        self.closeForm()

    def closeForm(self):
        self.close()



class Detailed(QWidget, Ui_Form):
    def __init__(self, mes):
        self.mes = mes
        super(Detailed, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.con = sqlite3.connect("project_qt.sqlite")
        cur = self.con.cursor()
        if self.mes == '1':
            self.result = cur.execute("SELECT * FROM Watercolor").fetchall()
            self.tableWidget.setColumnCount(len(self.result))
            self.tableWidget.setRowCount(len(self.result[0]) - 2)
        if self.mes == '2':
            self.result = cur.execute("SELECT * FROM Drawing").fetchall()
            self.tableWidget.setColumnCount(len(self.result))
            self.tableWidget.setRowCount(len(self.result[0]) - 2)
        if self.mes == '3':
            self.result = cur.execute("""SELECT * FROM Oilpainting""").fetchall()
            self.tableWidget.setColumnCount(len(self.result))
            self.tableWidget.setRowCount(len(self.result[0]) - 2)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.add()

    def add(self):
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem[2:]):
                if j > 0:
                    vid = QTextEdit(self)
                    vid.setFontPointSize(12)
                    vid.setText(str(val))
                    self.tableWidget.setCellWidget(j, i, vid)
                else:
                    self.tableWidget.setCellWidget(j, i, img(str(val)))
        self.con.commit()
        self.pushButton.clicked.connect(self.closeForm)

    def closeForm(self):
        self.close()
        self.Courses = Courses()
        self.Courses.show()


class img(QLabel):
    def __init__(self, im):
        super(img, self).__init__()
        self.setScaledContents(True)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        pic = QtGui.QPixmap(im)
        self.setPixmap(pic)


class Oplata(QWidget, Ui_Form_oplata):
    def __init__(self, mes):
        self.mes = mes
        super(Oplata, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.con = sqlite3.connect("project_qt.sqlite")
        cur = self.con.cursor()
        self.lineEdit_kurs.setReadOnly(True)
        self.lineEdit_stoim.setReadOnly(True)
        if self.mes == 'Watercolor':
            self.mes3 = 'Акварель'
            self.result = cur.execute("""SELECT name, cost FROM Courses
            WHERE name = (SELECT name FROM Watercolor)""").fetchall()
        if self.mes == 'Drawing':
            self.mes3 = 'Графика'
            self.result = cur.execute("""SELECT name, cost FROM Courses
            WHERE name = (SELECT name FROM Drawing)""").fetchall()
        if self.mes == 'Oilpainting':
            self.mes3 = 'Масло'
            self.result = cur.execute("""SELECT name, cost FROM Courses
            WHERE name = (SELECT name FROM Oilpainting)""").fetchall()
        self.lineEdit_kurs.setText(self.result[0][0])
        self.lineEdit_stoim.setText(str(self.result[0][1]))
        self.con.commit()
        self.oplata.clicked.connect(self.process_data)

    def get_card_number(self):
        card_num = self.lineEdit_num.text()
        card_num = ''.join(card_num.split())
        if card_num.isdigit() and len(card_num) == 16:
            return card_num
        else:
            return 404

    def double(self, x):
        res = x * 2
        if res > 9:
            res = res - 9
        return res

    def luhn_algorithm(self, card):
        odd = map(lambda x: self.double(int(x)), card[::2])
        even = map(int, card[1::2])
        return (sum(odd) + sum(even)) % 10 == 0

    def process_data(self):
        number = self.get_card_number()
        if number == 404:
            mes1 = QMessageBox()
            mes1.setWindowTitle('')
            mes1.setText("Введите только 16 цифр. Допускаются пробелы")
            mes1.setStandardButtons(QMessageBox.Cancel)
            mes1.exec_()
        elif self.luhn_algorithm(number):
            mes = QMessageBox()
            mes.setWindowTitle('')
            mes.setText("Оплата прошла успешно!")
            mes.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            mes.exec_()
            self.closeForm()
            self.Authorization = Authorization(self.mes3)
            self.Authorization.show()
            # вызов класса регистрации и занесение данных в таблицу
        else:
            mes2 = QMessageBox()
            mes2.setWindowTitle('')
            mes2.setText("Номер недействителен. Попробуйте снова.")
            mes2.setStandardButtons(QMessageBox.Cancel)
            mes2.exec_()

    def closeForm(self):
        self.close()


class Authorization(QWidget, Ui_Form_logining):
    def __init__(self, mes):
        self.mes4 = mes
        super(Authorization, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.lineEdit_pas.setEchoMode(QLineEdit.Password)
        self.con = sqlite3.connect("project_qt.sqlite")
        self.cur = self.con.cursor()
        self.next.clicked.connect(self.n)

    def n(self):
        n = self.lineEdit_name.text()
        sn = self.lineEdit_sname.text()
        log = self.lineEdit_log.text()
        pas = self.lineEdit_pas.text()
        exit = True
        if len(pas) <= 8:
            exit = False
        alf_eg = 'qwertyuioplkjhgfdsazxcvbnm'
        alf = 'йцукенгшщзхъфывапролджэячсмитьбюё'
        combs = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop', 'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk',
                 'jkl',
                 'zxc', 'xcv', 'cvb', 'vbn', 'bnm', 'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх',
                 'зхъ',
                 'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ', 'ячс', 'чсм', 'сми', 'мит', 'ить',
                 'тьб',
                 'ьбю', 'жэё']
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        big, small, num = 0, 0, 0
        for i in pas:
            if i in alf or i in alf_eg:
                small += 1
            if i in alf.upper() or i in alf_eg.upper():
                big += 1
            if i in nums:
                num += 1
        if big < 1 or small < 1:
            exit = False
        if num < 1:
            exit = False
        g = 3
        for i in range(0, len(pas)):
            if pas[i:g].lower() in combs:
                exit = False
            g += 1
        self.res = self.cur.execute("""SELECT login FROM UserData""").fetchall()
        res = []
        for elem in self.res:
            res.append(elem[0])

        if exit and log not in res:
            dt_now = datetime.date.today()
            self.cur.execute("INSERT INTO UserData VALUES(?, ?, ?, ?)", (log, pas, n, sn))
            self.cur.execute("INSERT INTO PurchasedCourses VALUES(?, ?, ?, ?, ?)", (self.mes4, log, n, sn, dt_now))
            self.con.commit()
            self.closeForm()
            self.Course = Course(self.mes4, log)
            self.Course.show()
        elif log in res:
            mes1 = QMessageBox()
            mes1.setWindowTitle('')
            mes1.setText("Логин уже занят")
            mes1.setStandardButtons(QMessageBox.Cancel)
            mes1.exec_()

    def closeForm(self):
        self.close()


class Hyperlinklabel(QLabel):
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet('font-size: 35px')
        self.setOpenExternalLinks(True)
        self.setParent(parent)


class Course(QWidget, Ui_Form_course):
    def __init__(self, mes, log):
        super(Course, self).__init__()
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        self.log = log
        self.mes = mes
        self.setupUi(self)
        self.label_name.setText(self.mes)
        self.textEdit.setText(self.log)
        self.textEdit.setReadOnly(True)
        self.progressBar.setMaximum(32)
        self.con = sqlite3.connect("project_qt.sqlite")
        self.cur = self.con.cursor()
        self.res = self.cur.execute("""SELECT date FROM PurchasedCourses WHERE login = ?""", (self.log, )).fetchall()
        if self.mes == 'Акварель':
            self.result = self.cur.execute("""SELECT lesson, photo FROM Watercolor""").fetchall()
        if self.mes == 'Графика':
            self.result = self.cur.execute("""SELECT lesson, photo FROM Drawing""").fetchall()
        if self.mes == 'Масло':
            self.result = self.cur.execute("""SELECT lesson, photo FROM Oilpainting""").fetchall()
        self.label_name_les1.setText(self.result[0][0])
        self.label_name_les2.setText(self.result[1][0])
        self.label_name_les3.setText(self.result[2][0])
        self.label_name_les4.setText(self.result[3][0])
        self.label_foto1.setScaledContents(True)
        self.label_foto1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label_foto2.setScaledContents(True)
        self.label_foto2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label_foto3.setScaledContents(True)
        self.label_foto3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label_foto4.setScaledContents(True)
        self.label_foto4.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label_foto1.setPixmap(QPixmap(self.result[0][1]))
        self.label_foto2.setPixmap(QPixmap(self.result[1][1]))
        self.label_foto3.setPixmap(QPixmap(self.result[2][1]))
        self.label_foto4.setPixmap(QPixmap(self.result[3][1]))
        self.bar()
        self.pushButton_watch_1.clicked.connect(self.res_)
        self.pushButton_watch_2.clicked.connect(self.res_)
        self.pushButton_watch_3.clicked.connect(self.res_)
        self.pushButton_watch_4.clicked.connect(self.res_)
        self.pushButton_send1.clicked.connect(self.send)
        self.pushButton_send2.clicked.connect(self.send)
        self.pushButton_send3.clicked.connect(self.send)
        self.pushButton_send4.clicked.connect(self.send)

    def bar(self):
        date_buy = self.res[0][0].split('-')
        dt_now = str(datetime.date.today()).split('-')
        d1 = int(dt_now[1]) - int(date_buy[1])
        if d1 < 0:
            d = 12 + d1
        else:
            d = d1
        if date_buy[1] != dt_now[1] and (30 - int(date_buy[-1]) + int(dt_now[-1])) <= 32 and d == 1:
            tek = 31 - int(date_buy[-1]) + int(dt_now[-1])
            self.progressBar.setValue(tek)
        elif date_buy[1] != dt_now[1] and (30 - int(date_buy[-1]) + 30 + int(dt_now[-1])) <= 32 and d == 2:
            tek = 30 - int(date_buy[-1]) + 30 + int(dt_now[-1])
            self.progressBar.setValue(tek)
        elif (int(dt_now[-1]) - int(date_buy[-1])) <= 32 and date_buy[1] == dt_now[1]:
            tek = int(dt_now[-1]) - int(date_buy[-1])
            self.progressBar.setValue(tek)
        else:
            self.closeForm()
            mes1 = QMessageBox()
            mes1.setWindowTitle('')
            mes1.setText("Время доступа к курсу истекло")
            mes1.setStandardButtons(QMessageBox.Cancel)
            mes1.exec_()
            raise SystemExit

    def res_(self):
        if self.sender() == self.pushButton_watch_1:
            self.result = '1'
        if self.sender() == self.pushButton_watch_2:
            self.mes2 = '2'
        if self.sender() == self.pushButton_watch_3:
            self.mes2 = '3'
        if self.sender() == self.pushButton_watch_4:
            self.mes2 = '4'
        self.link = Button_link(self.mes2, self.mes)
        self.link.show()

    def send(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        if self.sender() == self.pushButton_send1:
            self.mes5 = self.result[0][0]
        if self.sender() == self.pushButton_send2:
            self.mes5 = self.result[1][0]
        if self.sender() == self.pushButton_send3:
            self.mes5 = self.result[2][0]
        if self.sender() == self.pushButton_send4:
            self.mes5 = self.result[3][0]
        print(fname, type(fname))
        self.cur.execute("INSERT INTO FinishedWorks (lesson, login, work) VALUES(?, ?, ?)",
                         (self.mes5, self.log, fname))
        self.con.commit()

    def closeForm(self):
        self.close()


class Button_link(QWidget):
    def __init__(self, mes, course):
        super(Button_link, self).__init__()
        link = '<a href={0}>{1}</a>'
        if mes == '1' and course == 'Акварель':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/ZfOn19CWhbA', 'Введение. Вспоминаем основы живописи'))
        elif mes == '2' and course == 'Акварель':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/2H18HZMoA08', 'Учимся писать металл'))
        elif mes == '3' and course == 'Акварель':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/QrkXOH0Dumw', 'Как писать стекло'))
        elif mes == '4' and course == 'Акварель':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/_yex7RQwJDo', 'Итоговая: постановка с металлом и стеклом'))

        elif mes == '1' and course == 'Графика':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/wNy2qyVDXSU', 'Штрих. Построение шара и его штриховка'))
        elif mes == '2' and course == 'Графика':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/EzLvyvoLpbc', 'Перспектива'))
        elif mes == '3' and course == 'Графика':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/lLWzD2q_2no', 'Зарисовка крыльца в перспективе'))
        elif mes == '4' and course == 'Графика':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/3je3d3m76c0', 'Зарисовка деревянной скульптуры'))

        elif mes == '1' and course == 'Масло':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/V0_iJhTuwuQ', 'Введение в материалы'))
        elif mes == '2' and course == 'Масло':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/9EIXAM1o6Gg', 'Живопись мастихином'))
        elif mes == '3' and course == 'Масло':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/u8ul67p7Hbw', 'Пейзаж с горами'))
        elif mes == '4' and course == 'Масло':
            label1 = Hyperlinklabel(self)
            label1.setText(link.format('https://youtu.be/bY2jYShjcBA', 'Пейзаж. Закат на озере'))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Input()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
