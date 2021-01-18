# Вычислить значения нижеприведенной функции
# в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
# y = x2 при -5 <= x <= 5;
# y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
# В качестве результат вывести на экран
# значение функции y при каждом x из указанного диапазона.


def my_function(x: int) -> int:
    """ Calculation of mathematical operations for x."""
    if -5 <= x <= 5:
        y = x ** 2
        return y
    elif x < -5:
        y = 2 * abs(x) - 1
        return y
    elif x > 5:
        y = 2 * x
        return y


def main():
    """Calculate the value of a function in a given range."""
    return [print(my_function(x), end=' ') for x in range(-10, 11)]


if __name__ == '__main__':
    main()
