import requests
import secrets_nyt
from flask import Flask, render_template


NYTimes_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
params = {'api-key':secrets_nyt.api_key}
NYTimes_response = requests.get(NYTimes_url,params)
NYTimes_json = NYTimes_response.json()
# print(NYTimes_json)
title_list = []
# print(NYTimes_json['results'])
for i in range(5):
    title_list.append(NYTimes_json['results'][i]['title'])

app = Flask(__name__)
@app.route('/')
def welcome():
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name = nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    return render_template('headlines.html',name = nm, headlines = title_list)


if __name__ == '__main__':
    app.run(debug=True)