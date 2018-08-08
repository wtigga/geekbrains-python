# coding=utf-8
# lesson 1, task hard

print('Жданов Владимир, домашнее задание №1 hard')
print('Задача 1')

# имя, фамилию, возраст, и вес.

print('Медицинская анкета:')
user_firstname = input('Ваше имя: ')
user_lastname = input('Ваша фамилия: ')
user_age = input('Ваш возраст: ')
user_weight = input('Ваш вес: ')

user_age = int(user_age)
user_weight = int(user_weight)


# функция для вывода информации о пользователе
def user_full_report():
    print(user_firstname, user_lastname + ',', user_age, 'лет,', user_weight,'кг.')


# индикатор нездорового веса
weight_status = 0

# определение здоровости веса
if (user_weight > 120) or (user_weight < 50):
    weight_status = 1
else:
    weight_status = 0


if weight_status == 1:
    if user_age > 60:
        user_full_report()
        print('Вызывайте неотложку!')
    elif user_age > 40:
        user_full_report()
        print('Обратитесь к врачу.')
    elif user_age > 30:
        user_full_report()
        print('Вам нужно вести здоровый образ жизни.')
    else:
        print('Вы вводите алгоритм в заблуждение.')
else:
    user_full_report()
    print('У вас всё отлично!')
input()
# задержка выключения программы
