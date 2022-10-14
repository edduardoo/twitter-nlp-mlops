import json
import numpy as np
from joblib import dump, load
import json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import configparser
import keras


texts = ["Lauren Boebert: “Joe Biden can never be the kind of man that Donald Trump is.”"]

# loading model, tokenizer and configs
config = configparser.ConfigParser()
config.sections()
config.read('./config.ini')

max_len = int(config['model_params']['max_len'])
max_words = int(config['model_params']['max_words'])
sentiment = np.array(['Neutral','Negative','Positive'])

model = keras.models.load_model("./models/BidLTSM.hdf5")
tokenizer = load('./artifacts/keras_tokenizer.joblib')

sequence = tokenizer.texts_to_sequences(texts)
print(sequence)
padded = pad_sequences(sequence, maxlen=max_len)
raw_predictions = model.predict(padded)
print(raw_predictions)
predictions = sentiment[np.around(raw_predictions, decimals=0).argmax(axis=1)]
print(predictions)


if __name__ == "__main__":
    pass