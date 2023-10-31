print('enter your date of birth')
datebd = int(input())
print('enter your month of birth')
monthbd = int(input())
print('enter your year of birth')
yearbd = int(input())
today = 25
month = 9
year = 2023
if monthbd > month:
	print(year-yearbd-1)
elif month == month:
	if datebd > today:
		print(year-yearbd)
	if datebd == today:
		print(year-yearbd)
		print('happy birthday')
	if datebd < today:
		print(year-yearbd)
elif monthbd < month:
	print(year-yearbd)