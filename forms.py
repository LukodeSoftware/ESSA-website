from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TelField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=50)
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    phone = TelField('Phone', validators=[
        DataRequired(),
        Length(min=9, max=15)
    ])
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=10, max=1000)
    ])
