f = open('file.txt')
s = f.readline()
n = 0
maxn = 0
for i in range(len(s)):
    if s[i] == 'X':
        n += 1
    else:
        if n > maxn:
            maxn = n
        n = 0
print(maxn)
