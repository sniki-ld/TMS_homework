from datetime import datetime


def times_of_day() -> str:
    """ This is a function for greeting, depending on the time of day."""

    now = datetime.now().time()
    if 0 <= int(now.hour) < 6:
        return f'Доброй ночи!'
    elif 6 <= int(now.hour) < 12:
        return f'Доброе утро!'
    elif 12 <= int(now.hour) < 16:
        return f'Добрый день!'
    else:
        return f'Добрый вечер!'


# if __name__ == '__main__':
#     times_of_day()
