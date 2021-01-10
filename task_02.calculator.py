# Написать программу, в которой вводятся два операнда Х и Y
# и знак операции sign (+, –, /, *). Вычислить результат Z в зависимости от знака.
# Предусмотреть реакции на возможный неверный знак операции,
# а также на ввод Y=0 при делении. Организовать возможность многократных вычислений
# без перезагрузки программа (т.е. построить бесконечный цикл).
# В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').

print('To end the program, enter sing == 0')

while 1:
    sign = input('Enter operation sign  +, –, /, * : ')
    if sign == '0':
        break
    if sign in ('+', '-', '/', '*'):
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second  number: '))
        if sign == '+':
            z = x + y
            print(f'Addition result: {z}')
        elif sign == '-':
            z = x - y
            print(f'Subtraction result: {z}')
        elif sign == '*':
            z = x * y
            print(f'Multiplication result: {z}')
        elif sign == '/':
            if not y == 0:
                z = x / y
                print(f'Division result: {z}')
            else:
                print('You cannot divide by zero !')
    else:
        print('Invalid operation sign')
