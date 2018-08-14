# coding=utf-8
# lesson 2, task easy

print("Задача-1\n")
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruit_list = ["яблоко", "банан", "киви", "арбуз"]
print("Список фруктов:", fruit_list, "\n")
list_len = int(len(fruit_list))

print("Используя while...")
counter = 0
while counter < list_len:
    print(str((counter + 1)) + ". " + fruit_list[counter])
    counter = counter + 1
print("\n")


print("Используя for loop...")
counter = 1
for fruit in fruit_list:
    print(str(counter) + ".", fruit)
    counter += 1
print("\n")

print("Используя format...")
counter = 1
while counter <= list_len:
    print(str(counter) + ". {}".format(fruit_list[counter-1]))
    counter += 1

print("\nЗадача-2\n")
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_one = ["яблоко", "банан", "киви", "арбуз", "апельсин"]
list_two = ["мясо", "банан", "рыба", "кошки"]

print("Список №1:", list_one)
print("Список №2:", list_two)
print("Сравниваем списки №1 и №2...\n")

counter = 0
list_len = len(list_one)

while counter < (list_len-1):
    if list_one[counter] in list_two:
        print("Под номером {0} найден повтор ({1}), удаляем его из первого списка.".format((counter+1), list_one[counter]))
        list_one.pop(counter)
    counter = counter + 1

print("Обновлённый список №1:", list_one)


print("\nЗадача-3\n")
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Текущий список чисел: ", numbers_list)
new_list = []
print("Кратные двум делим на 4, не кратные умножаем на 2")
for number in numbers_list:
    if number % 2 == 0:
        to_add = number / 4
    else:
        to_add = number * 2
    new_list.append(to_add)
print(new_list)


