# Написать генератор песенки «TEN green bottles hanging on the wall».
# В песенке вместо цифр должны быть именно слова, обозначающие цифры,
# т.е. TEN, NINE, EIGHT, etc
# Песенка состоит из серии куплетов вот таких:
# <количество> green bottles hanging on the wall,
# <количество> green bottles hanging on the wall,
# And if one green bottle should accidentally fall,
# There‛ll be...
# <пустая строка>
# <количество - 1> green bottles hanging on the wall...
# И так до тех пор, пока не закончатся бутылки. Когда они закончились,
# то песенка должна закончится фразой: NO green bottles hanging on the wall!

numeral = ['TEN', 'NINE', 'EIGHT', 'SEVEN', 'SIX', 'FIVE', 'FOUR', 'THREE', 'TWO', 'ONE']

for i in numeral:
    b = f"{i} {'green bottles hanging on the wall...'}"
    print(b)
    print(b)
    print('And if one green bottle should accidentally fall,')
    print('There‛ll be...')
    print()
print('NO green bottles hanging on the wall!')

