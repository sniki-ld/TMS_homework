# Дано число. Найти сумму и произведение его цифр.

number = int(input('Enter number: '))

sum_number = 0
pr_number = 1

while number > 0:
    num_last = number % 10
    sum_number += num_last
    pr_number *= num_last
    number = number // 10

print(f'Sum of all digits of the number: {sum_number}')
print(f'Producing of all digits of the number: {pr_number}')
