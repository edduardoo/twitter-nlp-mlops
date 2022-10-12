from flask import Flask, render_template, request, flash
import requests
from config import inf_api_key

app = Flask(__name__)

def call_api(input_value):
    url = 'https://p1r4dch4la.execute-api.us-east-1.amazonaws.com/prod'
  
    inp = int(input_value)
    params = {"Input": [inp]}
  
    headers = {
                'Content-Type': 'application/json',
                'x-api-key': inf_api_key
                }
    response = requests.get(url, json=params, headers=headers)
    data = response.json()

    return "Your prediction is: {}".format(data)

@app.route('/hello')
def hello_geek():
    return '<h1>Hello from Flask & Docker Eduzao</h2>'

@app.route('/', methods=["GET"])
def twitter():
    flash("what's your name dude?")
    return render_template("index.html")

@app.route('/', methods=["POST"])
def search():    
    response = call_api(str(request.form['name_input']))
    flash("Response: " + response)
    return render_template("index.html")

if __name__ == "__main__":
    app.secret_key = 'ajwioefaijwoefa'
    app.config['SESSION_TYPE'] = 'filesystem'

    #sess.init_app(app)

    app.debug = True
    app.run(debug=True)

