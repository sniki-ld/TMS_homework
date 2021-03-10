#  При переходе на страницу со списком пользователей - должна отобразится страница,
#  где перечислены пользователи в виде ссылок.
#  При клике на любую из них должен осуществиться переход на детальную страницу пользователя.

from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('hello_home.html', name='Viktor')


@app.route('/list_users/')
def list_users():
    temp_dict = {'Viktor': ' http://127.0.0.1:5000/user/Victor/', 'Elena': ' http://127.0.0.1:5000/user/Elena/'}
    return render_template('list_users.html', **temp_dict)


@app.route('/user/<name>/')
def user_name(name):
    return f'Page user {name}'


if __name__ == '__main__':
    app.run()
