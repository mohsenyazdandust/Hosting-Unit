from flask import Flask 
from flask import render_template

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
app.run(debug=True)
