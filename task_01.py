# 1. Написать модуль, содержащий 12 функций по переводу:
# Примечание: функция принимает на вход число и возвращает
# конвертированное число

# 1.1.Дюймы в сантиметры


def inches_centimeters(number):
    number *= 2.54
    return number
    
    
# 1.2.Сантиметры в дюймы


def centimeters_inches(number):
    number /= 2.54
    return round(number, 2)


# 1.3.Мили в километры


def miles_kilometers(number):
    number *= 1.60934
    return round(number, 2)
    
    
# 1.4.Километры в мили


def kilometers_miles(number):
    number /= 1.60934
    return round(number, 2)


# 1.5.Фунты в килограммы


def lb_kg(number):
    number /= 2.20462
    return round(number, 2)


# 1.6.Килограммы в фунты


def kg_lb(number):
    number *= 2.20462
    return round(number, 2)


# 1.7.Унции в граммы


def oz_grams(number):
    number *= 28.3495
    return round(number, 2)


# 1.8.Граммы в унции


def grams_oz(number):
    number *= 0.035274
    return round(number, 2)


# 1.9.Галлон в литры


def gallons_liters(number):
    number *= 3.78541
    return round(number, 2)


# 1.10.Литры в галлоны


def liters_gallons(number):
    number /= 3.78541
    return round(number, 2)
    
    
# 1.11.Пинты в литры


def pints_liters(number):
    number /= 2.11338
    return round(number, 2)


# 1.12.Литры в пинты


def liters_pints(number):
    number *= 2.11338
    return round(number, 2)


# 2. Написать программу, со следующим интерфейсом:
# пользователю предоставляется на выбор 12 вариантов перевода
# (описанных в первой задаче). Пользователь вводит цифру от одного
# до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат.
# Использовать функции из первого задания. Программа должна быть
# в бесконечном цикле. Код выхода из программы - “0.
# Примечание: программа выполняется только в том случае,
# если модуль работает в основном потоке.


def main():
    print('To end the program, enter numeral = 0')
    
    operation_conv = ['Дюймы в сантиметры', 'Сантиметры в дюймы', 'Мили в километры', 'Километры в мили', 'Фунты в килограммы', 'Килограммы в фунты', 'Унции в граммы', 'Граммы в унции', 'Галлон в литры', 'Литры в галлоны', 'Пинты в литры', 'Литры в пинты']
    
    for idx, elem in enumerate(operation_conv, 1):
        print(idx, elem)
    while 1:
        numeral = int(input('Enter a numeral from 1 to 12: '))
        if numeral == 0:
            break
        number = int(input('Enter the number to convert: '))
        if numeral == 0:
            break
        if numeral == 1:
            print(inches_centimeters(number))
        if numeral == 2:
            print(centimeters_inches(number))
        if numeral == 3:
            print(miles_kilometers(number))
        if numeral == 4:
            print(kilometers_miles(number))
        if numeral == 5:
            print(lb_kg(number))
        if numeral == 6:
            print(kg_lb(number))
        if numeral == 7:
            print(oz_grams(number))
        if numeral == 8:
            print(grams_oz(number))
        if numeral == 9:
            print(gallons_liters(number))
        if numeral == 10:
            print(liters_gallons(number))
        if numeral == 11:
            print(pints_liters(number))
        if numeral == 12:
            print(liters_pints(number))


if __name__ == '__main__':
    main()
