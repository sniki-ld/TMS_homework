# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

for key in my_dict:
    new_key = key + str(len(key))
    print({new_key: my_dict[key]}, end=' ')
