import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from src.calculator_gui import Ui_MainWindow
from src.operaciones import Calculator


class CalculatorMain(QMainWindow):
    firstNum = None
    userIsTypingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.opr = Calculator()
        self.ui.setupUi(self)

        # Number Buttons
        self.ui.bnt_zero.clicked.connect(self.pushButton)
        self.ui.bnt_1.clicked.connect(self.pushButton)
        self.ui.bnt_2.clicked.connect(self.pushButton)
        self.ui.bnt_3.clicked.connect(self.pushButton)
        self.ui.bnt_4.clicked.connect(self.pushButton)
        self.ui.bnt_5.clicked.connect(self.pushButton)
        self.ui.bnt_6.clicked.connect(self.pushButton)
        self.ui.bnt_7.clicked.connect(self.pushButton)
        self.ui.bnt_8.clicked.connect(self.pushButton)
        self.ui.bnt_9.clicked.connect(self.pushButton)

        # Operation Buttons
        self.ui.bnt_sum.clicked.connect(self.operation)
        self.ui.bnt_substract.clicked.connect(self.operation)
        self.ui.bnt_division.clicked.connect(self.operation)
        self.ui.bnt_multiplication.clicked.connect(self.operation)

        # Equal button
        self.ui.bnt_equal.clicked.connect(self.equalResult)

        # Clear display
        self.ui.bnt_AC.clicked.connect(self.clearDisplay)

        # Information
        self.ui.bnt_Info.clicked.connect(self.information)

        # change state
        self.ui.bnt_sum.setCheckable(True)
        self.ui.bnt_substract.setCheckable(True)
        self.ui.bnt_division.setCheckable(True)
        self.ui.bnt_multiplication.setCheckable(True)

    def clearDisplay(self):
        self.ui.bnt_sum.setChecked(False)
        self.ui.bnt_substract.setChecked(False)
        self.ui.bnt_division.setChecked(False)
        self.ui.bnt_multiplication.setChecked(False)
        self.userIsTypingSecondNumber = False
        self.ui.estiLineOperacion.setText("0")

    def information(self):
        self.ui.estiLineOperacion.setText("Hello, It's a basic calculator")

    def pushButton(self):
        button = self.sender()
        if ((
                self.ui.bnt_sum.isChecked() or self.ui.bnt_substract.isChecked() or self.ui.bnt_division.isChecked() or
                self.ui.bnt_multiplication.isChecked()) and (not self.userIsTypingSecondNumber)):
            newLabel = format(float(button.text()), '.15g')
            self.userIsTypingSecondNumber = True
        else:

            newLabel = format(float(self.ui.estiLineOperacion.text() + button.text()), '.15g')

        self.ui.estiLineOperacion.setText(newLabel)

    def operation(self):
        button = self.sender()
        self.firstNum = float(self.ui.estiLineOperacion.text())
        button.setChecked(True)

    # check status of operation buttons
    def equalResult(self):
        # Add
        if self.ui.bnt_sum.isChecked():
            firstNum = self.firstNum
            secondNum = float(self.ui.estiLineOperacion.text())
            newLabel = format(self.opr.addResult(firstNum, secondNum), '.15g')
            self.ui.estiLineOperacion.setText(newLabel)

        # Subtraction
        elif self.ui.bnt_substract.isChecked():
            firstNum = self.firstNum
            secondNum = float(self.ui.estiLineOperacion.text())
            self.opr.addResult(firstNum, secondNum)
            newLabel = format(self.opr.subtractResutl(firstNum, secondNum), '.15g')
            self.ui.estiLineOperacion.setText(newLabel)

        # Divide
        elif self.ui.bnt_division.isChecked():
            firstNum = self.firstNum
            secondNum = float(self.ui.estiLineOperacion.text())
            if secondNum == float(0):
                self.ui.estiLineOperacion.setText('Can not divide a number 0')
            else:
                newLabel = format(self.opr.divideResult(firstNum, secondNum), '.15g')
                self.ui.estiLineOperacion.setText(newLabel)

        # Multiplication
        elif self.ui.bnt_multiplication.isChecked():
            firstNum = self.firstNum
            secondNum = float(self.ui.estiLineOperacion.text())
            newLabel = format(self.opr.multiplicationResult(firstNum, secondNum), '.15g')
            self.ui.estiLineOperacion.setText(newLabel)

        self.userIsTypingSecondNumber = False


# Main GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorMain()
    window.show()
    sys.exit(app.exec_())
