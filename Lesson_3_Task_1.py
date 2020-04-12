# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

list_num = (list(range(2, 100)))
Arr = (list(range(2, 10)))
for i, value in enumerate(Arr):
    Arr[i] = [value, 0]

for i, x in enumerate(list_num):
    for j, value in enumerate(Arr):
        if x % Arr[j][0] == 0:
            Arr[j][1] = Arr[j][1] + 1

for j, value in enumerate(Arr):
    print(f'Цифре {Arr[j][0]} кратно: {Arr[j][1]} чисел')
