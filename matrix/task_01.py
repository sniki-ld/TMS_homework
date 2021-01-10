# 1. Создать матрицу случайных чисел от a до b, размерность матрицы n*m;
# a. найти максимальный элемент матрицы;
# b. найти минимальный минимальный матрицы;
# c. найти сумму всех элементов матрицы;
# d. найти индекс ряда с максимальной суммой элементов;
# e. найти индекс колонки с максимальной суммой элементов;
# f. найти индекс ряда с минимальной суммой элементов;
# g. найти индекс колонки с минимальной суммой элементов;
# h. обнулить все элементы выше главной диагонали;
# i. обнулить все элементы ниже главной диагонали.

# 1. Создать матрицу случайных чисел от a до b, размерность матрицы n*m;

from random import randint

my_matrix = []

n = int(input())
m = int(input())
a = int(input())
b = int(input())

for i in range(n):
    temp_list = []
    for j in range(m):
        temp_list.append(randint(a, b))
    my_matrix.append(temp_list)
for i in my_matrix:
    print(i)
    
# a. найти максимальный элемент матрицы;

maximum = 0
for i in range(n):
    for j in range(m):
        if my_matrix[i][j] > maximum:
            maximum = my_matrix[i][j]

print(f'максимальный элемент матрицы = {maximum}')

# b. найти минимальный минимальный матрицы;

minimum = a
for i in range(n):
    for j in range(m):
        if my_matrix[i][j] == minimum:
            minimum = my_matrix[i][j]

print(f'минимальный элемент матрицы = {minimum}')
