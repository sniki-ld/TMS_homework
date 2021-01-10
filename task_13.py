# Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример:12345 -> 23451

my_list = [1, 6, 9, 11, 13]
new_list = my_list[1:]
new_list.append(my_list[0])
print(new_list)

# решение с while

my_list = [1, 6, 9, 11, 13]

len_my_list = len(my_list)

new_list = []
i = 0
while i < len_my_list:
    if i + 1 == len_my_list:  # если след элемент - это последний элемент
        new_list.append(my_list[0])
    else:
        new_list.append(my_list[i + 1])
    i += 1

print(new_list)

# решение с for

my_list = [1, 6, 9, 11, 13]

new_list = []

for i in range(1, len(my_list)):
    new_list.append(my_list[i])
new_list.append(my_list[0])

print(new_list)
