# 36. Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.

#     *Пример:*
#     [1, 5, 2, 3, 4, 6, 1, 7] =>  [1, 7]
#     [1, 5, 2, 3, 4, 1, 7] =>  [2, 5]

list1 = [1, 5, 2, 3, 4, 6, 1, 7]
list2 = [1, 5, 2, 3, 4, 1, 7]
list3 = [-2, -1, 5, 2, 3, 4, 4, 7, 8, 9, 6, 5, -3, 20, 21, 22]

def IncreasingSequence(lst):
    unique_sort_list = sorted(list(set(sorted(lst))))
    increasing_list = [unique_sort_list[0]]
    result_list = []
    count = 1
    for i in range(1, len(unique_sort_list)):
        if unique_sort_list[i] - 1 == increasing_list[-1]: # если сравниваемый элемент - 1 == последнему элементу списка
            increasing_list.append(unique_sort_list[i])
            count += 1
        elif unique_sort_list[i] - 1 != increasing_list[-1] and count == 1: # если сравниваемый элемент - 1 != последнему элементу списка, но уже есть хотя бы один готовый список
            increasing_list[0] = unique_sort_list[i]
        else:                                                               # во всех остальных случаях добавить список в итоговый
            result_list.append([increasing_list[0], increasing_list[-1]])
            increasing_list = []
            increasing_list = [unique_sort_list[i]]
            count = 1
    if len(increasing_list) > 1:
        result_list.append([increasing_list[0], increasing_list[-1]])
    return result_list


print(f'\nИзначальные данные: {sorted(list1)}')
print(f'Возрастающая последовательность(ти) => {IncreasingSequence(list1)}\n')

print(f'Изначальные данные: {sorted(list2)}')
print(f'Возрастающая последовательность(ти) => {IncreasingSequence(list2)}\n')

print(f'Изначальные данные: {sorted(list3)}')
print(f'Возрастающая последовательность(ти) => {IncreasingSequence(list3)}\n')