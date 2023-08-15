from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'

    return wrapper_function

def make_em(function):
    def wrapper_function():
        return f'<em>{function()}</em>'

    return wrapper_function


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test')
@make_bold
@make_em
def test_fun():
    return 'fun!!'


@app.route('/<int:n>')
def guess(n):
    if n > goal_num:
        return f'{n} is too high!'
    elif n < goal_num:
        return f'{n} is too low!'
    else:
        return 'You got it!'


if __name__ == '__main__':
    goal_num = 7
    app.run(debug=True)
