from flask import *
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "shubham"

@app.route("/")
def getIndex():
    return send_from_directory("www","index.html")

@app.route("/<path:path>")
def getFiles(path):
    return send_from_directory("www", path)

@app.route("/login", methods=['POST'])
def checkLogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username=="shubham" and password=="singh":
            return "Successfully Logged IN"
        else:
            return "Wrong Credentials"

@app.route("/upimage",methods=['POST', 'GET'])
def uploadImage():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No File Part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('uploaded_file', filename=filename))
        return '''
        <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
        '''
    else:
        return "upimage url called"

if __name__ == "__main__":
    app.run(port=8080, debug=True)
