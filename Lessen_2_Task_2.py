# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число # 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def fun_even(s, even):
    if s > 0:
        c = (s % 10)  # получаем последнюю цифру
        if (c % 2) == 0:
            even = even + 1
        return fun_even(s // 10, even)  # рекурсия отправляем число минус 1 символ
    return even


st = input('Введите целое натуральное число:')
even = fun_even(int(st), 0)
not_even = len(st) - even
print(f'Число {st} состоит из {even} - четных чисел и {not_even} - нечетных')
