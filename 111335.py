import re

input = open("input.txt", "r+")
output = open("output.txt", "w+")
lines = 0
words = 0
letters = 0

for line in input:
    lines += 1
    words += len(re.findall(r'\w+', line))
    letters += len(re.findall('[A-Za-z]', line))

letter1 = str(letters) + " letters" + "\n"
words1 = str(words) + " words" + "\n"
lines1 = str(lines) + " lines"

output.writelines("Input file contains:\n")
output.writelines(letter1)
output.writelines(words1)
output.writelines(lines1)

input.close()
output.close()
