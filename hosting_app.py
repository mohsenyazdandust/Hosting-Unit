from flask import Flask, render_template, jsonify, request
from modules import users

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/files")
def files():
	return render_template("files.html")

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

app.run(debug=True)
