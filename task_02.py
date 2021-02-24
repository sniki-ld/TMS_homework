# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
# т. е. таким, которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)


def word_palindrome1(word):
    pol = word[::-1]
    if pol != word:
        return False
    return True


def main():
    words = 'abba', 'jhgfdss', 'radar'
    for word in words:
        print(word_palindrome1(word))


if __name__ == '__main__':
    main()
