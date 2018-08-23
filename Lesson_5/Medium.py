# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import Lesson_5.Easy as smpl
import os


def go_to_folder(direct_path):
    try:
        os.chdir(direct_path)
        print('Вы перешли в директорию {}.'.format(direct_path))
    except FileNotFoundError:
        print('Путь не найден.')


def view_dir_content(thing=[os.getcwd()]):
    dir_content = []
    try:
        for i in os.listdir(thing[0]):
            dir_content.append(i)
            print(i)
    except FileNotFoundError:
        print('Пустая директория.')
    return dir_content


command = 10
current_working_dir = os.getcwd()
path = os.getcwd()

while command != '0':
    print('Консольная утилита')
    print('1. Перейти в указанную папку')
    print('2. Перейти на уровень выше')
    print('3. Просмотреть содержимое текущей папки')
    print('4. Удалить папку')
    print('5. Создать папку')
    print('0. Выход')
    command = input('Введите команду: ')
    if command == '1':  # go to folder
        path = str(input('Введите путь: '))
        go_to_folder(path)
        path = os.getcwd()
    elif command == '2':  # go up one level
        go_to_folder('..')
        path = os.getcwd()
        print(path)
    elif command == '3':  # view folder content
        view_dir_content()
    elif command == '4':  # remove folder
        rmv = [str(input('Введите имя папки для удаления: '))]
        smpl.dirs_remove(rmv)
    elif command == '5':  # create folder
        crt = [str(input('Введите имя для новой папки: '))]
        smpl.dirs_create(crt)
print('До скорого!')

