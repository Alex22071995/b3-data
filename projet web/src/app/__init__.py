from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask import request
from sqlalchemy.orm import sessionmaker
import os

Session = sessionmaker()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
# db.init_app(app)


def valid_add(rna_id, rna_id_ex, gestion):
    if rna_id != None and rna_id_ex != None and gestion != None:
        return True
    else:
        return False


def valid_del(id):
    if id != None:
        return True
    else:
        return False


class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    rna_id = db.Column(db.String(40), nullable=True)
    rna_id_ex = db.Column(db.String(40), nullable=True)
    gestion = db.Column(db.String(40), nullable=True)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    error = None
    if request.method == 'POST':
        print("lam", request.form["rna_id"])
        if valid_add(request.form['rna_id'], request.form['rna_id_ex'], request.form['gestion']):
            print("hello")
            data = Data(
                rna_id=request.form["rna_id"],
                rna_id_ex=request.form["rna_id_ex"],
                gestion=request.form["gestion"]
            )
            db.session.add(data)
            db.session.commit()
            error = "ok"
        else:
            error = "mauvaise frappe"
    # rna=[]
    # rna.append(request.form['rna_id'],request.form['rna_id_ex'],request.form['gestion'])
    #cursor.execute(""" INSERT INTO rna(rna_id,rna_id_ex,gestion) VALUES(?, ?, ?)""",rna)

    #    print("ici")
    #    pass
    # else:
    #    error = "mauvaise frappe"
    #    print("test")

    return render_template('add.html', error=error)


@app.route('/assos/<id>/delete')
def delete(id):
    error = None

    print("hello", id)
    Data.query.filter(Data.id == id).delete()
    print('passer')
    error = "ok"

    return "test"


@app.route('/assos')
def assos(datas=None):
    datas = Data.query.limit(10).all()
    for data in datas:
        print(f"{data.rna_id}")
    #stmt = select(Data)
    # result=db.session.execute(stmt)
    # for data in result.scalars():
    #    print(f"{data.rna_id}")
    return render_template('assos.html', datas=datas)


@app.route('/graph')
def graph():
    return render_template('graph.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '-_main_-':
    app.run()
