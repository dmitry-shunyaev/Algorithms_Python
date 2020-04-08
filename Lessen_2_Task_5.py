# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def fun_sum(num):
    s = 0
    while num > 0:
        a = num % 10
        num = num // 10
        s = s + a
    return (s)


n = int(input('Вывод Введите целое положительное число. Для завершения работы программы нажмите "0" :'))
sum_num_max = 0
number = 0
while n != 0:
    sum_num = fun_sum(n)
    if sum_num_max < sum_num:
        sum_num_max = sum_num
        number = n
    n = int(input('Вывод Введите целое положительное число. Для завершения работы программы нажмите "0" :'))
print(f'Число {number}. Сумма цифр {sum_num_max}.')
