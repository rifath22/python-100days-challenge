from flask import Flask, render_template, request
from forms import LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'rifath secret key'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        login_form.validate_on_submit()
        # print(login_form.email.data)
        # print(login_form.password.data)
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)