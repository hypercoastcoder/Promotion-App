from flask import Flask, render_template, request, redirect, url_for, send_file
from view import *
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from os import walk
from wtforms.validators import InputRequired
from merge import rename, get_downloadfile_name, get_uploadfile_name, clear_download_data, clear_upload_data
from promotion import promote

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oiuzfgh=)&/(9$%@)'
app.config['UPLOAD_FOLDER'] = 'static/upload/'
app.config['DOWNLOAD_FOLDER'] = 'static/download'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])

def home():
    form = UploadFileForm()

    clear_upload_data(get_uploadfile_name(0))
    clear_upload_data(get_uploadfile_name(0))
    clear_download_data(get_downloadfile_name(0))
    
    if request.method == 'POST':
        if form.validate_on_submit():
            file = form.file.data #grab the file
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file.filename))) #save the file
            filename = next(walk("./static/upload"), (None, None, []))[2]   
        uploaded = rename(filename)
        promote(uploaded)
        return redirect(url_for('download'))
    return render_template("index.html", form=form)

@app.route('/download')
def download():
    clear_upload_data(get_uploadfile_name(0))
    clear_upload_data(get_uploadfile_name(0))
    return render_template('download.html', files=os.listdir('./static/download'))

@app.route('/download/<filename>')
def download_file(filename):
    clear_upload_data(get_uploadfile_name(0))
    clear_upload_data(get_uploadfile_name(0))
    return send_file('static/download/data-delta.csv', filename, as_attachment=True)

if __name__ == ('__main__'):
    app.run(debug=True, port=8000)
