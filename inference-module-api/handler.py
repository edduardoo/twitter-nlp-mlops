import json
import numpy as np
from joblib import dump, load
import json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import configparser
import keras
import helper as hp


# loading model, tokenizer and configs
config = configparser.ConfigParser()
config.sections()
config.read('./config.ini')

max_len = int(config['model_params']['max_len'])
max_words = int(config['model_params']['max_words'])
sentiment = np.array(['Neutral','Negative','Positive'])

model = keras.models.load_model("./BidLTSM.hdf5")
tokenizer = load('./keras_tokenizer.joblib')

with open('./stopwords.txt') as file:
    lines = file.readlines()
    stopwords = [line.rstrip() for line in lines]
    print(stopwords)

def handler(event, context):

    print("EVENT PARAMS: {}".format(event))
    print("EVENT TYPE: {}".format(type(event)))
    new_data = event["texts"]
    if type(new_data) == str: # locally is a dict but on API Gateway is a string
        new_data = json.loads(new_data)

    new_data = [hp.clean_text(text, stopwords) for text in new_data]
    
    # predicting
    predictions = predict(new_data)

    # preparing response json
    response = {'predictions': list(predictions)}
    #response = json.dumps(response)

    return {
        'statusCode': 200,
        'body': response
    }

def predict(new_data):
    sequence = tokenizer.texts_to_sequences(new_data)
    padded = pad_sequences(sequence, maxlen=max_len)
    predictions = sentiment[np.around(model.predict(padded), decimals=0).argmax(axis=1)]
    return predictions


# TODO: implement continuous training
def train():
    pass


# the model is trained locally, by runing "python handler.py"
if __name__ == "__main__":
    pass
    #print(hp.remove_stopwords("This is a test for the stopwords that I'm using and she`s not using", stopwords))

