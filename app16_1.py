# 1. Создать сайт, содержащий 3 страницы: главную, страницу со списком пользователей,
# детальную страницу пользователя.
# 2. При переходе на главную страницу должна отобразится страница с приветственной надписью для пользователя.
# 3.При переходе на страницу со списком пользователей - должна отобразится страница,
#  где перечислены пользователи в виде ссылок.
#  При клике на любую из них должен осуществиться переход на детальную страницу пользователя.
# 4.При переходе на детальную страницу пользователя должна открыться страница с приветствием пользователя
# по его имени и текущее время с указанием утро это, день, вечер или ночь
# (6 - 12 утро, 12 - 16 день, 16 - 0 вечер, 0 - 6 ночь), например: Привет, Жора! Сейчас 23:00:32. Приятного вечера!

from flask import Flask, request, render_template
from datetime import datetime
from times_of_day import times_of_day

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('hello_home.html', name='User')


@app.route('/list_users/')
def list_users():
    users = ['Viktor', 'Petr']
    name_dict = {'users': users}
    return render_template('list_users.html', **name_dict)


@app.route('/user/<name>/')
def user_name(name):
    user = name
    hi = times_of_day()
    temp_dict = {'user': user, 'time': datetime.strftime(datetime.now(), " %H:%M:%S"), 'hi': hi}
    return render_template('hello_user.html', **temp_dict)


if __name__ == '__main__':
    app.run()
