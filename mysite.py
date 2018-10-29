from flask import Flask, render_template, request
from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__)

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        ''' Add entry to the database '''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name, email, phone, message, datetime.now())



    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')


app.run(debug=True)
