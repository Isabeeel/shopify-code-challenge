import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static'

def validate_image(stream):
    header = stream.read(512)  # 512 bytes for a header
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

#get index page
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

#submit image
@app.route('/', methods=['POST'])
def upload_files():
    for uploaded_file in request.files.getlist('file'):
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if (file_ext not in app.config['UPLOAD_EXTENSIONS']) or (file_ext != validate_image(uploaded_file.stream)):
                return "Invalid image", 400
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index'))

#list submitted image
@app.route("/uploads/<filename>",methods=["GET"])
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


if __name__ == "__main__":
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(debug=True, port=8080)
