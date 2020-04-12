# 3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_index = 0
max_index = 0

m_ax = array[0]
m_in = array[0]
for i, x in enumerate(array[1:len(array)]):
    if m_ax < x:
        m_ax = x
        max_index = i + 1
    if m_in > x:
        m_in = x
        min_index = i + 1

print(f'Исходный массив:      {array}')
array[min_index] = m_ax
array[max_index] = m_in
print(f'Результирующий массив:{array}')
