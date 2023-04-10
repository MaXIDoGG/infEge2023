f = open('file.txt')
s = f.readline()

n = 0
maxn = 0

for i in range(len(s)):
    if (s[i] == 'A' and n % 2 == 0) or (s[i] == 'B' and n % 2 == 1):
        n += 1
        if n > maxn:
            maxn = n
    elif s[i] == 'A':
        n = 1
    else:
        n = 0

print(maxn)
