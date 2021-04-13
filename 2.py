# Задание № 2

# Представлен список чисел. Необходимо вывести элементы
# исходного списка, значения которых больше предыдущего элемента.

# Подсказка: элементы, удовлетворяющие условию, оформить
# в виде списка. Для формирования списка использовать генератор.

print('Вариант с генератором')
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [el for el in list if el > list[list.index(el)-1]]
print(f'Исходный список {list}')
print(f'Новый список {new}')

print('-'*55)

print('Вариант с циклом')
i = 0
new= []
for el in list:
    if el > list[i-1]:
        new.append(el)
    i+=1
print(f'Новый список {new}')