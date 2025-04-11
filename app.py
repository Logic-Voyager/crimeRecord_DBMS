from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Crime
from datetime import datetime
from config import Config
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'warning')
            return redirect(url_for('signup'))
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Signup successful, please login.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('crimes'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'info')
    return redirect(url_for('login'))

@app.route('/crimes')
@login_required
def crimes():
    crime_list = Crime.query.all()
    return render_template('crimes.html', crimes=crime_list)

@app.route('/addcrime', methods=['GET', 'POST'])
@login_required
def add_crime():
    if request.method == 'POST':
        description = request.form['description']
        date = request.form['date']
        location = request.form['location']
        crime_type = request.form.get('crime_type')
        severity = request.form.get('severity')
        evidence_file = request.files['evidence']

        filename = None
        if evidence_file and evidence_file.filename != '':
            filename = secure_filename(evidence_file.filename)
            evidence_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_crime = Crime(description=description, date=date, location=location,
                          crime_type=crime_type, severity=severity, evidence=filename)
        db.session.add(new_crime)
        db.session.commit()
        flash("Crime Report Added Successfully", "success")
        return redirect(url_for('crime_list'))

    return render_template('add_crime.html')

if __name__ == '__main__':
    app.run(debug=True)