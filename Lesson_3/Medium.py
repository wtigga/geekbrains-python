# coding=utf-8
# lesson 3, task easy

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000

employees = ['Walter', 'Callahan', 'Jake', 'Roland', 'Eddie', 'Susannah']
salaries = [150000, 20000, 5000, 90000, 45000, 35000]
salaries_list = dict(zip(employees, salaries))
list_of_keys = salaries_list.keys()

with open('salaries_file.txt', 'w+', encoding='utf-8') as opened_file:
    for keys in list_of_keys:
        to_write = (str(keys) + '\t-\t' + str(salaries_list.get(keys)) + '\n') # табуляция вместо пробела для настоящих столбцов, как в table delimited CSV
        opened_file.write(to_write)

# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),

with open('salaries_file.txt', 'r', encoding='utf-8',) as read_file:
    print('Зарплаты до 50 тыс. с вычетом налога 13%:\n')
    for entries in read_file:
        single_user_data = entries.split('\t')
        username = single_user_data[0]
        salary = float(single_user_data[2].rstrip('\n')) * 0.87
        if salary < 50000:
            print(username.upper(), '-', int(salary))


# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
