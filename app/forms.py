from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class BrandSubmitForm(FlaskForm):
    brand = StringField("Brand")
    submit = SubmitField("Submit")