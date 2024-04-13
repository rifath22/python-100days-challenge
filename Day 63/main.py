from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBXox7C0sKR6b'
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

all_books = []

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, unique=True, nullable=False)
    review = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Books {self.title}>'

class BookForm(FlaskForm):
    book_name     = StringField('Book name', validators=[DataRequired()])
    book_author   = StringField('Book Author', validators=[DataRequired()])
    rating        = StringField('Rating', validators=[DataRequired()])
    submit        = SubmitField('Submit')

db.create_all()

@app.route('/')
def home():
    library = db.session.query(Books).all()
    print(f"library: {library}")
    return render_template("index.html", book_list=library)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            db.session.add(Books(title=form.book_name.data, author=form.book_author.data, review=form.rating.data))
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Books.query.get(book_id)
        book_to_update.review = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)

if __name__ == "__main__":
    app.run(debug=True)

