
f = open("24_demo.txt")  # Открытие файла
s = f.readline()        # Чтение строки из файла

n = 1                   # Количество идущих подряд символов
maxn = 1                # Максимальное количество идущих подряд символов
for i in range(len(s)-1):  # 0 до len-1
    if s[i] != s[i+1]:  # Сравнение элементов
        n += 1
    else:
        if n > maxn:
            maxn = n    # Запись макс. количества
        n = 1

print(maxn)
