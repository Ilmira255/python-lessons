s = input()
a = s.find('h')
b = s.rfind('h')
s = s[:a] + s[b+1:len(s)]
print(s)