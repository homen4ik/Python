number = int(input("Введите целое положительное число: "))
i = number
m = i % 10

while i > 10:
    if i % 10 > m:
        m = i % 10
    i = i // 10
print(m)

