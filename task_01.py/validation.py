from exeptions import MyTypeError, TimeError


def valid_value(hours, minutes, seconds):
    if isinstance(hours, int):
        return True
    if isinstance(minutes, int):
        return True
    if isinstance(seconds, int):
        return True
    else:
        raise MyTypeError


def valid_time(hours, minutes, seconds):
    if hours < 0 or hours > 24:
        raise TimeError
    if minutes < 0 or minutes > 60:
        raise TimeError
    if seconds < 0 or seconds > 60:
        raise TimeError
    else:
        return True
