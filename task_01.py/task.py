# Создать класс MyTime.
# Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы
# сравнения(==, !=, >=, <=, <, >), сложения, вычитания, умножения на число, вывод на экран.


from validation import valid_value, valid_time
from exeptions import TimeError


class MyTime:
    def __init__(self, hours: int, minutes: int, seconds: int):
        valid_value(hours, minutes, seconds)
        valid_time(hours, minutes, seconds)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time = self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        return f"Time {self.hours}:{self.minutes}:{self.seconds}"

    def __eq__(self, other):
        """Проверяет равенство двух значений времени.
        other должен быть обьектом класса MyTime
        """
        if isinstance(other, MyTime):
            return self.time == other.time
        else:
            raise TimeError

    def __ne__(self, other):
        """Проверяет неравенство двух значений времени.
        other должен быть обьектом класса MyTime
        """
        if isinstance(other, MyTime):
            return self.time != other.time
        else:
            raise TimeError

    def __add__(self, other):
        """Складывает двa значения времени.
        other должен быть обьектом класса MyTime.
        """
        if isinstance(other, MyTime):
            return self.time + other.time

    def __mul__(self, other):
        """Перемножает двa значения времени, либо умножает время на число.
        other должен быть обьектом класса MyTime, int, float
        """
        if isinstance(other, MyTime):
            return self.time * other.time
        if isinstance(other, (int, float)):
            return self.time * other

    def __sub__(self, other):
        """Вычитает двa значения времени.
        other должен быть обьектом класса MyTime.
        """
        if isinstance(other, MyTime):
            return self.time - other.time

    def __gt__(self, other):
        """Определяет поведение оператора больше, >.
        other должен быть обьектом класса MyTime.
        """
        if isinstance(other, MyTime):
            return self.time > other.time

    def __lt__(self, other):
        """Определяет поведение оператора меньше, <.
        other должен быть обьектом класса MyTime.
        """
        if isinstance(other, MyTime):
            return self.time < other.time

    def __ge__(self, other):
        """Определяет поведение оператора больше или равно, >=.
        other должен быть обьектом класса MyTime.
        """
        if isinstance(other, MyTime):
            return self.time >= other.time

    def __le__(self, other):
        """Определяет поведение оператора меньше или равно, <=.
        other должен быть обьектом класса MyTime.
        """
        if isinstance(other, MyTime):
            return self.time <= other.time


def main():
    my_object = MyTime(1, 0, 0)
    print(my_object)

    my_object_new = MyTime(1, 0, 0)
    print(my_object_new)

    print('Проверка равенства (__eq__):', my_object == my_object_new)
    print('Проверка неравенства (__ne__):', my_object != my_object_new)
    print('Сложение (__add__):', my_object + my_object_new)
    print('Умножение (__mul__):', my_object * my_object_new)
    print('Умножение на число (__mul__):', my_object * 1.5)
    print('Вычитание (__sub__):', my_object - my_object_new)
    print('Сравнение (оператор больше, >) (__gt__):', my_object > my_object_new)
    print('Сравнение (оператор меньше, <) (__lt__):', my_object < my_object_new)
    print('Сравнение (оператор больше или равно, >=) (__ge__):', my_object >= my_object_new)
    print('Сравнение (оператор меньше или равно, <=) (__le__):', my_object <= my_object_new)
    print('-' * 5)

    my_object2 = MyTime(12, 12, 12)
    print(my_object2)

    my_object_new2 = MyTime(15, 30, 16)
    print(my_object_new2)

    print('Проверка равенства (__eq__):', my_object2 == my_object_new2)
    print('Проверка неравенства (__ne__):', my_object2 != my_object_new2)
    print('Сложение (__add__):', my_object2 + my_object_new2)
    print('Умножение (__mul__):', my_object2 * my_object_new2)
    print('Умножение на число (__mul__):', my_object2 * 1.5)
    print('Вычитание (__sub__):', my_object2 - my_object_new2)
    print('Сравнение (оператор больше, >) (__gt__):', my_object2 > my_object_new2)
    print('Сравнение (оператор меньше, <) (__lt__):', my_object2 < my_object_new2)
    print('Сравнение (оператор больше или равно, >=) (__ge__):', my_object2 >= my_object_new2)
    print('Сравнение (оператор меньше или равно, <=) (__le__):', my_object2 <= my_object_new2)


if __name__ == '__main__':
    main()
