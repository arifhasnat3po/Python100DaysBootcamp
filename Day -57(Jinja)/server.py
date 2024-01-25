from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route('/')
def home():
    current_datetime = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_datetime)


@app.route('/guess/<name>')
def guess(name):
    current_datetime = datetime.datetime.now().year
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']
    return render_template('guess.html', name=name, age=age, gender=gender, year=current_datetime)


@app.route(('/blog/<num>'))
def get_blog(num):
    response = requests.get("https://api.npoint.io/131ba90b5fa5a27d1c68")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
