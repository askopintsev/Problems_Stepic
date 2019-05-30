# CAlCULATOR 1
# input cipher 1
# input cipher 2
# input operation sign

a = float(input())
b = float(input())
op = str(input())
result = 0

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '/':
    if b != 0:
        result = a / b
    else:
        result = 'Деление на 0!'
elif op == '*':
    result = a * b
elif op == 'mod':
    if b != 0:
        result = a % b
    else:
        result = 'Деление на 0!'
elif op == 'pow':
    result = a ** b
elif op == 'div':
    if b != 0:
        result = a // b
    else:
        result = 'Деление на 0!'
print(result)
