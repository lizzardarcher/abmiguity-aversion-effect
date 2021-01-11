# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Form")
        MainWindow.setFixedSize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 290, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 330, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 581, 251))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Experiment"))
        MainWindow.setStyleSheet("background-color: #4E75CF")
        self.checkBox.setText(_translate("MainWindow", "Accept"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))
        self.pushButton.setStyleSheet("background-color: #6997D3")
        self.textBrowser.setStyleSheet("background-color: #8C9FC9")
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:1px; margin-bottom:0px; margin-left:1px; margin-right:1px; -qt-block-indent:0; text-indent:0px;\">"
                                                          "<span style=\" font-family:\'Open Sans\',\'Arial\',\'sans-serif\'; font-size:10pt; font-style:italic; color:#000000; background-color:#8C9FC9;\">"
                                                          "    Welcome! You are asked to pass the simple test. There is two urns with red and blue marbles."
                                                          "Number of marbles in each urn is equal and even.  One urn contains marbles in certain ratio 50/50 and the other urn"
                                                          "contains marbles in an unknown ratio. In this test you will need to choose only one "
                                                          "urn(urn A or urn B) and try to get the RED marble out of urn. If you reach red marlbe you win, blue - loose."
                                                          "Remember that you have only one choice attempt. Before the test starts you need to give us your voluntary agreement "
                                                          "for the processing of personal data such as your: age, gender, level of education. Good luck"
                                                          "</span></p></body></html>"))

