import random

n = random.randint(1, 50)
#   загадываем число от 1 до 50
i = int(input())
## 6 попыток пользователю,
y = 1          ## если не угадано, то сообщает пользователю
while y<6:
    if n > i:
        print(y)
        print("Загаданное число больше")
        i = int(input())
        y += 1
    if n < i:
        print(y)
        print("Загаданное число меньше")
        i = int(input())
        y += 1

    if n == i:
        print("Число отгадано!")
        break


if y == 6:
    print("Загаданное число:")
    print(n)