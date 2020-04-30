from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine('postgresql://ngqctlsfswcnpr:ba7f5dddd401955aaec5b8d0c5a549628479bf6c338efb3ebc77a2d8bd0902ea@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d3hjdgnvdv8c62')
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
