class MyTypeError(Exception):
    def __init__(self, massage='Значение должно быть числом'):
        super(MyTypeError, self).__init__(massage)


class TimeError(Exception):
    def __init__(self, massage='Неверный параметр для значения времени'):
        super(TimeError, self).__init__(massage)


