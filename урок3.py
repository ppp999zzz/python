#  Пользователь вводит числа до тех пор, пока не вводит 0
#  После ввода 0, программа завершается и выводит кол-во чисел

counter = 0
while True:
    a = int(input("введите число: "))
    counter = counter + 1
    if a == 0:
        break
print(counter)