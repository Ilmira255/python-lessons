import sys
with open('log.txt', 'w') as sys.stdout:

    def sum(x, y):
        print(x + y)

    def subtraction(x, y):
        print(x - y)

    def multiplication(x, y):
        print(x * y)

    def division(x, y):
        print(x / y)

    def exponent(x, y):
        print(x ** y)

    x = float(input('Hello! Enter 1st number '))
    print(x)
    y = float(input('Enter 2nd number '))
    print(y)
    z = int(input('Do you want to 1. sum, 2. subtract, 3. multiply, 4. divide, 5. exponentiate. Enter only number ',))
    print(z)
    if z == 1:
        sum(x, y)
    elif z == 2:
        subtraction(x, y)
    elif z == 3:
        multiplication(x, y)
    elif z == 4:
        division(x, y)
    elif z == 5:
        exponent(x, y)

