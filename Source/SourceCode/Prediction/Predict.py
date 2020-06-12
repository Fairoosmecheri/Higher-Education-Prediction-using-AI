
from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
import sys
import time
class Ui_Predict(object):
    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        print(fileName)
        self.lineEdit.setText(fileName)

    def predict(self):
        try:
            trainset = []
            fname = self.lineEdit.text()
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute(
                "select math,chinese,eng,phy,che,bio,hist,condt,sprt,art,result from dataset")
            row = cursor.fetchall()
            y_train = []
            trainset.clear()
            y_train.clear()
            for r in row:
                x_train = []
                x_train.clear()
                x_train.append(float(r[0]))
                x_train.append(float(r[1]))
                x_train.append(float(r[2]))
                x_train.append(float(r[3]))
                x_train.append(float(r[4]))
                x_train.append(float(r[5]))
                x_train.append(float(r[6]))
                x_train.append(float(r[7]))
                x_train.append(float(r[8]))
                x_train.append(float(r[9]))
                y_train.append(r[10])
                trainset.append(x_train)
            print("y=", y_train)
            print("trd=", trainset)
            trainset = np.array(trainset)
            print("trd=", trainset)

            # Train the model
            y_train = np.array(y_train)


            tf = pd.read_csv(fname)
            testdata = np.array(tf)
            print("td=", testdata)
            testdata = testdata.reshape(len(testdata), -1)



            cnn = MLPClassifier()
            cnn.fit(trainset, y_train)
            #s = time.clock()
            reslt = cnn.predict(testdata)
            #e = time.clock()
            #t = round(e - s, 5)
            #print("Time:", t, "seconds")
            print("pre=", reslt)

            self.result.setText(reslt[0])

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(652, 501)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 80, 331, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 165, 141, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 200, 381, 41))
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Verdana\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 280, 181, 41))
        self.pushButton.setStyleSheet("background-color: rgb(170, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Verdana\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predict)

        self.browseBtn = QtWidgets.QPushButton(Dialog)
        self.browseBtn.setGeometry(QtCore.QRect(480, 202, 151, 41))
        self.browseBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 75 16pt \"Times New Roman\";\n")
        self.browseBtn.setObjectName("browseBtn")
        self.browseBtn.clicked.connect(self.browse_file)
        

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 390, 141, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.label_3.setObjectName("label_3")
        self.result = QtWidgets.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(230, 380, 351, 51))
        self.result.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.result.setText("")
        self.result.setObjectName("result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prediction"))
        self.label.setText(_translate("Dialog", "Prediction Universities Degree"))
        self.label_2.setText(_translate("Dialog", "Select Testing File"))
        self.pushButton.setText(_translate("Dialog", "Predict"))
        self.browseBtn.setText(_translate("Dialog", "Browse"))
        self.label_3.setText(_translate("Dialog", "Result       :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Predict()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

