x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
# Между функциями и кодом всегда должно быть 2 пустые строки
# Функции определяются в самом верху (но после импортов)
def distance (x1, y1, x2, y2):  # Пробел после имени функции не ставится
    result = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return(result)  # return - это не функция. return result
result = distance(x1, y1, x2, y2)
print(result)
