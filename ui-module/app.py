from flask import Flask, render_template, request, flash
import requests
from config import inf_api_key, twitter_api_token
import modules.helper as hp
import tweepy

app = Flask(__name__)
app.secret_key = 'ajwioefaijwoefa'
app.config['SESSION_TYPE'] = 'filesystem'

hardcoded_texts =  ["i hate youtube ads, they are annoying",
             "this data science article is the best ever",
             "this experience has been the worst, want my money back",
             "I think she is a lovely and very good person",
             "I love the color of your products",
             "I hate the color of your products"
             ]
hardcoded_tweets = [{
                    "author_id": "1320537348317339650",
                    "created_at": "2022-10-07T01:03:06.000Z",
                    "edit_history_tweet_ids": [
                        "1578189136204541952"
                    ],
                    "id": "1578189136204541952",
                    "public_metrics": {
                        "like_count": 9494,
                        "quote_count": 126,
                        "reply_count": 17,
                        "retweet_count": 2368
                    },
                    "text": "I love the color of your products"
                },
                {
                    "author_id": "14454670",
                    "created_at": "2022-10-10T13:37:09.000Z",
                    "edit_history_tweet_ids": [
                        "1579466063213113344"
                    ],
                    "id": "1579466063213113344",
                    "public_metrics": {
                        "like_count": 16878,
                        "quote_count": 147,
                        "reply_count": 159,
                        "retweet_count": 756
                    },
                    "text": "I hate the color of your products"
                }]

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

def search_for_tweets(keyword, bearer_token):
    client = tweepy.Client(bearer_token=bearer_token)
    # search query
    query = '"{}" -is:retweet lang:en'.format(keyword)

    tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at', 'public_metrics'], 
                                     sort_order='relevancy', user_fields=['profile_image_url'], 
                                     expansions='author_id', max_results=10)
    return tweets

def match_predictions_texts(texts):
    pass



@app.route('/', methods=["GET"])
def twitter():
    flash("what's your name dude?")
    return render_template("index.html")

@app.route('/', methods=["POST"])
def search():    
    search_term = request.form['name_input']
    tweets = search_for_tweets(search_term, twitter_api_token)
    tweets_df = hp.tweets_to_df(tweets.data)

    predictions = call_api(list(tweets_df['text']))
    tweets_df['sentiment'] = predictions['body']['predictions']
    tweets_df = tweets_df[['sentiment', 'text']]

    return render_template("results.html", df=tweets_df)

if __name__ == "__main__":
    app.run(debug=True)

    

    
    

