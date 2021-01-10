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

# c. найти сумму всех элементов матрицы;

sum_my_matrix = 0
for i in range(n):
    for j in range(m):
        sum_my_matrix += my_matrix[i][j]

print(f'сумма всех элементов матрицы = {sum_my_matrix}')

# d. найти индекс ряда с максимальной суммой элементов;

sum_row_max = 0
ind_row_max = 0
for i in range(n):
    sum_row_current = 0
    for j in range(m):
        sum_row_current += my_matrix[i][j]
        if sum_row_current > sum_row_max:
            sum_row_max = sum_row_current
            ind_row_max = i

print(f'индекс ряда с максимальной суммой элементов = {ind_row_max}')

# e. найти индекс колонки с максимальной суммой элементов;

sum_colum_max = 0
ind_colum_max = 0

for j in range(m):
    sum_colum_tec = 0
    for i in range(n):
        sum_colum_tec = sum_colum_tec + my_matrix[i][j]
        if sum_colum_tec > sum_colum_max:
            sum_colum_max = sum_colum_tec
            ind_colum_max = j
print(f'индекс колонки с максимальной суммой элементов = {ind_colum_max}')

# f. найти индекс ряда с минимальной суммой элементов

sum_row_min = sum_row_max
ind_row_min = 0

for i in range(n):
    sum_row_tmin = 0
    for j in range(m):
        sum_row_tmin = sum_row_tmin + my_matrix[i][j]
    if sum_row_tmin < sum_row_min:
        sum_row_min = sum_row_tmin
        ind_row_min = i

print(f'индекс ряда с минимальной суммой элементов = {ind_row_min}')



