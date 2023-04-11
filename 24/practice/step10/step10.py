file = open("file.txt")
s = file.readline()

d = {}

for i in range(len(s)-1):
    if s[i] == 'A':
        if s[i+1] in d:
            d[s[i+1]] += 1
        else:
            d[s[i+1]] = 1


print(max(d, key=d.get))
