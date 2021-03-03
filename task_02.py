# 2. Написать скрипт, который будет получать на входе: обязательный параметр: адрес изображения в интернете;
# необязательный параметр: флаг, указывающий на поведение в случае, если изображение уже есть в папке:
# 1.перезаписать файл; 2. оставить оба файла(в этом случае к имени нового файла добавить случайно сгенерированную
# строку); 3. не сохранять файл. По умолчанию: перезаписать файл.
# Скрипт должен скачать указанный файл и сохранить его в папку images.
# Покрыть тестами все значимые функции(использовать unittest и doctest).
# Важно: - если папка images не существует - она должна быть создана скриптом автоматически.
#  - имя сохраняемого файла должно соответствовать имени файла в адресе запроса, например:файл
# в интернете https://cdn.pixabay.com/photo/ 2015/03/26/09/40/forest-690058_960_720.jpg должен быть сохранен с именем
# forest-690058_960_720.jpg.
# - предусмотреть проверку на существование введенного адреса.
# - предусмотреть проверку на то, что скачиваемый файл является изображением
# (допустимые форматы изображения - .jpg, .jpeg, .png,.tiff).
# - если размер изображения менее 100кб - скачивать его в один заход, если больше - скачивать порционно.
# Подсказка: чтобы определить тип и размер файла обратите внимание на словарь headers вашего объекта запроса,
# чтобы определить, существует ли запрашиваемая страница - обратите внимание на статус вашего запроса.

import os
import requests
import argparse
import random
import string


def create_parser():
    """Function defines command line parameters.
     Parameters
     ----------
    '-u': str, short name, '--url': str, full name
    This is the address of the image.
    '-e', '--extension': str
    The file extension.
   '-m', '--mode': int
    Flag affecting the behavior of the image, if it already exists in the folder.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True, )
    parser.add_argument('-e', '--extension', choices=['.jpg', '.jpeg', '.png', '.tiff'])
    parser.add_argument('-m', '--mode', type=int, default=1)
    pars = parser.parse_args()
    return pars


def download_file(url):
    """Function for sending a GET request.
    Parameters
    ----------
    url: str
    This is the address of the image.
    """
    res = requests.get(url, stream=True)
    return res


def file_write(dirname, filename, res, mode=1):
    """Function to write a file to a folder"""

    if not isinstance(mode, int):
        raise TypeError('mode must be a number')
    full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dirname)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    if mode == 1:
        with open(f"{full_path}/{filename}", 'wb') as f:
            for chunk in res.iter_content(chunk_size=50000):
                f.write(chunk)
    elif mode == 2:
        random_string = random.sample(string.ascii_letters, 5)
        new_str = f"{(''.join(random_string))}{filename}"
        filename = (''.join(new_str))
        with open(f'{full_path}/{filename}', 'ab') as f:
            for chunk in res.iter_content(chunk_size=50000):
                f.write(chunk)
    else:
        pass
