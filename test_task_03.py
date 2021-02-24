from task_03 import decimal_to_binary


def test_binary():
    assert decimal_to_binary('1'), 'Функция принимает значение числового типа'


def test_binary1():
    assert decimal_to_binary(8) == 34


def test_binary2():
    assert decimal_to_binary(5) == 101, 'Функция возвращает значение строкового типа'


def test_binary3():
    assert decimal_to_binary(5) == '101'


def test_binary4():
    assert decimal_to_binary(99) == '1100011'


def test_binary5():
    assert decimal_to_binary(1345)
