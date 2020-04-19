# 2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import Counter
from collections import deque


def sum_(a, b):
    res = deque()
    hex_ = Counter(
        {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
         'D': 13, 'E': 14, 'F': 15})
    hex_1 = Counter(
        {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
         13: 'D', 14: 'E', 15: 'F'})
    remainder = 0
    for j, i in enumerate(b):
        if j < len(a):
            c = hex_[i] + hex_[a[j]] + remainder
        else:
            c = hex_[i] + remainder
        if c > 15:
            remainder = 1
            c -= 16
        else:
            remainder = 0
        res.appendleft(hex_1[c])
    if remainder != 0:
        res.appendleft(1)
    return res


num1 = deque(input('Введите первое число в шестнадцатеричной системе исчисления: ').upper())
num2 = deque(input('Введите второе число в шестнадцатеричной системе исчисления: ').upper())

num1.reverse()
num2.reverse()
print('*' * 50)

if len(num1) <= len(num2):
    print(sum_(num1, num2))
else:
    print(sum_(num2, num1))
