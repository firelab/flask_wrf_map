import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

app=Flask(__name__)

app.secret_key = "secret key"
global fire_name

@app.route('/')
def WRF():
    global fire_name
    return render_template('wrf.html', fire_name=fire_name)


@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':

        if 'kml[]' not in request.files:
            flash('No file part')
            return edit()

        files = request.files.getlist('kml[]')

        for file in files:
            filename = secure_filename(file.filename)
            file.save('./static/ninja/wrfSim/wrf/'+filename)

        if 'bmp[]' not in request.files:
            flash('No file part')
            return edit()

        files = request.files.getlist('bmp[]')

        for file in files:
            filename = secure_filename(file.filename)
            file.save('./static/ninja/wrfSim/wrf_key/'+filename)

        if 'log[]' not in request.files:
            flash('No file part')
            return edit()

        files = request.files.getlist('log[]')

        for file in files:
            filename = secure_filename(file.filename)
            file.save('./static/ninja/wrfSim/'+filename)

        files = request.files.getlist('zip[]')

        for file in files:
            filename = secure_filename(file.filename)
            file.save('./static/ninja/wrfSim/ninjaout/1km_wrf/'+filename)

        flash('File(s) successfully uploaded')
        return redirect('/edit')

@app.route('/fire_name', methods = ['POST'])
def fire_name():
    global fire_name
    fire_name = request.form['new_name']
    print(fire_name)
    return redirect('/edit')