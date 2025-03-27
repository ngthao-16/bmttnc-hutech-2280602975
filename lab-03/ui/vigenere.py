# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 191, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.PlainText = QtWidgets.QLabel(self.centralwidget)
        self.PlainText.setGeometry(QtCore.QRect(70, 90, 47, 13))
        self.PlainText.setObjectName("PlainText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 200, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 310, 61, 16))
        self.label_3.setObjectName("label_3")
        self.txt_plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(150, 70, 371, 71))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_cipher_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(150, 300, 371, 71))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.txt_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(150, 190, 371, 51))
        self.txt_key.setObjectName("txt_key")
        self.btn_encrypt = QtWidgets.QToolButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(170, 440, 71, 19))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QToolButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(410, 440, 101, 19))
        self.btn_decrypt.setObjectName("btn_decrypt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "VIGENERE CIPHER"))
        self.PlainText.setText(_translate("MainWindow", "Plain Text:"))
        self.label_2.setText(_translate("MainWindow", "Key:"))
        self.label_3.setText(_translate("MainWindow", "CipherText:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())