
from PyQt5 import QtCore, QtGui, QtWidgets

from AdminLogin import AdminLogin
from Predict import Ui_Predict
from AdminHome import AdminHome
from UserLogin import UserLogin


class Ui_Dialog(object):

    def adminlogin(self):
        self.admin = QtWidgets.QDialog()
        self.ui = AdminLogin()
        self.ui.setupUi(self.admin)
        self.admin.show()
    def userhome(self):
        self.user = QtWidgets.QDialog()
        self.ui = UserLogin()
        self.ui.setupUi(self.user)
        self.user.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(621, 513)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-4, 0, 731, 551))
        self.label.setStyleSheet("background-image: url(../Prediction/images/arch.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 240, 191, 51))
        #self.pushButton.setStyleSheet("backdround-color: rgb(255, 255, 255);\n"
#"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
#"font: 75 16pt \"Times New Roman\";")
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 75 16pt \"Times New Roman\";\n")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.adminlogin)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 350, 191, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Times New Roman\";\n")
#"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.userhome)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", " Higher Education Prediction Using Deep Learning "))
        self.pushButton.setText(_translate("Dialog", "Admin"))
        self.pushButton_2.setText(_translate("Dialog", "User"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
