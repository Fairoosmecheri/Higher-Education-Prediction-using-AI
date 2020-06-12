
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import xlrd
from DBConnection import DBConnection
class UploadDataSet(object):
    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        print(fileName)
        self.lineEdit.setText(fileName)

    def showMessageBox(self, title, message):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle(title)
            msgBox.setText(message)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()
    def saveToDB(self):
        try:
            fname=self.lineEdit.text()
            book = xlrd.open_workbook(fname)
            sheet = book.sheet_by_index(0)
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("delete from dataset")
            database.commit()
            query = "insert into dataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            for r in range(1, sheet.nrows):
                math = sheet.cell(r, 0).value
                chin = sheet.cell(r, 1).value
                eng= sheet.cell(r, 2).value
                phy = sheet.cell(r, 3).value
                che = sheet.cell(r, 4).value
                bio= sheet.cell(r, 5).value
                hist = sheet.cell(r, 6).value
                condt = sheet.cell(r, 7).value
                sprt = sheet.cell(r, 8).value
                art = sheet.cell(r, 9).value
                sts = sheet.cell(r, 10).value
                print(math,chin,eng,phy,che,bio,condt,sprt,art,sts)
                values = (int(math),int(chin),int(eng),int(phy),int(che),int(bio),int(hist),int(condt),int(sprt),int(art),str(sts))
                cursor.execute(query, values)
                database.commit()
                columns = str(sheet.ncols)
                # rows=str(sheet.nrows)
                print("inserted")
            self.showMessageBox("Information", "DataSet Loaded Successfully")
            self.lineEdit.setText("")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
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
        self.lineEdit.setGeometry(QtCore.QRect(110, 160, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 160, 75, 31))
        self.pushButton.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 210, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Upload DataSet"))
        self.label.setText(_translate("Dialog", "Upload  DataSet"))
        self.label_2.setText(_translate("Dialog", "Select File"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Store"))
        self.pushButton_2.clicked.connect(self.saveToDB)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui =UploadDataSet()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

