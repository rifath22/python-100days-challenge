from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url
import csv
from csv import writer

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# def url_check(form, field):
#     if not field.startswith("http://"):
#         raise ValidationError('Please enter the valid url')

class CafeForm(FlaskForm):
    coffee_rating_choices = ['✘','☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕']
    wifi_strength_choices = ['✘','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪']
    power_socket_choices = ['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌']
    cafe_name           = StringField('Cafe name', validators=[DataRequired()])
    cafe_location       = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), url()])
    operating_time      = StringField('Operating Time e.g.8 AM', validators=[DataRequired()])
    closing_time        = StringField('Closing Time e.g.5:30 AM', validators=[DataRequired()])
    coffee_rating       = SelectField('Coffee Rating', choices=coffee_rating_choices)
    wifi_strength_rating = SelectField('Wifi Strength Rating', choices=wifi_strength_choices)
    power_socket_rating = SelectField('Power Socket Rating', choices=power_socket_choices)
    submit              = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # print(f"cafe_name: {form.cafe_name.data}")
            # print(f"cafe_location: {form.cafe_location.data}")
            # print(f"operating_time: {form.operating_time.data}")
            # print(f"closing_time: {form.closing_time.data}")
            # print(f"coffee_rating: {form.coffee_rating.data}")
            # print(f"wifi_strength_rating: {form.wifi_strength_rating.data}")
            # print(f"power_socket_rating: {form.power_socket_rating.data}")
            new_cafe = [form.cafe_name.data,form.cafe_location.data,form.operating_time.data,form.closing_time.data,form.coffee_rating.data,form.wifi_strength_rating.data,form.power_socket_rating.data]
            print(new_cafe)
            with open("cafe-data.csv", 'a', newline='', encoding="utf-8") as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(new_cafe)
                f_object.close()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
