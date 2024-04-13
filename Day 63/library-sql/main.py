# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, unique=True, nullable=False)
    review = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Books {self.title}>'

# db.create_all()
# # db.session.add(Books(title="Harry Potter", author="J. K. Rowling", review=9.3))
# # db.session.commit()
# book_harry = Books(title="Harry Potter", author="J. K. Rowling", review=9.3)

# db.session.add(book_harry)
# db.session.commit()
# users = Books.query.all()
# print(book_harry.title)
# print(db.session.query(Books).all())
# # all_books = session.query(Book).all()
# book = Books.query.filter_by(title="Harry Potter").first()
# print(book)