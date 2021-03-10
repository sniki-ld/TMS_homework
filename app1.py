# 1. Создать сайт, содержащий 3 страницы: главную, страницу со списком пользователей,
# детальную страницу пользователя.
from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Home page'


@app.route('/list_users/')
def list_users():
    return f'List users: Viktor, Elena'


@app.route('/user/<name>/')
def user_name(name):
    return f'Page user {name}'


if __name__ == '__main__':
    app.run()
