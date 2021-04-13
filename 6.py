# Задание № 6

# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа,
# начиная с указанного,

# б) бесконечный итератор, повторяющий элементы
# некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle()
# модуля itertools.

from itertools import count
stop_num = int(input('Введите стоп число - '))
for i in count(int(input('Введите начальное число - '))):
    if i == stop_num:
        break
    else:
        print(i)


# from itertools import cycle
# number = 0
# stop_num = int(input('Введите количество строк - '))
# my_list = [True, 'ABC', 123, None]
# for el in cycle(my_list):
#     if number == stop_num:
#         break
#     print(el)
#     number += 1