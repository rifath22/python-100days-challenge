from flask import Flask, render_template
import random

app = Flask(__name__)
random_number = random.randint(0,9)
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<int:post_id>")
def is_equal(post_id):
    if  post_id == random_number:
        return  "<h1 style='color: green'>You're right:</h1>" \
                '<img src="static/equal.webp" alt="gif images">'
    elif post_id > random_number:
        return  "<h1 style='color: red'>Too high, try again!</h1>" \
                '<img src="static/high.webp" alt="gif images">'
    elif post_id < random_number:
        return  "<h1 style='color: purple'>Too low, try again!</h1>" \
                '<img src="static/low.webp" alt="gif images">'


if __name__ == "__main__":
    app.run(debug=True)