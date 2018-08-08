#coding=utf-8
#lesson 1, task easy

print('Жданов Владимир, домашнее задание №1 easy')
print('Задача 1')

variable_A = input('Введите значение переменной "A"  ')
print('Значение переменной "А": ', variable_A)

variable_B = input('Введите значение переменной "В"  ')
print('Значение переменной "А" и "В":', variable_A, 'и', variable_B)



print('Задача 2')

variable_A = int(input('Введите значение переменной "A" в виде целого числа: '))
print('Значение переменной "А" + 2: ', (variable_A+2))

print('Задача 3')

user_age = int(input('Ваш возраст: '))
if user_age >= 18:
    print('Доступ разрешён.')
else:
    print('Извините, пользование данным ресурсом только с 18 лет.')
