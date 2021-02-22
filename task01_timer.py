

from time import sleep, strftime, gmtime


class MyTimer:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.total_sec()

    def total_sec(self):
        self.total = self.hours * 3600 + self.minutes * 60 + self.seconds
        return self.total

    def my_generator(self):
        while self.total > 0:
            yield f"Осталось времени: {strftime('%H:%M:%S', gmtime(self.total))}"
            self.total -= 1
            sleep(1)

    def my_timer(self):
        for i in MyTimer.my_generator(self):
            print(i)
        return f'ALARM!!!'









