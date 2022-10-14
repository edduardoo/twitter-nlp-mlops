import pandas as pd

def tweets_to_df(tweets, type="tweepy"): # during tests I used a hardcoded set of tweets, so I change 'type' to anything else
    results = pd.DataFrame()
    for tweet in tweets:
        if type=="tweepy":
            tweet = tweet.data
        
        tweet = tweet
        metrics = tweet['public_metrics']    
        keys, values = zip(*metrics.items())
        df = pd.DataFrame(tweet, index=[0]).drop(['edit_history_tweet_ids','public_metrics'], axis=1)
        df[list(keys)] = [list(values)]
        results = pd.concat([results, df])

        results['created_at'] = pd.to_datetime(results['created_at'])
        results.reset_index(drop=True, inplace=True)
        # reordering columns:
        results = results[['id', 'created_at', 'author_id', 'text', 'retweet_count', 'reply_count', 'like_count', 'quote_count']]
    return results