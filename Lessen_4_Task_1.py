# 3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import timeit
import cProfile


def func2(size, min_item, max_item):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    min_index = 0
    max_index = 0
    m_ax = None
    m_in = None
    for i, x in enumerate(array):
        m_ax = x
        m_in = x
        for j, y in enumerate(array):
            if m_ax < y:
                m_ax = y
                max_index = j
            if m_in > y:
                m_in = y
                min_index = j

    # print(f'Исходный массив:      {array}')
    array[min_index] = m_ax
    array[max_index] = m_in
    # print(f'Результирующий массив:{array}')


def func(size, min_item, max_item):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    min_index = 0
    max_index = 0
    m_ax = array[0]
    m_in = array[0]
    for i, x in enumerate(array):
        if m_ax < x:
            m_ax = x
            max_index = i
        if m_in > x:
            m_in = x
            min_index = i

    #    print(f'Исходный массив:      {array}')
    array[min_index] = m_ax
    array[max_index] = m_in


#    print(f'Результирующий массив:{array}')

def func1(size, min_item, max_item):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    max_index = 0
    m_ax = array[0]
    for i, x in enumerate(array):
        if m_ax < x:
            m_ax = x
            max_index = i
    min_index = 0
    m_in = array[0]
    for i, x in enumerate(array):
        if m_in > x:
            m_in = x
            min_index = i

    #    print(f'Исходный массив:      {array}')
    array[min_index] = m_ax
    array[max_index] = m_in


#    print(f'Результирующий массив:{array}')

print(timeit.timeit('func(100, 0, 100)', number=100, globals=globals()))  # 0.0110179
print(timeit.timeit('func(200, 0, 100)', number=100, globals=globals()))  # 0.021862899999999998
print(timeit.timeit('func(300, 0, 100)', number=100, globals=globals()))  # 0.034398
print(timeit.timeit('func(400, 0, 100)', number=100, globals=globals()))  # 0.04625520000000001
print(timeit.timeit('func(500, 0, 100)', number=100, globals=globals()))  # 0.6098329
print('*' * 20 + 'два не вложенных цикла в функции')
print(timeit.timeit('func1(100, 0, 100)', number=100, globals=globals()))  # 0.011531100000000016
print(timeit.timeit('func1(200, 0, 100)', number=100, globals=globals()))  # 0.023364700000000016
print(timeit.timeit('func1(300, 0, 100)', number=100, globals=globals()))  # 0.03538109999999994
print(timeit.timeit('func1(400, 0, 100)', number=100, globals=globals()))  # 0.046049100000000065
print(timeit.timeit('func1(500, 0, 100)', number=100, globals=globals()))  # 0.058210400000000107
print('*' * 20 + 'появился вложенный цикл в функции')
print(timeit.timeit('func2(100, 0, 100)', number=100, globals=globals()))  # 0.10023910000000003
print(timeit.timeit('func2(200, 0, 100)', number=100, globals=globals()))  # 0.3531232
print(timeit.timeit('func2(300, 0, 100)', number=100, globals=globals()))  # 0.8711872000000002
print(timeit.timeit('func2(400, 0, 100)', number=100, globals=globals()))  # 1.4448256000000002
print(timeit.timeit('func2(500, 0, 100)', number=100, globals=globals()))  # 2.2609345000000003

cProfile.run('func2(100, 0, 100)')
cProfile.run('func2(200, 0, 100)')
cProfile.run('func2(300, 0, 100)')
cProfile.run('func2(400, 0, 100)')
cProfile.run('func2(500, 0, 100)')

# Пример для cProfile.run('func(500, 0, 100)') - генерация массива из 500 элементов
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#        1    0.000    0.000    0.002    0.002 Lessen_4_Task_1.py:7(func)
#        1    0.000    0.000    0.002    0.002 Lessen_4_Task_1.py:8(<listcomp>)
#      500    0.001    0.000    0.001    0.000 random.py:200(randrange)
#      500    0.000    0.000    0.002    0.000 random.py:244(randint)
#      500    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      642    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Пример для cProfile.run('func2(500, 0, 100)') - генерация массива из 500 элементов - сильно изменилось время работы функции
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.023    0.023 <string>:1(<module>)
#        1    0.022    0.022    0.023    0.023 Lessen_4_Task_1.py:7(func2)
#        1    0.000    0.000    0.001    0.001 Lessen_4_Task_1.py:8(<listcomp>)
#      500    0.000    0.000    0.001    0.000 random.py:200(randrange)
#      500    0.000    0.000    0.001    0.000 random.py:244(randint)
#      500    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
#      500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      631    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# Вывод
# Я сделал три функции func, func1, func2 - фсе функции вызывал 5 раз с разной длинной массива от 100 до 500
# По результатам работы timeit сделал вывод:
#   - func (один цикл) и func1(два но не вложенных цикла) асимптотика линейная
#   - в функци func2 используется вложенный цикл. Наблюдается квадратичная асимптотика
# в функци func2 использовал заведомо не правильный алгоритм с целью проверки
# Функция cProfile показывает что в моих функция самое большое количество раз используется модуль random
# так же видно что в func2 используется не правильный алгоритм из-за вложенности циклов
#   время выполнения значительно отличается от функции func

# в целях оптимизации относительно первой сданной работы избавился от среза массива в цикле
