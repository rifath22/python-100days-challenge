from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)

def get_gender(username):
    genderize_url = f'https://api.genderize.io/?name={username}'
    genderize_api_response = requests.get(genderize_url)
    genderize_api_response.raise_for_status()
    genderize_api_data = genderize_api_response.json()
    gender = genderize_api_data["gender"]
    return gender

def get_age(username):
    agify_url = f'https://api.agify.io/?name={username}'
    agify_api_response = requests.get(agify_url)
    agify_api_response.raise_for_status()
    agify_api_data = agify_api_response.json()
    age = agify_api_data["age"]
    return age

@app.route('/')
def home():
    random_number = random.randint(0,10)
    today = datetime.now()
    str_today = datetime.strftime(today, '%Y')
    your_name = "Azas"
    return render_template('index.html', num=random_number, current_year=str_today, name=your_name)

@app.route('/guess/<username>')
def user_name_age(username):
    gender = get_gender(username)
    age = get_age(username)
    return render_template('guess.html', name=username.title(), gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)


