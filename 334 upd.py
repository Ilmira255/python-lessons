a = int(input())
b = int(input())
c = int(input())
d = int(input())
# Здесь цикл делает b итераций, а может в d раз меньше
for n in range(b + 1):  # Между оператором и операндом ставится пробел: range(b + 1)
	if n % d == c:  # if n % d == c
		print(n)
	