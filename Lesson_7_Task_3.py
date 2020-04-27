# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
import random


# Функция предназначена для поиска m+1 максимального элемента
# это число и будет являться медианой
def median(array, ind_, min_):
    count_max = 0
    index_median = []
    while count_max < ind_:
        max_ = min_
        index_ = 0
        for i, j in enumerate(array):
            l = [value for value in index_median if i == value]
            if len(l) == 0:
                if j > max_:
                    index_ = i
                    max_ = j
        index_median.append(index_)
        count_max += 1
    return arr[index_]


m = int(input('Введите натуральное число m: '))
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * m + 1)]
print(f'Массив случайных чисел размером {2 * m + 1} элементов: {arr}')
print(f'Медианой в массиве является число: {median(arr, (2 * m + 1) / 2, MIN_ITEM)}')
