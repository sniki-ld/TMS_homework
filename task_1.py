# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.


list_str = ['word', 'by', 'user']

print(list(f'{i} - {string}' for i, string in enumerate(list_str)))


