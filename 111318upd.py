# Кажется, в задаче просят написать программу, которая будет принимать две строки
# И строки могут быть любые, а не жёстко зашитые в программе
# Тут стандартная ошибка хардкод (почитай в инете)

b = input()
a = input()
if (b in a) == True:
    print ("YES")
elif (b in a) == False:
    print ("NO")