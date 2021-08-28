from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField("Enter new title: ", validators=[DataRequired()])
    format = StringField("Enter new format: ", validators=[DataRequired()])
    num_pages = StringField("Enter num_pages: ", validators=[DataRequired()])
    update = SubmitField("Update")


class CreateBookForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    author = StringField("Author: ", validators=[DataRequired()])
    avg_rating = FloatField("Avg Rating: ", validators=[DataRequired()])
    format = StringField("Format: ", validators=[DataRequired()])
    image = StringField("Image: ", validators=[DataRequired()])
    num_page = IntegerField("Num of pages: ", validators=[DataRequired()])
    pub_id = IntegerField("Publisher ID: ", validators=[DataRequired()])
    create = SubmitField("Create book")
