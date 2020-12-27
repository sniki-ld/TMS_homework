# Дан список целых чисел. Подсчитать сколько четных чисел в списке

my_list = [1, 34, 4, 6, 5, 123]

count = 0
i = 0

while i < len(my_list):
    if my_list[i] % 2 == 0:
        count += 1
    i += 1

print(count)

# решение через  for


count = 0

for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        count += 1
        i += 1

print(count)

