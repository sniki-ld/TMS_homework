# Описать функцию для перевода десятичного числа в двоичное.
# Описать бесконечный цикл, в котором запрашивать у пользователя число
# и переводить его в двоичную систему. Признак окончания работы программы -
# введенное пользователем число 0.
# Подсказка: числа в двоичной системе хранить как строки.


def decimal_to_binary(decimal_number: int) -> str:
    """A function to convert a decimal number to binary."""
    binary_number = ''
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number


def main():
    """Function that converts a user-specified number to a binary system"""
    print('To end the program, enter numeral = 0')
    while 1:
        decimal_number = int(input())
        if decimal_number == 0:
            break
        else:
            print(decimal_to_binary(decimal_number))


if __name__ == '__main__':
    main()
