from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

themoviedb_API_key = os.getenv('themoviedb_API_key')
SEARCH_MOVIE_URL = 'https://api.themoviedb.org/3/search/movie'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(10000))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(300))
    img_url = db.Column(db.String(300))

    def __repr__(self):
        return f'<Movie {self.title}>'

#########################  Run Only during First Run       ######################
# db.create_all()
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# db.session.add(new_movie)
# db.session.commit()

class ReviewEditForm(FlaskForm):
    rating  = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review  = StringField('Your Review', validators=[DataRequired()])
    submit  = SubmitField('Done')

class AddMovie(FlaskForm):
    title  = StringField('Movie Title', validators=[DataRequired()])
    submit  = SubmitField('Add Movie')

def search_movie(title):
    parameters = {
    "api_key": themoviedb_API_key,
    "language": "en-US",
    "query": title,
    "page": 1
    }
    response = requests.get(SEARCH_MOVIE_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    return data['results']

def find_movie_by_id(id):
    parameters = {
    "api_key": themoviedb_API_key,
    "language": "en-US"
    }
    FIND_MOVIE_URL = f"https://api.themoviedb.org/3/movie/{id}"
    response = requests.get(FIND_MOVIE_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)
    movie_info = {}
    movie_info['title'] = data['title']
    movie_info['img_url'] = f"https://image.tmdb.org/t/p/original/{data['poster_path']}"
    movie_info['year'] = data['release_date'].split('-')[0]
    movie_info['description'] = data['overview']
    return movie_info

@app.route("/")
def home():
    movies_list = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    for i in range(len(movies_list)):
        movies_list[i].ranking = len(movies_list) - i
    db.session.commit()
    print(movies_list)
    return render_template("index.html", movies_list=movies_list)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = ReviewEditForm()
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)
    if request.method == "POST":
        if form.validate_on_submit():
            movie_selected.rating = float(form.rating.data)
            movie_selected.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", movie=movie_selected, form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovie()
    if request.method == "POST":
        if add_form.validate_on_submit():
            similar_movies_list = search_movie(add_form.title.data)
            return render_template("select.html", movies_list=similar_movies_list)
    return render_template("add.html", form=add_form)

@app.route("/find", methods=["GET", "POST"])
def find():
    movie_api_id = request.args.get("id")
    movie_metadata = find_movie_by_id(movie_api_id)
    print(movie_metadata)
    new_movie = Movie(
        title=movie_metadata['title'],
        year=movie_metadata['year'],
        description=movie_metadata['description'],
        img_url=movie_metadata['img_url']
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
