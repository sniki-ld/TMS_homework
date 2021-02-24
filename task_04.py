# Вычислить значения нижеприведенной функции
# в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
# y = x2 при -5 <= x <= 5;
# y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
# В качестве результат вывести на экран
# значение функции y при каждом x из указанного диапазона.


def my_function(x: int) -> int:
    """ Calculate function values for x in the range from -5 to 5 inclusive."""

    if x < -5:
        return 2 * abs(x) - 1
    elif x > 5:
        return 2 * x
    return x ** 2



def main():
    return [print(my_function(x), end=' ') for x in range(-10, 11)]


if __name__ == '__main__':
    main()
