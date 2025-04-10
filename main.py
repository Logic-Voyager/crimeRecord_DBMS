from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy

# MY db connection
local_server= True
app = Flask(__name__)


app.run(debug=True)    


# username=current_user.username