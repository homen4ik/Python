vyruchka = int(input('Введите размер выручки: '))
izdershki = int(input('Введите размер издержек: '))
x = vyruchka
y = izdershki

if x < y:
    print("У вас убытки")

else:
    print("У вас прибыль")

    rent = (x - y) / x * 100
    print(rent)
    staff = int(input("Введите число сотрудников: "))
    i = rent / staff
    print(i)
    print("Прибыль фирмы в расчете на одного сотрудника:", i )
