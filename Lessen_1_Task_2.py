# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
print('Введите две буквы')

first_simbol = input('Первая латинская буква:')
second_simbol = input('Вторая латинская буква:')

print(f'Позиция в алфавите буквы {first_simbol} = {ord(first_simbol) - 96}')
print(f'Позиция в алфавите буквы {second_simbol} = {ord(second_simbol) - 96}')
print(f'Между буквами "{first_simbol}"  и  "{second_simbol}"  {abs(ord(second_simbol) - ord(first_simbol) - 1)} символ')

