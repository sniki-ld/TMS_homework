# 2.Создать две новые матрицы
# matrix_a, matrix_b случайных чисел размерностью n*m;
# a.создать матрицу равную сумме matrix_a и matrix_b;
# b.создать матрицу равную разности matrix_a и matrix_b;
# c.создать новую матрицу равную matrix_a умноженной на число g.
# g вводится с клавиатуры


from random import randint

my_matrix_a = []
my_matrix_b = []
n = int(input())
m = int(input())

print('Матрица matrix_a:')

for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(1, 10))
    my_matrix_a.append(row)
for i in my_matrix_a:
    print(i)

print('Матрица matrix_b:')

for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(0, 18))
    my_matrix_b.append(row)
for i in my_matrix_b:
    print(i)

