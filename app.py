from flask import Flask, render_template, request
import sqlite3

# This line creates the flask app
app = Flask(__name__)

@app.route('/')
def Map():

    fire_name = "Moose Fire"
    return render_template('wrf.html', fire_name=fire_name)