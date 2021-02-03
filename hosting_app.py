from flask import Flask, render_template, jsonify, request, send_from_directory
import os
import clipboard as cb
from modules import users, box_files


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "box/"


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/files")
def files():
	all_files = box_files.get_files()
	return render_template("files.html", files=all_files)

@app.route("/done")
def done():
	return render_template("done.html")

@app.route("/upload")
def upload():
	return render_template("upload.html")

@app.route("/login", methods=['POST'])
def login():
	user =  request.form['username']
	password = request.form['password']
	is_user = users.check_user(user, password)
	return jsonify(validate=is_user)

@app.route('/box/<path:filename>', methods=['GET', 'POST'])
def get_link(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)

@app.route("/copy_link", methods=['GET'])
def copy_link():
	link =  request.args.get('link')
	cb.copy(link)
	return jsonify(done=True)
@app.route("/logout")
def logout():
	return render_template("index.html")

app.run(debug=True)
