f = open("file.txt")

lines = 0

for line in f:
    a = 0  # счетчик букв A
    e = 0  # счетчик букв E
    for i in range(len(line)):
        if line[i] == 'A':
            a += 1
        elif line[i] == 'E':
            e += 1
    if e > a:
        lines += 1

print(lines)
