from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def receive_data():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return f"<h1>username: {username}, password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)