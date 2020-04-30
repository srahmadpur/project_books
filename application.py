from flask import Flask , jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://ngqctlsfswcnpr:ba7f5dddd401955aaec5b8d0c5a549628479bf6c338efb3ebc77a2d8bd0902ea@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d3hjdgnvdv8c62'
app.config["SESSION_PERMANENT"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_TYPE"] = "filesystem"
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "books"
    isbn = db.Column(db.String, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)




@app.route("/")
def index():
    return render_template('index.html', title='Home')


@app.route("/api/<string:isbn>")
def isbn_api(isbn):
    """Return details about a single flight."""
    # Make sure flight exists.
    book = Book.query.get(isbn)
    if book is None:
        return jsonify({"KeyError": "Invalid ISBN number"}), 422
    else:    
        return jsonify({
                "isbn": book.isbn,
                "title": book.title,
                "author": book.author,
                "year": book.year
            })