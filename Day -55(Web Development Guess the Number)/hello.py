from flask import Flask


app = Flask(__name__)


def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper


def make_emphasis(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<em>{result}</em>"
    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<u>{result}</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style = "text-align: center"> Hello, World!</h1> '\
        '<p> This is a paragraph </p> '\
        '<iframe src="https://giphy.com/embed/MDJ9IbxxvDUQM">'


@app.route('/username/<name>/<int:number>')
def greeting(name, number):
    return f"Hello there {name}. Your number is {number}"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(user):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(arg[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"this is {user.name}'s new blog post")


new_user = User("Arif")
new_user.is_logged_in = True
create_blog_post(new_user)
