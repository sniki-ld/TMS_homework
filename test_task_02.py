from task_02 import word_palindrome1


def test_palindrom():
    assert word_palindrome1(1), 'Функция принимает значение строкового типа'


def test_palindrom1():
    assert word_palindrome1('1') == True


def test_palindrom2():
    assert word_palindrome1('radar') == True


def test_palindrom3():
    assert word_palindrome1('fds') == False


if __name__ == "__main__":
    test_palindrom()
    test_palindrom1()
    test_palindrom2()
    test_palindrom3()
