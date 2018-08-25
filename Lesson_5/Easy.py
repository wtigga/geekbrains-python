# coding=utf-8
# lesson 5, task easy

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil


def dir_list(num_start, num_stop, prefix="dir_"):
    list_full = [(prefix + str(i)) for i in range(int(num_start), int(num_stop))]
    return list_full


def dirs_create(directories_list):
    for entry in directories_list:
        try:
            os.mkdir(entry)
        except FileExistsError:
            print('Директория {} уже существует'.format(entry))


# dirs_create(dir_list(1, 10))


def dirs_remove(directories_list):
    for entry in directories_list:
        try:
            os.rmdir(entry)
            print('Директория {} удалена'.format(entry))
        except OSError:
            print('Директория {} не пустая, либо не существует.'.format(entry))


# dirs_remove(dir_list(1, 10))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_only_dirs(thing):
    only_dirs_list = []
    for i in os.listdir(thing):
        if os.path.isdir(i): # print only if directory
            only_dirs_list.append(i)
        else:
            continue
    return only_dirs_list


# print(list_only_dirs(os.getcwd()))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def self_backup():
    shutil.copy2(__file__, (__file__ + ".backup"))


# self_backup()
