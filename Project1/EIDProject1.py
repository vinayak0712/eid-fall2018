# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abcd.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
# @author: Vinayak
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from datetime import datetime
import Adafruit_DHT
import sys
import csv
import time


#secure login window
class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'admin' and
            self.textPass.text() == 'password'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 360)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 254, 149))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_usr = QtWidgets.QLabel(self.groupBox)
        self.label_usr.setObjectName("label_usr")
        self.horizontalLayout.addWidget(self.label_usr)

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_updatetime = QtWidgets.QLabel(self.centralwidget)
        self.label_updatetime.setGeometry(QtCore.QRect(356, 220, 131, 21))
        self.label_updatetime.setText("")
        self.label_updatetime.setObjectName("label_updatetime")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(350, 180, 61, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcd_h = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_h.setGeometry(QtCore.QRect(430, 180, 61, 23))
        self.lcd_h.setObjectName("lcd_h")
        self._img_temp = QtWidgets.QLabel(self.centralwidget)
        self._img_temp.setGeometry(QtCore.QRect(330, 100, 81, 71))
        self._img_temp.setText("")
        self._img_temp.setPixmap(QtGui.QPixmap("Downloads/3.jpg"))
        self._img_temp.setObjectName("_img_temp")
        self.label_img_h = QtWidgets.QLabel(self.centralwidget)
        self.label_img_h.setGeometry(QtCore.QRect(430, 100, 71, 71))
        self.label_img_h.setText("")
        self.label_img_h.setPixmap(QtGui.QPixmap("Downloads/4.png"))
        self.label_img_h.setObjectName("label_img_h")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 180, 119, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_temp = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_temp.setObjectName("radioButton_temp")
        self.verticalLayout_2.addWidget(self.radioButton_temp)
        self.radioButton_h = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_h.setObjectName("radioButton_h")
        self.verticalLayout_2.addWidget(self.radioButton_h)
        self.label_connection = QtWidgets.QLabel(self.centralwidget)
        self.label_connection.setGeometry(QtCore.QRect(100, 220, 101, 21))
        self.label_connection.setText("")
        self.label_connection.setObjectName("label_connection")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.radioButton_temp.toggled.connect(self.readtemp_clicked)
        self.radioButton_h.toggled.connect(self.readh_clicked)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_temp.setText(_translate("MainWindow", "Temperature %C"))
        self.radioButton_h.setText(_translate("MainWindow", "Humidity "))



        

       
        #read temperature data and display in LCD
    def readtemp_clicked(self,enabled):
        humidity,temperature = Adafruit_DHT.read(22,4)

        if enabled:
            if temperature==None:
                self.label_connection.setText('Not Connected')
                self.lcdNumber.display("Err")
            else:
                self.label_connection.setText('Connected')
                self.lcdNumber.display(temperature)
                time=datetime.now().strftime('%b-%d-%Y %H:%M:%S')
                self.label_updatetime.setText(time)
                self.lcdNumber.repaint()
        #read humidity data and display in LCD
    def readh_clicked(self,enabled):
        humidity,temperature = Adafruit_DHT.read(22,4)
        if enabled:
            if humidity==None:
                self.label_connection.setText('Not Connected')
                self.lcd_h.display("Err")
            else:
                self.label_connection.setText('Connected')
                self.lcd_h.display(humidity)
                #datetime which shows the time and date
                time=datetime.now().strftime('%b-%d-%Y %H:%M:%S')
                self.label_updatetime.setText(time)

# Main Function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:

        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

