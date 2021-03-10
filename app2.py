# 2. При переходе на главную страницу должна отобразится страница с приветственной надписью для пользователя.

from flask import Flask, request, render_template

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
    return f'Page user {name}'


if __name__ == '__main__':
    app.run()
