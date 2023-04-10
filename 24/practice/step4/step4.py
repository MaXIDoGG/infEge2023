f = open('file.txt')
s = f.readline()

n = 0
maxn = 0

for i in range(len(s)):
    if (s[i] == 'X' and n % 3 == 0) or (s[i] == 'Y' and n % 3 == 1) or (s[i] == 'Z' and n % 3 == 2):
        n += 1
        if n > maxn:
            maxn = n
    elif s[i] == 'X':
        n = 1
    else:
        n = 0

print(maxn)
