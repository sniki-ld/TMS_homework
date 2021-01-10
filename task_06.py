# Задан целочисленный список c n случайных элементов.
# Определить количество участков списка, на котором элементы монотонно возрастают
# (каждое следующее число больше предыдущего).

from random import randint

n = int(input())
my_list = []

for numb in range(n):
    my_list.append(randint(1, 100))

print(my_list)

counter = 0

for elem in range(len(my_list)-1):
    if my_list[elem + 1] > my_list[elem]:
        counter += 1
print(counter)
