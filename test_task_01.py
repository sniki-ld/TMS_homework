from task_01 import fact2


def test_fact():
    assert fact2('3') == 15, 'n должно быть целым числом'


def test_fact1():
    assert fact2(5.0) == 15, 'n должно быть целым числом'


def test_fact2():
    assert fact2(5) == 15


def test_fact3():
    assert fact2(-5) == 15,  'n должно быть целым, положительным числом'


if __name__ == "__main__":
    test_fact()
    test_fact1()
    test_fact2()
    test_fact3()
