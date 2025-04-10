from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import config

app = Flask(__name__)
app.config.from_object(config)

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM crimes")
    crimes = cur.fetchall()
    cur.close()
    return render_template('index.html', crimes=crimes)

@app.route('/add_crime', methods=['GET', 'POST'])
def add_crime():
    if request.method == 'POST':
        description = request.form['description']
        location = request.form['location']
        date = request.form['date']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO crimes(description, location, date) VALUES(%s, %s, %s)",
                    (description, location, date))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    return render_template('add_crime.html')

@app.route('/add_suspect', methods=['GET', 'POST'])
def add_suspect():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, description FROM crimes")
    crimes = cur.fetchall()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        crime_id = request.form['crime_id']
        cur.execute("INSERT INTO suspects(name, age, crime_id) VALUES(%s, %s, %s)",
                    (name, age, crime_id))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    
    cur.close()
    return render_template('add_suspect.html', crimes=crimes)

if __name__ == '__main__':
    app.run(debug=True)



