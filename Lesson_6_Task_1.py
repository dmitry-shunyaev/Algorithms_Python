# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


import sys


def func1(n):
    count_ = 3
    while True:
        max_sieve = 0
        sieve = [i for i in range(count_)]
        max_sieve = sys.getsizeof(sieve)  # при максимальной длинне списка
        for s in sieve:  # в цикле считаем объем рамяти занимаемы элементами списка
            max_sieve += sys.getsizeof(s)
        sieve[1] = 0
        for i in range(2, count_):
            if sieve[i] != 0:
                j = i + i
                while j < count_:
                    sieve[j] = 0
                    j += i
        # на выходе из циклов будут максимальные числовые значения i,j
        max_sieve += sys.getsizeof(i)
        max_sieve += sys.getsizeof(j)
        res = [i for i in sieve if i != 0]
        max_sieve += sys.getsizeof(res)
        for s in res:  # в цикле считаем объем рамяти занимаемы элементами списка
            max_sieve += sys.getsizeof(s)
        count_ += 1
        max_sieve += sys.getsizeof(count_)
        if len(res) == n:
            max_sieve += sys.getsizeof(n)
            print(f'Объем памяти всех переменных функции: {max_sieve} байт')
            return res[len(res) - 1]
            break


def func3(n):
    if n == 1:
        k = 3
    else:
        k = n
    while True:
        max_sieve = 0
        sieve = [i for i in range(k)]
        max_sieve = sys.getsizeof(sieve)  # при максимальной длинне списка
        sieve[1] = 0
        for i in range(2, k):
            if sieve[i] != 0:
                j = i + i
                while j < k:
                    sieve[j] = 0
                    j += i
        # на выходе из циклов будут максимальные числовые значения i,j
        max_sieve += sys.getsizeof(i)
        max_sieve += sys.getsizeof(j)
        res = [i for i in sieve if i != 0]
        max_sieve += sys.getsizeof(res)
        for s in res:  # в цикле считаем объем рамяти занимаемы элементами списка
            max_sieve += sys.getsizeof(s)
        if len(res) > n:
            max_sieve += sys.getsizeof(n)
            print(f'Объем памяти всех переменных функции: {max_sieve} байт')
            return res[n - 1]
            break
        else:
            k *= 2


# - измерентя

def func2(n):
    count_ = 0
    i = 2
    max_sieve = 0
    while True:
        j = 1
        x = 0
        while j <= i:
            if i % j == 0:
                x += 1
            if i <= j:
                break
            j += 1
        if x == 2:
            count_ += 1
        if count_ == n:
            max_sieve += sys.getsizeof(count_)
            max_sieve += sys.getsizeof(i)
            max_sieve += sys.getsizeof(j)
            max_sieve += sys.getsizeof(x)
            max_sieve += sys.getsizeof(n)
            print(f'Объем памяти всех переменных функции: {max_sieve} байт')
            return i
            break
        else:
            i += 1


n_ = int(input('Введите порядковый номер простого числа: '))

res_ = func1(n_)
print(f'Func1 возвращает Число: {res_} является {n_}-м простым числом')

res_ = func3(n_)
print(f'Func3 возвращает Число: {res_} является {n_}-м простым числом')

res_ = func2(n_)
print(f'Func2 возвращает Число: {res_} является {n_}-м простым числом')

# Вывод: при поиске 100-го простого числа:
#    Функци Func1 занимае в памяти 11914 байт
#    Функци Func3 занимае в памяти 6132 байт
#    Функци Func2 занимае в памяти 70 байт
