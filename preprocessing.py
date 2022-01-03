import pandas as pd
import numpy as np
import re
import string
from nltk.tokenize import RegexpTokenizer
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

tokenizer = RegexpTokenizer(r'\w+')
st = nltk.PorterStemmer()
lm = nltk.WordNetLemmatizer()

stopwordlist = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
            'and','any','are', 'as', 'at', 'be', 'because', 'been', 'before',
            'being', 'below', 'between','both', 'by', 'can', 'd', 'did', 'do',
            'does', 'doing', 'down', 'during', 'each','few', 'for', 'from',
            'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
            'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
            'into','is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
            'me', 'more', 'most','my', 'myself', 'now', 'o', 'of', 'on', 'once',
            'only', 'or', 'other', 'our', 'ours','ourselves', 'out', 'own', 're','s', 'same', 'she', "shes", 'should', "shouldve",'so', 'some', 'such',
            't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
            'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
            'through', 'to', 'too','under', 'until', 'up', 've', 'very', 'was',
            'we', 'were', 'what', 'when', 'where','which','while', 'who', 'whom',
            'why', 'will', 'with', 'won', 'y', 'you', "youd","youll", "youre",
            "youve", 'your', 'yours', 'yourself', 'yourselves']
STOPWORDS = set(stopwordlist)

punctuations_list = string.punctuation

def cleaning_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

def cleaning_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

def cleaning_repeating_char(text):
    return re.sub(r'(.)1+', r'1', text)

def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))',' ',data)

def cleaning_numbers(data):
    return re.sub('[0-9]+', '', data)

def stemming_on_text(data):
    text = [st.stem(word) for word in data]
    return data

def lemmatizer_on_text(data):
    text = [lm.lemmatize(word) for word in data]
    return data

class preprocessing:

    def remove_null(df):
        null_count = df.loc[df['text'].isnull()].index.tolist()
        for i in null_count:
            df.drop(i - 1)
        return df

    def data_prep(df):
        df['text'] = df['text'].str.lower()
        df['text'] = df['text'].apply(lambda text: cleaning_stopwords(text))
        df['text']= df['text'].apply(lambda x: cleaning_punctuations(x))
        df['text'] = df['text'].apply(lambda x: cleaning_repeating_char(x))
        df['text'] = df['text'].apply(lambda x: cleaning_URLs(x))
        df['text'] = df['text'].apply(lambda x: cleaning_numbers(x))
        df['text']= df['text'].apply(lambda x: stemming_on_text(x))
        df['text'] = df['text'].apply(lambda x: lemmatizer_on_text(x))
        return df