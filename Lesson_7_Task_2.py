# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


# Пример сортировки слиянием из Википедии.
# Сначала делим список на кусочки (по 1 элементу),
# затем сравниваем каждый элемент с соседним,
# сортируем и объединяем.
# В итоге, все элементы отсортированы и объединены вместе.


def crush_arr(array):  # Разбиваем массив на элементы
    n = len(array)
    if n <= 1:
        return array
    else:
        middle = int(len(array) / 2)
        left_arr = crush_arr([left for i, left in enumerate(array) if i < middle])
        right_arr = crush_arr([right for i, right in enumerate(array) if i > middle - 1])
        return sort_merge(left_arr, right_arr)


def sort_merge(left_, right_):  # Сравниваем и объединяем
    res = []
    while len(left_) > 0 and len(right_) > 0:
        if left_[0] <= right_[0]:  # Сравниваем первые элементы
            res.append(left_[0])
            left_ = [left for i, left in enumerate(left_) if i >= 1]  # Массив без первого элемента
        else:
            res.append(right_[0])
            right_ = [right for i, right in enumerate(right_) if i >= 1]  # Массив без первого элемента
    # Сливаем обе части
    if len(left_) > 0:
        res += left_
    if len(right_) > 0:
        res += right_
    return res


SIZE = 10
MIN_ITEM = 0.00
MAX_ITEM = 49.99
arr = [round(random.uniform(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]
print(f'Исходный массив: {arr}')
result = crush_arr(arr)
print(f'Отсортированный массив: {result}')
