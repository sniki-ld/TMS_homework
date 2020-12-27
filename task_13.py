# Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример:12345 -> 23451

my_list = [1, 6, 9, 11, 13]
new_list = my_list[1:]
new_list.append(my_list[0])
print(new_list)