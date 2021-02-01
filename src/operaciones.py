class Calculator:

    # Suma operation
    def addResult(self, num1, num2):
        labelNumber = num1 + num2
        return labelNumber

    # Subtract operation
    def subtractResutl(self, num1, num2):
        labelNumber = num1 - num2
        return labelNumber

    # Multiplication operation
    def multiplicationResult(self, num1, num2):
        labelNumber = num1 * num2
        return labelNumber

    # Divide operation
    def divideResult(self, num1, num2):
        if num2 == float(0):
            raise ValueError('Can not divide a number 0')
        else:
            labelNumber = num1 / num2
            return labelNumber
