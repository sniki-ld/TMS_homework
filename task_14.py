# Составить список чисел Фибоначчи содержащий 15 элементов.
# (подсказка: числа Фибоначчи - последовательность,
# в которой первые два числа равны либо 1 и 1, а каждое последующее число равно
# сумме двух предыдущих чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2

i = 0
numb_1 = 1
numb_2 = 1
new_list = []

while i < 15:
    numb_3 = numb_1 + numb_2
    new_list.append(numb_3)
    numb_1 = numb_2
    numb_2 = numb_3
    i += 1

print(new_list)


# пример преподавателя

fib_list = [1, 1]

while len(fib_list) < 15:
    fib_list.append(fib_list[-1] + fib_list[-2])


print(fib_list)

# решение с for

list_fib = [1, 1]

for i in range(3, 16):
    list_fib.append(list_fib[-1] + list_fib[-2])


print(list_fib)
