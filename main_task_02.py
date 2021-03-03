from task_02 import *


def main():
    pars = create_parser()
    url = 'https://cdn.pixabay.com/photo/2021/02/20/18/11/sea-6034191_1280.jpg'

    res = download_file(url)
    dirname = 'images'
    filename = url.split('/')[-1]

    file_write(dirname, filename, res, mode=1)


if __name__ == '__main__':
    main()
