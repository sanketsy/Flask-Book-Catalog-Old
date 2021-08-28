from app import db
from datetime import datetime

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The ID is {self.id} and name is {self.name}'


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(80))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Foreign key with id in publication table as primary
    pub_id = db.Column(db.Integer, db.ForeignKey("publication.id"))

    def __init__(self, title, author, avg_rating, format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return f'Title: {self.title} | ' \
               f'Author: {self.author} | ' \
               f'Rating: {self.avg_rating} | ' \
               f'Format: {self.format} | ' \
               f'Image: {self.image} | ' \
               f'num_pages: {self.num_pages} | ' \
               f'pub_id: {self.pub_id}'

