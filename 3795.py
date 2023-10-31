# Ошибка в том, что в задании написано, что область включает границы, а на границе круга в некоторых случаях не проходит условие
# После имени функции пробел не ставится
def IsPointInArea (x, y):
    IsPointInCircle(x,y)

# Между функциями должно быть 2 пустые строки
def IsPointInCircle (x, y):
    # У тебя всего два возможных варианта - YES и NO
    # Звучит как, что должно быть 1 условие
    if ((x + 1)**2 + (y - 1)**2) <= 4:
        if (x*2 + 2 - y) <= 0:  # Зачем вот здесь скобки?
            if (y + x) >= 0:  # А вот здесь?
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if x + y <= 0:
            if (x*2 + 2 - y) >= 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")


x = float(input())
y = float(input())
IsPointInArea(x,y)
