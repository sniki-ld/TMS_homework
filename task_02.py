# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость - 5),
# стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости).
# Все атрибуты приватные.

# from typing import Optional, Union


class Car:
    """ Simple car model.

    Attributes
    ----------
    car_brand : str
        the auto car_brand
    model: str
        the auto model
    year: int
        the year of car production
    speed: int - default = 0
        the auto speed
    """

    def __init__(self, car_brand: str, model: str, year: int, speed: int = 0) -> None:
        """ Инициализирует атрибуты car_brand, model, year, speed"""
        self.__car_brand = car_brand
        self.__model = model
        self.__year = year
        self.__speed = speed
        new_speed = 0

    def information_car_print(self) -> str:
        """Выводит информацию о экземпляре class Car"""
        return f'АВТОМОБИЛЬ: {self.__car_brand}, {self.__model}, {self.__year}, начальная скорость:{self.__speed}'

    def increase_speed(self) -> int:
        """Скорость машины увеличивается на 5"""
        new_speed = self.__speed + 5
        self.__speed = new_speed
        return self.__speed

    def decrease_speed(self) -> int:
        """Скорость машины уменьшается на 5"""
        if self.__speed < 5:
            return 0
        else:
            new_speed = self.__speed - 5
            self.__speed = new_speed
            return self.__speed

    def stop_speed(self) -> int:
        """Машина останавливается speed = 0"""
        self.__speed = 0
        return self.__speed

    def reversal(self) -> int:
        """Машина разворачивается"""
        new_speed = - self.__speed
        self.__speed = new_speed
        return self.__speed


def main():
    my_new_car = Car('audi', 'A4', 2018)
    a = my_new_car.information_car_print()
    print(a)
    print(f'Увеличить скорость: {my_new_car.increase_speed()}')
    print(f'Уменьшить скорость : {my_new_car.decrease_speed()}')
    print(f'Увеличить скорость: {my_new_car.increase_speed()}')
    print(f'Стоп: {my_new_car.stop_speed()}')
    print()

    my_new_car2 = Car('ford', 'Focus', 2010, 20)
    b = my_new_car2.information_car_print()
    print(b)
    print(f'Увеличить скорость: {my_new_car2.increase_speed()}')
    print(f'Увеличить скорость: {my_new_car2.increase_speed()}')
    print(f'Уменьшить скорость : {my_new_car2.decrease_speed()}')
    print(f'Увеличить скорость: {my_new_car2.increase_speed()}')
    print(f'Уменьшить скорость : {my_new_car2.decrease_speed()}')
    print(f'Стоп: {my_new_car2.stop_speed()}')
    print(f'Уменьшить скорость : {my_new_car2.decrease_speed()}')
    print(f'Увеличить скорость: {my_new_car2.increase_speed()}')
    print(f'Разворот: {my_new_car2.reversal()}')
    print(f'Увеличить скорость: {my_new_car2.increase_speed()}')
    print(f'Увеличить скорость: {my_new_car2.increase_speed()}')


if __name__ == '__main__':
    main()
