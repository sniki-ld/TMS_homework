#!/usr/bin/python3.8
#  Написать программу таймер.
# Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
# После программа начинает обратный отсчет выводя оставшееся время.
# Программа должна хранить файл логирования с информацией о том
# кто запускал программу и когда.
# Пример :
# 00:00:03
# 00:00:02
# 00:00:01
# ALARM!!!

import os
import argparse
from datetime import datetime
from task01_timer import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)

    args = parser.parse_args()

    gen = MyTimer(0, 0, 5)
    print(gen.my_timer())
    current_datetime = datetime.now()
    file_path = os.path.realpath(__file__)
    dir_name = os.path.dirname(file_path)
    with open(f'{ dir_name}/task_01.txt', 'a') as my_file:
        my_file.write(f'{args.first_name} {args.last_name}| {current_datetime} \n')


if __name__ == '__main__':
    main()


