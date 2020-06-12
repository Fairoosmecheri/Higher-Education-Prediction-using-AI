
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import xlrd
from Predict import Ui_Predict
from DBConnection import DBConnection
from UserRegister import UserRegister


class UserLogin(object):
    def userLogin(self):

        uname = self.lineEdit.text()
        passwd = self.lineEdit_1.text()
        database = DBConnection.getConnection()
        cursor = database.cursor()
        database.commit()
        query = "select * from user where uname = %s and password = %s"
        values = (uname,passwd)
        cursor.execute(query,values)
        row = cursor.fetchall()
        if row:
            print("Login success")
            self.user = QtWidgets.QDialog()
            self.ui = Ui_Predict()
            self.ui.setupUi(self.user)
            self.user.show()
    def userRegister(self):
        print("Reg")
        self.userreg = QtWidgets.QDialog()
        self.ui = UserRegister()
        self.ui.setupUi(self.userreg)
        self.userreg.show()


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
        self.pushButton_2.clicked.connect(self.userLogin)
        self.register = QtWidgets.QPushButton(Dialog)
        self.register.setGeometry(QtCore.QRect(190, 290, 75, 23))
        self.register.setStyleSheet("background-color: rgb(85, 85, 0);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "font: 75 12pt \"Times New Roman\";")
        self.register.setObjectName("register")
        self.register.clicked.connect(self.userRegister)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Login"))
        self.label.setText(_translate("Dialog", "User Login"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton_2.setText(_translate("Dialog", "Login"))
        self.register.setText(_translate("Dialog", "Register"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UserLogin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

