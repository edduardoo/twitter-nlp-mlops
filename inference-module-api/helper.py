import re

def clean_text(text, stopwords):
    text = text.lower()
    text = re.sub(' +', ' ', text) # remove extra spaces
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text) # remove non-alphanumeric
    words = text.split(' ')
    words = [w for w in words if w not in stopwords]
    return ' '.join(words)

