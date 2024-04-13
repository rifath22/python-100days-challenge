from flask import Flask, render_template
import requests
from datetime import datetime
app = Flask(__name__)
now = datetime.now()
d = now.strftime("%d %B, %Y")

response = requests.get(url='https://api.npoint.io/ed99320662742443cc5b')
response.raise_for_status()
data = response.json()

@app.route("/")
def home():
    return render_template('index.html', posts=data, author='Rifath', date=d)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    for single_post in data:
        print(f"single_post: {single_post}")
        if single_post['id'] == id:
            return render_template("post.html", posts=single_post, author='Rifath', date=d)

if __name__ == "__main__":
    app.run(debug=True)