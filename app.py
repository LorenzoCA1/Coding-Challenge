from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from lxml import etree

from DataSearch import SearchPlaintiffs, SearchDefendants

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cases(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	plaintiff = db.Column(db.String(100))
	defendant = db.Column(db.String(100))


@app.route("/")
def home():
    return  render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
	file = request.files['inputFile']

	parser = etree.XMLParser(ns_clean=True)
	root = etree.fromstring(file.read(), parser)
	processedText = "@@ @@".join(root.itertext()).replace("\n", '')

	results = {}

	results['plaintiffs'] = SearchPlaintiffs(processedText)
	results['defendants'] = SearchDefendants(processedText)

	store = Cases(plaintiff= results['plaintiffs'],defendant = results['defendants'])
	db.session.add(store)
	db.session.commit()

	user_data = Cases.query.all()

	return render_template("data.html", user_data = user_data)
	

@app.route("/data")
def data():
	user_data = Cases.query.all()

	return render_template("data.html", user_data = user_data)

if __name__ == '__main__':
  app.run(debug=True)