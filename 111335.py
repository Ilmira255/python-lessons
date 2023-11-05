input = open("input.txt", "r+")
output = open("output.txt", "w+")
lines = 0
words = 0
symbols = 0

for line in input:
    lines += 1
    words += len(line.split())
    symbols += len(line.replace(" ", "").strip('\n'))

print("Input file contains:")
print(symbols, "letters")
print(words, "words")
print(lines, "lines")

# output.writelines("Input file contains:")
# output.writelines(symbols, "letters")
# output.writelines(words, "words")
# output.writelines(lines, "lines")

input.close()
output.close()
