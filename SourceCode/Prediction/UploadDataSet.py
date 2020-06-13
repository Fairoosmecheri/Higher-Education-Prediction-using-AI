
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import xlrd
from DBConnection import DBConnection
class UploadDataSet(object):
    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        print(fileName)
        self.fileName.setText(fileName)

    def showMessageBox(self, title, message):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle(title)
            msgBox.setText(message)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()
    def saveToDB(self):
        try:
            fname=self.fileName.text()
            if (fname == ""):
                self.showMessageBox("Information", "Dataset is not selected.")
            else :
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
                self.fileName.setText("")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 496)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 650, 496))
        # self.label.setStyleSheet("background-image: url(../Prediction/images/adminhomeBackground.jpg);")
        self.label.setStyleSheet(
            "border-image: url(../Prediction/images/adminhomeBackground.jpg) 0 0 0 0 stretch stretch;")
        self.label.setText("")
        self.label.setObjectName("label")

        self.titleLabel = QtWidgets.QLabel(Dialog)
        self.titleLabel.setGeometry(QtCore.QRect(174, 70, 790, 81))
        self.titleLabel.setStyleSheet("color: rgb(255, 255, 255); font: 40pt \"Franklin Gothic Heavy\";")
        self.titleLabel.setObjectName("titleLabel")

        self.selectFileLabel = QtWidgets.QLabel(Dialog)
        self.selectFileLabel.setGeometry(QtCore.QRect(110, 170, 100,16))
        self.selectFileLabel.setStyleSheet("font: 16pt \"Franklin Gothic Heavy\"; color:#ffffff;")
        self.selectFileLabel.setObjectName("selectFileLabel")

        self.fileName = QtWidgets.QLineEdit(Dialog)
        self.fileName.setGeometry(QtCore.QRect(110, 200, 251, 41))
        self.fileName.setText("")
        self.fileName.setObjectName("fileName")

        self.browseBtn = QtWidgets.QPushButton(Dialog)
        self.browseBtn.setGeometry(QtCore.QRect(380, 200, 151, 41))
        self.browseBtn.setStyleSheet("background-color: rgb(255, 255, 255); font: 16pt \"Times New Roman\";")
        self.browseBtn.setObjectName("browseBtn")
        self.browseBtn.clicked.connect(self.browse_file)

        self.storeBtn = QtWidgets.QPushButton(Dialog)
        self.storeBtn.setGeometry(QtCore.QRect(250, 280, 151, 41))
        self.storeBtn.setStyleSheet("background-color: rgb(255, 255, 255); font: 16pt \"Times New Roman\";")
        self.storeBtn.setObjectName("browseBtn")
        self.storeBtn.clicked.connect(self.saveToDB)





        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Upload DataSet"))
        self.titleLabel.setText(_translate("Dialog", "Upload  DataSet"))
        self.selectFileLabel.setText(_translate("Dialog", "Select File"))
        self.browseBtn.setText(_translate("Dialog", "Browse"))
        self.storeBtn.setText(_translate("Dialog", "Store"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui =UploadDataSet()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

