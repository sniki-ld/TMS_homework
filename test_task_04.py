from task_04 import my_function


def test_my_function():
    assert my_function('4'), 'Функция принимает значение числового типа'


def test_my_function1():
    assert my_function(-10) == 19


def test_my_function2():
    assert my_function(-5) == 25


def test_my_function3():
    assert my_function(0) == 0


def test_my_function4():
    assert my_function(10) == '1100011', 'Функция возвращает значение числового типа'


def test_my_function5():
    assert my_function(99)
