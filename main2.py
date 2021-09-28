time = int(input('Введите количество секунд: '))
hours = time // 3600
minutes = time // 60
while minutes >= 60:
    minutes = minutes - 60
sec = time % 3600
while sec >= 60:
    sec = sec - 60

print(f'{hours}.{minutes}.{sec}')