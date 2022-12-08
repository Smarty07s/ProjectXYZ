from flask import Flask, render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
from mod import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def create_new_db(app=app,db=db):
    with app.app_context():
        db.create_all()

class data(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    vote = db.Column(db.String(500), primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'{self.sno} - {self.title}'

@app.route('/_stuff', methods = ['GET','POST'])
def stuff():
    return jsonify(result={'count':5})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create',methods = ['GET','POST'])
def form():

    return render_template('form.html')


@app.route('/created',methods = ['GET','POST'])
def create():
    create_new_db()
    return render_template('admin.html')
    
@app.route('/admin',methods=['GET','POST'])
def admin():
    
    return render_template('admin.html')

if __name__=="__main__":
    app.run(debug=True)
