input = open("input.txt", "r+")
output = open("output.txt", "w+")
str1 = input.readlines()
str1 = str1[::-1]
output.write(''.join(str1))
input.close()
output.close()
