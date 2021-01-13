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

