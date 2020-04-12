# 7.	В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
m_in1 = array[0]
min_index = 0
m_in2 = 0
print(f'Иисходный массив: {array}')
for i, item in enumerate(array[1:len(array)]):
    if item < m_in1:
        min_index = i + 1
        m_in1 = item
if min_index != 0:
    m_in2 = array[0]
else:
    m_in2 = array[1]
for i, item in enumerate(array[1:len(array)]):
    if i + 1 != min_index:
        if item < m_in2:
            m_in2 = item

print(f'Минмальное значение1 : {m_in1}')
print(f'Минмальное значение2 : {m_in2}')
