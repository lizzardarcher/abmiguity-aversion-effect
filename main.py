#!/usr/bin/python

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mydesign import Ui_MainWindow
from form import Ui_Form
from experiment import Ui_Experiment
from debrief import Ui_Debrief
import random
import csv
import os.path

# data to collect
data = {"age": "",
        "gender": "",
        "level": "",
        "numBall": "",
        "urnPos": "",
        "choice": "",
        "marble": ""}  # marble 1 == red; 0 == blue


def checkAcceptance(state):
    """Method checks if agreement is accepted"""
    if state == QtCore.Qt.Checked:
        uiMain.pushButton.clicked.connect(showForm)
        uiMain.pushButton.setEnabled(True)
    else:
        uiMain.pushButton.setEnabled(False)


def showForm():
    """Method to open Form page"""
    def checkAgeInput():
        try:
            if int(uiForm.lineEdit.text()) >= 18:
                uiForm.pushButton.clicked.connect(lambda: showExperiment(""))
        except:
            pass
        age = uiForm.lineEdit.text()
        data["age"] = age
        print(age)

    global Form
    Form = QtWidgets.QWidget()
    uiForm = Ui_Form()
    uiForm.setupUi(Form)
    MainWindow.close()
    Form.show()

    gender = uiForm.comboBox_2.currentText()
    data["gender"] = gender
    print(gender)
    level = uiForm.comboBox.currentText()
    data["level"] = level
    print(level)
    uiForm.lineEdit.textChanged.connect(checkAgeInput)


def showExperiment(_str):
    """Method to open Experiment page"""

    def checkRadioBtn_1():
        """Method checks if one of two radiobuttons are clicked,
        then sets opposite radiobtn to be disabled and counts which
        marble was obtained.
        """
        ui.pushButton.clicked.connect(lambda: showDebrief(""))
        ui.radioButton_2.setEnabled(False)
        marble = 1
        if ui.selector == 1:
            data["urnPos"] = 0
            data["choice"] = 1
            ball = random.randint((ui.numOfBalls / 2), ui.numOfBalls)
            if (ui.numOfBalls / 2) > ball:
                marble = 0
            else:
                marble = 1
        else:
            data["urnPos"] = 1
            data["choice"] = 0
            if ui.numOfBalls == 100:
                ball = random.randint(1, 100)
                if ball > 53:
                    marble = 0
                else:
                    marble = 1
            elif ui.numOfBalls == 10:
                ball = random.randint(1, 10)
                if ball > 8:
                    marble = 0
                else:
                    marble = 1
            elif ui.numOfBalls == 2:
                ball = random.randint(1, 2)
                if ball > 1:
                    marble = 0
                else:
                    marble = 1
        data["marble"] = marble
        return marble

    def checkRadioBtn_2():
        """Method checks if one of two radiobuttons are clicked,
        then sets opposite radiobtn to be disabled and counts which
        marble was obtained.
        """
        ui.pushButton.clicked.connect(lambda: showDebrief(""))
        ui.radioButton.setEnabled(False)
        marble = 0
        if ui.selector == 1:
            data["urnPos"] = 0
            data["choice"] = 0
            ball = random.randint((ui.numOfBalls / 2), ui.numOfBalls)
            if (ui.numOfBalls / 2) > ball:
                marble = 0
            else:
                marble = 1
        else:
            data["urnPos"] = 1
            data["choice"] = 1
            if ui.numOfBalls == 100:
                ball = random.randint(1, 100)
                if ball > 53:
                    marble = 0
                else:
                    marble = 1
            elif ui.numOfBalls == 10:
                ball = random.randint(1, 10)
                if ball > 8:
                    marble = 0
                else:
                    marble = 1
            elif ui.numOfBalls == 2:
                ball = random.randint(1, 2)
                if ball > 1:
                    marble = 0
                else:
                    marble = 1
        data["marble"] = marble
        return marble

    global Exp
    Exp = QtWidgets.QWidget()
    ui = Ui_Experiment()
    ui.setupUi(Exp)
    Form.close()
    Exp.show()
    data["numBall"] = ui.numOfBalls
    ui.radioButton.toggled.connect(checkRadioBtn_1)
    ui.radioButton_2.toggled.connect(checkRadioBtn_2)


def showDebrief(_str):
    """Method to open Debrief page"""

    def finish():
        """Method to exit program"""
        Debrief.close()

    def returnToStart():
        """Method to get back and open Start(Agreement) page """
        MainWindow.show()
        uiMain.checkBox.setChecked(False)
        Ui_Debrief.marble = 0
        Ui_Experiment.numOfBalls = random.choice([2, 10, 100])
        Debrief.close()

    global Debrief
    Debrief = QtWidgets.QWidget()
    ui = Ui_Debrief()
    ui.setupUi(Debrief)
    Debrief.show()
    Exp.close()
    print(data)

    if data["marble"] == 1:
        ui.label.setText("Marble is RED you win")
        ui.label.setStyleSheet("background-color: red")
    else:
        ui.label.setText("Marble is blue you loose")
        ui.label.setStyleSheet("background-color: blue")

    # Write collected data to csv
    # Adds header to csv file if it wasn't exist
    if os.path.exists("results.csv"):
        with open("results.csv", "a") as file:
            fieldnames = ['age', 'gender', 'level', 'numBall', 'urnPos', 'choice', 'marble']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
    else:
        with open("results.csv", "a") as file:
            fieldnames = ['age', 'gender', 'level', 'numBall', 'urnPos', 'choice', 'marble']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)

    ui.pushButton.clicked.connect(returnToStart)
    ui.pushButton_2.clicked.connect(finish)

# Entry point
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    uiMain = Ui_MainWindow()
    uiMain.setupUi(MainWindow)
    # Checks checkbox state and if it is clicked 'confirm' button activates
    uiMain.checkBox.stateChanged.connect(checkAcceptance)
    MainWindow.show()
    sys.exit(app.exec_())
