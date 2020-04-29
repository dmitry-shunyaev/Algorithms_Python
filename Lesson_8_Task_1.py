# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:

# func("papa")
# 6
# func("sova")
# 9


import hashlib


def substring_count(str_):
    result_set = set()  # используем множество для подсчета только уникальных элементов
    len_str = len(str_)
    for i in range(len_str + 1):
        for j in range(i + 1, len_str + 1):
            if str_ != str_[i: j]:
                h = hashlib.sha1(str_[i:j].encode('utf-8')).hexdigest()  # хэш
                result_set.add(h)
    return len(result_set)  # возвращаем кол-во элементов множества result_set


str_input = input('Введите слово:')
print(substring_count(str_input))
