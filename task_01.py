# Дан текстовый файл, содержащий различные даты.
# Каждая дата - это число, месяц и год. Найти самую раннюю дату.


from datetime import datetime

with open('my_file_task1.txt') as data_file:
    for row in data_file:
        new_list = (data_file.read().split())
    n2_l = []
    for d in new_list:
        n2_l.append(datetime.strptime(d, '%d.%m.%Y'))
    print(min(n2_l))
