from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
#db.init_app(app)

class data(db.model):
    __tablename__="data"

    id=db.Column(db.Integer, primary_key=True)
    rna_id=db.Column(db.String(40), nullable=True)
    rna_id_ex=db.Column(db.String(40), nullable=True)
    gestion=db.Column(db.String(40), nullable=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/liste')
def liste():
    return render_template('liste.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)   


if __name__ == '-_main_-':
    app.run()
