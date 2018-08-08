#coding=utf-8
#lesson 1, task medium


print('Жданов Владимир, домашнее задание №1 medium')
print('Задача 1')


user_input = int(input('Введите число от 1 до 10: '))
while (user_input > 10) or (user_input < 0):
    user_input = int(input('Неправильно. Введите число от 1 до 10: '))
user_input = user_input ** 2
print(user_input)



print('Жданов Владимир, домашнее задание №1 medium')
print('Задача 2')

user_input_1 = int(input('Введите первое число:  '))
user_input_2 = int(input('Введите второе число:  '))

#кручу верчу обмануть хочу

user_input_1 = user_input_1 + user_input_2
user_input_2 = user_input_1 - user_input_2
user_input_1 = user_input_1 - user_input_2

print('Первая переменная: ', user_input_1, '; вторая переменная: ', user_input_2)