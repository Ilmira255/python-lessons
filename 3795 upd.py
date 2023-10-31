def IsPointInArea(x, y):
    IsPointInCircle(x,y)

# Между функциями должно быть 2 пустые строки
def IsPointInCircle(x, y):
   
    if ((x + 1)**2 + (y - 1)**2) < 4: 
        if x*2 + 2 - y <= 0: 
            if y + x >= 0: 
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    elif ((x + 1)**2 + (y - 1)**2) == 4:
        if x + y <= 0:
            if (x*2 + 2 - y) >= 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    elif ((x + 1)**2 + (y - 1)**2) > 4:
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
