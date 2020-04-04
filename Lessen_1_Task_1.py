# ссылка на блоксхему
# https://drive.google.com/file/d/1SKjDIPdaDrrRxJZX8-UfqHc80w2J_efO/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
x = int(input('Введите положительное целое трехзначное число:'))
a = int(x / 100)
x = (x - a * 100)
b = int(x / 10)
c = (x - b * 10)

print(f'Сумма чисел: {a} + {b} + {c} = {a + b + c}')
print(f'Произведение чисел: {a} * {b} * {c} = {a * b * c}')
