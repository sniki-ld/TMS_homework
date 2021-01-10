#  Дан список целых чисел.
# Создать новый список, каждый элемент которого равен
# исходному элементу умноженному на -2

my_list = [2, 8, 7, 9, 12]

new_list = [(i * -2) for i in my_list]

print(new_list)

# решение через  while

len_list = len(my_list)
i = 0
new_list = []
while i < len_list:
    new_list.append(my_list[i] * (-2))
    i += 1

print(new_list)

# решение через  for

my_list = [2, 8, 7, 9, 12]

len_list = len(my_list)
new_list = []
for i in my_list:
    new_list.append(i * -2)

print(new_list)
