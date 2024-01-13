from flask import Flask

import random

RANDOM_NUMBER = random.randint(3, 10)
print(RANDOM_NUMBER)
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> "Guess a number between 0 and 9"</h1>'\
        '<iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" frameBorder="0" </iframe>'


@app.route('/<int:number>')
def is_valid_number(number):
    global RANDOM_NUMBER
    if RANDOM_NUMBER == number:
        return f'<h1 style="color: green" > Congratulations! Your guess {number} is correct.</h1>'\
            '<iframe src="https://giphy.com/embed/4T7e4DmcrP9du" width="458" height="480" frameBorder="0"</iframe>'
    elif RANDOM_NUMBER < number:
        return f'<h1 style="color: purple">Your guess {number} is too high.</h2>'\
            '<iframe src="https://giphy.com/embed/3o6ZtaO9BZHcOjmErm" width="480" height="453" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'

    else:
        return f'<h1 style="color: red"> Your guess {number} is too low.</h2>'\
            '<iframe src="https://giphy.com/embed/jD4DwBtqPXRXa" width="384" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
