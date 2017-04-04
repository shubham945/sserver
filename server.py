#!/usr/bin/env python
from flask import *
import os
import json
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./upload"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "shubham"

def allowed_file(filename): # check if current file is allowed or not
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def getIndex():
    return send_from_directory("www", "index.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# To upload file from raspberry pi use following code
# with open('test1.jpg', 'rb') as f : r = requests.post("http://localhost:2121/upimage", files={'file' : f})


@app.route('/upimage', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect('upload.html')
            return abort(404)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            # return redirect('upload.html')
            return abort(404)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file', filename=filename))
            return "success"

@app.route("/get-images")
def getImages():
    imageList = os.listdir(UPLOAD_FOLDER)
    for indexNo in range(len(imageList)):
        imageList[indexNo] = "/uploads/"+imageList[indexNo]
    tmpList = []
    while len(imageList) > 0:
        tmpList.append(imageList[:4])
        imageList = imageList[4:]
    imageList = tmpList
    return make_response(json.dumps(imageList))

@app.route("/<path:path>")
def getFiles(path):
    return send_from_directory("www", path)

@app.route("/login", methods=['POST'])
def checkLogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "shubham" and password == "singh":
            return send_from_directory("./", "home.html")
        else:
            return "Wrong Credentials"


if __name__ == "__main__":
    app.run(port=2121, debug=True)
