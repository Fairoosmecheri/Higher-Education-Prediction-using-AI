
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import xlrd
from AdminHome import AdminHome

class AdminLogin(object):
    def adminLogin(self):

        uname = self.lineEdit.text()
        passwd = self.lineEdit_1.text()
        if ((uname == "admin") and (passwd == "admin")):
            self.admin = QtWidgets.QDialog()
            self.ui = AdminHome()
            self.ui.setupUi(self.admin)
            self.admin.show()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 388)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 70, 141, 20))
        self.label.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 71, 16))
        self.label_2.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 150, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 190, 71, 16))
        self.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_1.setGeometry(QtCore.QRect(110, 210, 251, 31))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 260, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Login"))
        self.label.setText(_translate("Dialog", "Admin Login"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton_2.setText(_translate("Dialog", "Login"))
        self.pushButton_2.clicked.connect(self.adminLogin)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AdminLogin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

