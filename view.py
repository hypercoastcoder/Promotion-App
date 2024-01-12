from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


views = Blueprint(__name__, "views")

@views.route("/", methods=['GET', 'POST'])
@views.route("/home", methods=['GET', 'POST'])
@views.route("/download", methods=['GET'])

def home():
    return render_template("index.html") #,form=form)

def download():
    return render_template("download.html")