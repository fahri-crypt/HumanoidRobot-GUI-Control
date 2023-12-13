# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'humanoidrobot.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 674)
        font = QtGui.QFont()
        font.setFamily("Monotxt")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(99, 198, 200);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(140, 240, 311, 291))
        font = QtGui.QFont()
        font.setFamily("Monotxt")
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.byeButton = QtWidgets.QPushButton(self.frame_2)
        self.byeButton.setGeometry(QtCore.QRect(40, 10, 91, 91))
        self.byeButton.setStyleSheet("background-color: rgb(0, 0, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("wave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("wave.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.byeButton.setIcon(icon)
        self.byeButton.setIconSize(QtCore.QSize(75, 75))
        self.byeButton.setObjectName("byeButton")
        self.slebewButton = QtWidgets.QPushButton(self.frame_2)
        self.slebewButton.setGeometry(QtCore.QRect(170, 10, 91, 91))
        self.slebewButton.setStyleSheet("background-color: rgb(0, 255, 106);")
        self.slebewButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("haluan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.slebewButton.setIcon(icon1)
        self.slebewButton.setIconSize(QtCore.QSize(75, 75))
        self.slebewButton.setObjectName("slebewButton")
        self.punchKiriButton = QtWidgets.QPushButton(self.frame_2)
        self.punchKiriButton.setGeometry(QtCore.QRect(40, 116, 91, 91))
        self.punchKiriButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.punchKiriButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("punch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("punch.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.punchKiriButton.setIcon(icon2)
        self.punchKiriButton.setIconSize(QtCore.QSize(75, 75))
        self.punchKiriButton.setObjectName("punchKiriButton")
        self.punchKananButton = QtWidgets.QPushButton(self.frame_2)
        self.punchKananButton.setGeometry(QtCore.QRect(170, 117, 91, 91))
        self.punchKananButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.punchKananButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("punchKanan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.punchKananButton.setIcon(icon3)
        self.punchKananButton.setIconSize(QtCore.QSize(75, 75))
        self.punchKananButton.setObjectName("punchKananButton")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(40, 213, 90, 41))
        font = QtGui.QFont()
        font.setFamily("Monotxt_IV50")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(160, 213, 110, 41))
        font = QtGui.QFont()
        font.setFamily("Monotxt_IV50")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 3, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(168, 153, 240, 51))
        font = QtGui.QFont()
        font.setFamily("Monotxt_IV50")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-50, 650, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Monotxt_IV50")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 227, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Monotxt_IV50")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 227, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Monotxt_IV50")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Gambar1 = QtWidgets.QLabel(self.centralwidget)
        self.Gambar1.setGeometry(QtCore.QRect(640, 79, 460, 531))
        self.Gambar1.setText("")
        self.Gambar1.setPixmap(QtGui.QPixmap("humanoid.png"))
        self.Gambar1.setScaledContents(True)
        self.Gambar1.setObjectName("Gambar1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 81, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("robot (2).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 590, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Monotxt_IV50")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.frame_2.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.Gambar1.raise_()
        self.label_3.raise_()
        self.label_11.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.byeButton.clicked.connect(self.show_bye)
        self.slebewButton.clicked.connect(self.show_slebew)
        self.punchKiriButton.clicked.connect(self.show_pukulkiri)
        self.punchKananButton.clicked.connect(self.show_pukulkanan)

    def show_humanoid(self):
        self.Gambar1.setPixmap(QtGui.QPixmap("humanoid.png"))

    def show_bye(self):
        self.Gambar1.setPixmap(QtGui.QPixmap("dada-dada.png"))

    def show_slebew(self):
        self.Gambar1.setPixmap(QtGui.QPixmap("slebew.png"))

    def show_pukulkiri(self):
        self.Gambar1.setPixmap(QtGui.QPixmap("pukul kiri.png"))

    def show_pukulkanan(self):
        self.Gambar1.setPixmap(QtGui.QPixmap("pukul kanan.png"))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.byeButton.setText(_translate("MainWindow", " "))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:696;\">PUNCH<br/>LEFT</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:696;\">PUNCH<br/>RIGHT</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">HUMANOID ROBOT</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">GRAPHICAL USER INTERFACE</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">CONTROL<br/>HUMANOID ROBOT</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">YOU MOVE <br/>WE CTRL</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:696;\">SLEBEW</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">BYE</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">YOU MOVE<br/>WE CONTROL</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())