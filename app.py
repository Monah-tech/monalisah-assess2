import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# SQLite configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Create an SQLite database named app.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications for performance


db = SQLAlchemy(app)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

    class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


# Create the database tables
with app.app_context():
    db.create_all()  # Creates the SQLite database and tables

