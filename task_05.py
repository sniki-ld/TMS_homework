# В списке целых случайных чисел с количеством элементов n
# определить максимальное число и заменить им все четные по значению элементы.

from random import randint

n = int(input())  # количество элементов списка

my_list = []
for i in range(n):
    my_list.append(randint(1, 100))  # формируем список случайных чисел

print(my_list)

max_my_list = max(my_list)

print(max_my_list)

for elem in range(len(my_list)):
    if my_list[elem] % 2 == 0:
        my_list[elem] = max_my_list
print(my_list)
