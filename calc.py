# А где же деление по модулю?
# После имени функции пробел не ставится
def sum (x, y):
    # После имени функции пробел не ставится
    print (x + y)

# Между функциями должно быть 2 пустые строки
def subtraction (x, y):
    print(x - y)

def multiplication (x, y):
    print(x * y)

def division (x, y):
    print(x / y)

def exponent (x, y):
    print (x ** y)

x = float(input('Hello! Enter 1st number ',))  # Для чего здесь запятая?
y = float(input('Enter 2nd number ',))
z = int(input('Do you want to 1. sum, 2. subtract, 3. multiply, 4. divide, 5. exponentiate. Enter only number ',))
if z == 1:
    sum (x, y)
# Здесь напрашивается elif, так как z не может быть равно и 1, и 2
if z == 2:
    subtraction(x, y)
if z == 3:
    multiplication(x, y)
if z == 4:
    division(x, y)
if z == 5:
    exponent(x, y)
