# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Иисходный массив: {array}')
m_ax = MIN_ITEM
for i, item in enumerate(array):
    if array[i] < 0:
        if m_ax < array[i]:
            m_ax = array[i]
            max_index = i
print(f'Максимальный отрицательный элементmax: {m_ax} с позицией в массиве: {max_index}')
