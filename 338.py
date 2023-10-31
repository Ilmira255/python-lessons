a=[]  # Пробел между оператором и операндом: a = []
# Посмотри внимательно на формат ввода и вывода и помни, что тебя проверяет машина
# а машина английского языка не знает)
print('enter length of array')
n=int(input())
for i in range(n):
	a.append(int(input()))
print('The reversed array is ', a[::-1])
