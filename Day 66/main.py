from queue import Empty
from unicodedata import name
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as r
import json
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record  
@app.route("/random", methods=["GET"])
def random():
    random_num = r.randint(1,20)
    cafe = Cafe.query.filter_by(id=random_num).first()
    return jsonify(cafe={
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price,
    })

@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafes = Cafe.query.all()
    cafe_list = []
    for cafe in cafes:
        cafe_dict = {"id": cafe.id, "name": cafe.name, "map_url": cafe.map_url,
                     "img_url": cafe.img_url,
                     "location": cafe.location, "has_sockets": cafe.has_sockets,
                     "has_toilet": cafe.has_toilet, "has_wifi": cafe.has_wifi,
                     "can_take_calls": cafe.can_take_calls, "seats": cafe.seats,
                     "coffee_price": cafe.coffee_price}
        cafe_list.append(cafe_dict)
    all_cafes = {"cafes": cafe_list}
    all_cafes_json = jsonify(cafes=all_cafes["cafes"])
    return all_cafes_json

@app.route("/search", methods=["GET"])
def search_cafes():
    cafe = Cafe.query.filter_by(location=request.args.get("loc")).first()
    if not cafe:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    else:
        return jsonify(cafe={
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        })
## HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add():
    name = request.form.get('name')
    print(name)
    new_cafe = Cafe(
        id=int(request.form.get('id')),
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe.."})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    coffee_price    =request.args.get("new_price")
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if not cafe:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = coffee_price
        # db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe.."})

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_price(cafe_id):
    api_key    =    request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe_to_delete = Cafe.query.get(cafe_id)
        if not cafe_to_delete:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe.."})
    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key"), 403

if __name__ == '__main__':
    app.run(debug=True)
