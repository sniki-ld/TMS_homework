# При переходе на детальную страницу пользователя должна открыться страница с приветствием пользователя
# по его имени и текущее время с указанием утро это, день, вечер или ночь
# (6 - 12 утро, 12 - 16 день, 16 - 0 вечер, 0 - 6 ночь), например: Привет, Жора! Сейчас 23:00:32. Приятного вечера!

from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('hello_home.html', name='Viktor')


@app.route('/list_users/')
def list_users():
    return 'List users'


@app.route('/user/<name>/')
def user_name(name):
    temp_dict = {'name': 'Viktor', 'time': datetime.now().strftime("%H:%M:%S")}
    return render_template('hello_user.html', **temp_dict)


if __name__ == '__main__':
    app.run()
