from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grand.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    registration = db.relationship('Registration', backref='visitor', lazy=True)

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    image = db.Column(db.String(100), unique=True, nullable=True)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    image = db.Column(db.String(100), unique=True, nullable=True)


class Callback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@app.route('/')
def index():
    equipment = Equipment.query.all()
    location = Location.query.all()
    return render_template('index.html', equipment=equipment, location=location)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            flash('Email already registered.')
            return redirect(url_for('register'))

        new_user = User(firstname=firstname, lastname=lastname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and (user.password == password):
            session['user_id'] = user.id
            session['username'] = user.firstname
            session['lastname'] = user.lastname
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password.')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/callback', methods=['POST'])
def callback():
    name = request.form['name']
    phone = request.form['phone']
    date = datetime.datetime.now()

    new_comment = Callback(name=name, phone=phone, date=date)
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/registration', methods=['POST'])
def registration():
    name = session['username'] + ' ' + session['lastname']
    phone = request.form['phone']
    date = datetime.datetime.strptime(request.form['date'],'%m/%d/%Y')
    location = request.form['location']
    user_id = session['user_id']

    new_comment = Registration(name=name, phone=phone, date=date, location=location, user_id=user_id)
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
