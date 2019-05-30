'''
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
и ещё одна строка, которую нужно расшифровать.

Пример ввода:
abcd
*d%#
dcb
#b#b#
'''
alice = input('Введите исходный алфавит')
bob = input('Введите конечный алфавит')
to_code = input('Введите текст для кодировки')
encode = input('Введите текст для расшифровки')
to_code_exit = []
encode_exit = []
for i in to_code:
    for j in alice:
        if i == j:
            index = alice.index(j)
            x = bob[index]
            to_code_exit.append(x)
print('Закодированный текст:')
for i in to_code_exit:
    print(i, end='')
print('')

for i in encode:
    for j in bob:
        if i == j:
            index = bob.index(j)
            x = alice[index]
            encode_exit.append(x)
print('Расшифрованный текст:')
for i in encode_exit:
    print(i, end='')
