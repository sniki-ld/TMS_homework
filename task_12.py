# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

for key in my_dict:
    new_key = key + str(len(key))
    print({new_key: my_dict[key]}, end=' ') # первое решение

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

keys = list(my_dict.keys())
# print(keys)
len_keys = len(keys)

i = 0

while i < len(keys):
    my_new_keys = f'{keys[i]}{len(keys[i])}'
    my_dict[my_new_keys] = my_dict.pop(keys[i])
    i += 1

print(my_dict)

# решение с for

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

keys = list(my_dict.keys())

len_keys = len(keys)
i = 0

for key in range(len_keys):
    my_new_keys = f'{keys[i]}{len(keys[i])}'
    my_dict[my_new_keys] = my_dict.pop((keys[i]))
    i += 1

print(my_dict)
