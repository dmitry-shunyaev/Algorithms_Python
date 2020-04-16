# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# sieve(2)
# 3
# prime(4)
# 7
# sieve(5)
# 11
# prime(1)
# 2
import timeit


## Рещение задачи с помощью алгоритма «Решето Эратосфена».
def func1(n):
    count_ = 3
    while True:
        sieve = [i for i in range(count_)]
        sieve[1] = 0
        for i in range(2, count_):
            if sieve[i] != 0:
                j = i + i
                while j < count_:
                    sieve[j] = 0
                    j += i
        res = [i for i in sieve if i != 0]
        count_ += 1
        if len(res) == n:
            return res[len(res) - 1]
            break


def func3(n):
    k = n
    while True:
        sieve = [i for i in range(k)]
        sieve[1] = 0
        for i in range(2, k):
            if sieve[i] != 0:
                j = i + i
                while j < k:
                    sieve[j] = 0
                    j += i
        res = [i for i in sieve if i != 0]
        if len(res) > n:
            return res[n - 1]
            break
        else:
            k *= 2



## Рещение задачи без использования «Решето Эратосфена».
## n = int(input('Введите порядковый номер простого числа: '))
def func2(n):
    count_ = 0
    i = 2
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
            return i
            break
        else:
            i += 1


n_ = int(input('Введите порядковый номер простого числа: '))
res_ = func1(n_)
print(f'Func1 возвращает Число: {res_} является {n_}-м простым числом')

# алгоритм имеет кубическую зависимость 3 вложенных цикла
# алгорит создан в учемных целях для того что бы понять как делать нельзя!
# print(timeit.timeit('func1(10)', number=100, globals=globals()))  # 0.013779000000000003
# print(timeit.timeit('func1(20)', number=100, globals=globals()))  # 0.07460710000000001
# print(timeit.timeit('func1(30)', number=100, globals=globals()))  # 0.1868918
# print(timeit.timeit('func1(40)', number=100, globals=globals()))  # 0.44684149999999995
# print(timeit.timeit('func1(50)', number=100, globals=globals()))  # 0.7803143

res_ = func3(n_)
print(f'Func3 возвращает Число: {res_} является {n_}-м простым числом')

# понимая что трачу больше памяти но алгоритм работает на много быстрее
#   очень хорошо видно при N больше 100
# алгоритм имеет линейную асимптотику не смотря на 2 вложенных цикла
# алгорит создан в учемных целях для того что бы понять как делать нельзя!
#print(timeit.timeit('func3(100)', number=100, globals=globals()))  # 0.002058000000000001
#print(timeit.timeit('func3(200)', number=100, globals=globals()))  # 0.0039034000000000013
#print(timeit.timeit('func3(300)', number=100, globals=globals()))  # 0.013007299999999996
#print(timeit.timeit('func3(400)', number=100, globals=globals()))  # 0.017832999999999995
#print(timeit.timeit('func3(500)', number=100, globals=globals()))  # 0.022890900000000006

res_ = func2(n_)
print(f'Func2 возвращает Число: {res_} является {n_}-м простым числом')
# алгоритм имеет квадратичную зависимость 2 вложенны цикл
# print(timeit.timeit('func2(10)', number=100, globals=globals()))  # 0.006577400000000001
# print(timeit.timeit('func2(20)', number=100, globals=globals()))  # 0.03619460000000001
# print(timeit.timeit('func2(30)', number=100, globals=globals()))  # 0.08904219999999999
# print(timeit.timeit('func2(40)', number=100, globals=globals()))  # 0.2049377
# print(timeit.timeit('func2(50)', number=100, globals=globals()))  # 0.358004
