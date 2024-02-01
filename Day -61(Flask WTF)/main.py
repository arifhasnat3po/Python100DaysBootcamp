# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField

# app = Flask(__name__)
# # Set a secret key for CSRF protection
# app.config['SECRET_KEY'] = 'some secret string'


# class LoginForm(FlaskForm):
#     email = StringField('Email', render_kw={"size": 30})
#     password = PasswordField('Password', render_kw={"size": 30})


# @app.route("/")
# def home():
#     return render_template('index.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         print(f'Email: {form.email.data}, Password: {form.password.data}')

#     return render_template('login.html', form=form)


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
