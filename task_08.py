#  В заданной строке расположить в обратном порядке все слова.
#  Разделителями слов считаются пробелы.

user_str = input().split()

new_str = user_str[::-1]

print(new_str)

# второй способ

user_2 = input().split()

user_2.reverse()

print(list(user_2))
