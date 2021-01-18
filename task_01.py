# Описать функцию fact2(n), вычисляющую двойной факториал: n!! = 1·3·5·...·n,
# если n — нечетное; n!! = 2·4·6·...·n,
# если n — четное (n > 0 — параметр целого типа).
# С помощью этой функции найти двойные факториалы пяти случайных целых чисел.


from random import randint


def fact2(n: int) -> int:
    """A function that calculates the double factorial of even and odd numbers."""
    if n % 2 != 0:
        pr = 1
        for i in range(3, n + 1, 2):
            pr *= i
        return pr

    else:
        pr = 2
        for i in range(4, n + 1, 2):
            pr *= i
        return pr


def main():
    """A function that calculates the double factorial of five random integers"""
    a, b = map(int, input('Enter two integers separated by a space: ').split())

    random_number = [randint(a, b) for i in range(5)]
    print(list(random_number))
    return [print(fact2(n), end=' ') for n in random_number]


if __name__ == '__main__':
    main()

