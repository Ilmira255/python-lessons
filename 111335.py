input = open("input.txt", "r+")
output = open("output.txt", "w+")
lines = 0
words = 0
symbols = 0

for line in input:
    lines += 1
    words += len(line.split())
    symbols += len(line)

output.write("Input file contains:")
output.write(str(symbols))
output.write(str(words))
output.write(str(lines))

input.close()
output.close()
