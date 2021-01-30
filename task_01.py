# Создать три класса, описывающие реальные объекты.
# Каждый класс должен содержать минимум
# три приватных атрибута, конструктор, геттеры и сеттеры для каждого атрибута, два метода.


class Zoo:
    """ Represents zoo animals.

    Attributes
    ----------
    nickname : str
        the name of the animal
    age: int
        the age of the animal
    aviary_number: int
        the aviary number of animal
    """

    def __init__(self, nickname: str, age: int, aviary_number: int) -> None:
        """Initializes the animal and its location in the zoo.
        Parameters
        ----------
        nickname : str
            The name of the animal.
        age: int
            The age of the animal.
        aviary_number: int
            The aviary number of animal.
        """
        self.nickname = nickname
        self.__age = age
        self.__aviary_number = aviary_number

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def aviary_number(self):
        return self.__aviary_number

    @aviary_number.setter
    def aviary_number(self, aviary_number):
        self.__aviary_number = aviary_number


class Bear_family(Zoo):
    """Represents data specific to bears."""

    def __init__(self, nickname: str, age: int, aviary_number: int, color: str) -> None:
        """Initializes the attributes of the parent class.Then it initializes the bear-specific attributes.
        Parameters
        ----------
        color: str - the bear-specific attributes
        The color of animal.
        """

        super().__init__(nickname, age, aviary_number)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def food_bear(self) -> str:
        return 'Bear eats!'

    def growl_bear(self) -> str:
        return 'gr-gr-gr!!!'


class Cat_family(Zoo):
    """Represents data specific to cats."""

    def __init__(self, nickname: str, age: int, aviary_number: int, representative: str) -> None:
        """Initializes the attributes of the parent class.Then it initializes the cat-specific attribute
        Parameters
        ----------
        representative: str - the cat-specific attributes
            The representative of animal.
        """
        super().__init__(nickname, age, aviary_number)
        self.__representative = representative

    @property
    def representative(self):
        return self.__representative

    @representative.setter
    def representative(self, representative):
        self.__representative = representative

    def jump_cat(self) -> str:
        return 'Jump!'

    def sleep_cat(self) -> str:
        return f'{self.__representative} sleep!'


class Monkeys(Zoo):
    """Represents data specific to monkeys."""

    def __init__(self, nickname: str, age: int, aviary_number: int, size: str) -> None:
        """Initializes the attributes of the parent class.Then it initializes the monkeys-specific attri
        Parameters
        ----------
        size: str - the monkeys-specific attributes :'little monkey' or 'big monkey'
            The size of animal.
        """
        super().__init__(nickname, age, aviary_number)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def climb_trees_monkey(self) -> str:
        if self.__size == 'little monkey':
            return 'Climbs trees and hanging on a tree!'
        elif self.__size == 'big monkey':
            return 'Sits and eats a banana!'

    def makes_faces_monkey(self) -> str:
        return 'Makes faces'


def main():
    bear1 = Bear_family('Stepan', 6, 32, 'Brown')
    bear1 = bear1.nickname, bear1.age, bear1.aviary_number, bear1.color, bear1.growl_bear()
    print(bear1)
    bear2 = Bear_family('Glasha', 10, 33, 'white')
    bear2 = bear2.nickname, bear2.age, bear2.aviary_number, bear2.color, bear2.food_bear()
    print(bear2)

    lion = Cat_family('King', 13, 4, 'lion')
    lion = lion.nickname, lion.age, lion.aviary_number, lion.representative, lion.sleep_cat()
    print(lion)
    panther = Cat_family('Bagira', 10, 8, 'panther')
    panther = panther.nickname, panther.age, panther.aviary_number, panther.representative, panther.jump_cat()
    print(panther)

    chimpanzee = Monkeys('Greg', 14, 11, 'big monkey')
    chimpanzee = chimpanzee.nickname, chimpanzee.age, chimpanzee.aviary_number, chimpanzee.climb_trees_monkey()
    print(chimpanzee)
    macaque = Monkeys('Nimble', 4, 11, 'little monkey')
    macaque = macaque.nickname, macaque.age, macaque.aviary_number, macaque.makes_faces_monkey()
    print(macaque)


if __name__ == '__main__':
    main()
