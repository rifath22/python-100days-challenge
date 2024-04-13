from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

my_email = os.getenv('my_email')
password = os.getenv('my_email_password')
another_email_address = os.getenv('another_email_address')

posts = requests.get("https://api.npoint.io/ed99320662742443cc5b").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        message_content = f'''
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        '''
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=another_email_address, 
                                msg=f"Subject:Flask Website Message\n\n {message_content}")
        return render_template('contact.html', msg_sent= True)
    return render_template('contact.html', msg_sent= False)

if __name__ == "__main__":
    app.run(debug=True)
