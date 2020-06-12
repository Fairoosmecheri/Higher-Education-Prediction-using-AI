
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from DBConnection import DBConnection

class UserRegister(object):
    def userRegister(self):
        uname = self.name_lineEdit.text()
        passwd = self.passw_lineEdit.text()
        database = DBConnection.getConnection()
        cursor = database.cursor()
        database.commit()

        query = "insert into users (uname,  passwd) values (%s,%s)"
        values = (uname, passwd)
        cursor.execute(query, values)

        print("Register Successfully")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 388)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 70, 141, 20))
        self.label.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(110, 130, 71, 16))
        self.name.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.name.setObjectName("name")
        self.name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.name_lineEdit.setGeometry(QtCore.QRect(110, 150, 251, 31))
        self.name_lineEdit.setText("")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.passw = QtWidgets.QLabel(Dialog)
        self.passw.setGeometry(QtCore.QRect(110, 190, 71, 16))
        self.passw.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.passw.setObjectName("passw")
        self.passw_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.passw_lineEdit.setGeometry(QtCore.QRect(110, 210, 251, 31))
        self.passw_lineEdit.setText("")
        self.passw_lineEdit.setObjectName("passw_lineEdit")
        self.regbtn = QtWidgets.QPushButton(Dialog)
        self.regbtn.setGeometry(QtCore.QRect(190, 260, 75, 23))
        self.regbtn.setStyleSheet("background-color: rgb(85, 85, 0);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 75 12pt \"Times New Roman\";")
        self.regbtn.setObjectName("regbtn")
        self.regbtn.clicked.connect(self.userRegister)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Register"))
        self.label.setText(_translate("Dialog", "User Register"))
        self.name.setText(_translate("Dialog", "Username"))
        self.passw.setText(_translate("Dialog", "Password"))
        self.regbtn.setText(_translate("Dialog", "Register"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UserRegister()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())