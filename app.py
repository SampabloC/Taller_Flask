from flask import Flask, render_template#, urlfor
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Nombre de la aplicaciòn dentro de Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/flaskcontacts.db'
db = SQLAlchemy(app)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))

@app.route('/')
def home():
    return render_template('layouts.html')


if __name__ == '__main__':
    app.run(port = 5000, debug = True)
