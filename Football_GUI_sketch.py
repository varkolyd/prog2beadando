class Fmeccs:

    def __init__(self, id, hazai, dontetlen, vendeg, hszorzo, dszorzo, vszorzo):
        self.id=id
        self.hazai=hazai
        self.dontetlen=dontetlen
        self.vendeg=vendeg
        self.hszorzo=hszorzo
        self.dszorzo=dszorzo
        self.vszorzo=vszorzo

    def get_match(self):
        return f"{self.id()},{self.hazai()},{self.dontetlen()},{self.vendeg()},{self.hszorzo(),self.dszorzo, self.vszorzo}"
    def __str__(self):
        return f"{self.id()},{self.hazai()},{self.dontetlen()},{self.vendeg()},{self.hszorzo(),self.dszorzo, self.vszorzo}"

    def __lt__(self, other):
        return self.id<other.id

    def __le__(self, other):
        return self.id<= other.id

    def __ge__(self, other):
        return self.id>= other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

############################################################################
############################################################################
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
class Ui_MainWindow(object):
    ######
    meccshalmaz={}
    kreditszam=1000
    ######
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1161, 814)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(490, 10, 161, 61))
        font = QFont()
        font.setFamily(u"Copperplate Gothic Bold")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.home = QPushButton(self.centralwidget)
        self.home.setObjectName(u"home")
        self.home.setEnabled(True)
        self.home.setGeometry(QRect(190, 450, 221, 41))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        self.home.setFont(font1)
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black\n"
"\n"
"\n"
"")
        self.home.setAutoDefault(False)
        self.home.setFlat(False)
        self.away = QPushButton(self.centralwidget)
        self.away.setObjectName(u"away")
        self.away.setGeometry(QRect(730, 450, 211, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.away.setFont(font2)
        self.away.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black\n"
"\n"
"")
        self.matchlist = QListWidget(self.centralwidget)
        self.matchlist.setObjectName(u"matchlist")
        self.matchlist.setGeometry(QRect(190, 520, 751, 192))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.matchlist.setFont(font3)
        self.matchlist.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
"color: rgb(170, 0, 0);\n"
"color:white;\n"
"border-color:black")
        self.tie = QPushButton(self.centralwidget)
        self.tie.setObjectName(u"tie")
        self.tie.setGeometry(QRect(470, 450, 211, 41))
        self.tie.setFont(font2)
        self.tie.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black\n"
"\n"
"")
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1231, 771))
        self.background.setPixmap(QPixmap("ball.jpg"))
        self.background.setScaledContents(False)
        self.feltoltes = QPushButton(self.centralwidget)
        self.feltoltes.setObjectName(u"feltoltes")
        self.feltoltes.setGeometry(QRect(190, 720, 191, 41))
        self.feltoltes.setFlat(True)
        self.matchupload = QPushButton(self.centralwidget)
        self.matchupload.setObjectName(u"matchupload")
        self.matchupload.setGeometry(QRect(190, 720, 171, 28))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setItalic(False)
        font4.setKerning(False)
        self.matchupload.setFont(font4)
        self.matchupload.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black")
        self.results = QPushButton(self.centralwidget)
        self.results.setObjectName(u"results")
        self.results.setGeometry(QRect(740, 720, 201, 28))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(50)
        font5.setStrikeOut(False)
        font5.setKerning(False)
        self.results.setFont(font5)
        self.results.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 201, 41))
        font6 = QFont()
        font6.setPointSize(10)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.483684, y1:0, x2:0.516, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
        self.title.raise_()
        self.home.raise_()
        self.away.raise_()
        self.matchlist.raise_()
        self.tie.raise_()
        self.feltoltes.raise_()
        self.matchupload.raise_()
        self.results.raise_()
        self.label.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1161, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.home.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)

        ##########################
        ### INNEN JÖHET A KÓD ####
        ##########################

        self.matchupload.clicked.connect(self.load_matches)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"IK-BETS", None))
        self.home.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.away.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.tie.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.background.setText("")
        self.feltoltes.setText("")
        self.matchupload.setText(QCoreApplication.translate("MainWindow", u"Meccsek bet\u00f6lt\u00e9se", None))
        self.results.setText(QCoreApplication.translate("MainWindow", u"Eredm\u00e9nyek bet\u00f6lt\u00e9se", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kreditek:", None))

    #fájlból betöltés függvény
    def load_matches(self,):
            f = open("meccsek.txt","r", encoding="utf8")
            for line in f:
                data = line.rstrip().split(";")
                m1=Fmeccs(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
                if m1.id not in self.meccshalmaz:
                    self.matchlist.addItem(m1.id+" - "+m1.hazai+" VS "+m1.vendeg+" |  H:"+m1.hszorzo+" D:"+m1.dszorzo+" V:"+m1.vszorzo)
                    self.meccshalmaz[m1.id]=m1

    def kreditek(self):
        self.label.setText(f"Kreditek: {self.kreditszam}")

import sys
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.kreditek()    ### Felhasználható krediteket rendel a profilhoz
MainWindow.show()
sys.exit(app.exec_())