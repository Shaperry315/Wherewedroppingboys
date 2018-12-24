from flask import Flask, render_template
import requests 

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/searchresults')
def searchresults():
	requestURL = 'https://api.fortnitetracker.com/v1/profile/pc/Ninja'
	
	req = requests.get(requestURL, headers={"TRN-Api-Key": "0c4877f8-57bd-411e-b04d-027a6ed9fa85"})
	res = req.json()
	# print(res)
	# res = res["epicUserHandle"]
	res = [ res["epicUserHandle"], res["stats"]["p2"]["trnRating"]["percentile"] ]
	return render_template('searchresults.html', res = res)


@app.route('/*')
def home2():
	# return "Hello Meke!"
	return render_template('index.html')