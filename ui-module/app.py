from flask import Flask, render_template, request, flash
import requests
from config import inf_api_key, twitter_api_token
import modules.helper as hp
import tweepy

app = Flask(__name__)
app.secret_key = 'ajwioefaijwoefa'
app.config['SESSION_TYPE'] = 'filesystem'

def call_api(texts):
    url = 'https://p1r4dch4la.execute-api.us-east-1.amazonaws.com/prod'
      
    params = {"texts": texts} 
  
    headers = {
                'Content-Type': 'application/json',
                'x-api-key': inf_api_key
                }
    response = requests.get(url, json=params, headers=headers)
    data = response.json()    

    return data


@app.route('/', methods=["GET"])
def twitter():
    flash("what's your name dude?")
    return render_template("index.html")

@app.route('/', methods=["POST"])
def search():    
    search_term = request.form['name_input']
    tweets = hp.search_for_tweets(search_term, twitter_api_token)
    tweets_df = hp.tweets_to_df(tweets.data)

    predictions = call_api(list(tweets_df['text']))
    tweets_df['sentiment'] = predictions['body']['predictions']
    tweets_df = tweets_df[['sentiment', 'text', 'like_count']]

    return render_template("results.html", df=tweets_df)

if __name__ == "__main__":
    app.run(debug=True)

    

    
    

