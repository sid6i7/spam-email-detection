from joblib import load
import sys
sys.path.append('app')
from config import *
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re

class Classifier:

    def __init__(self) -> None:
        model, vectorizer = load(MODEL_PATH)
        self.model = model
        self.vectorizer = vectorizer
        self.stop_words = stopwords.words('english')
        self.lemmatizer = WordNetLemmatizer()
    
    def get_wordnet_pos(self, word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)
    
    def preprocess_email(self, email):
        # tokenization
        email = word_tokenize(email)

        # removing unwanted characters like punctuations
        email = [re.sub(r'[^\w\s]', "", word) for word in email if word != '']

        # url removal
        email = [re.sub(r'http\S+', '', word) for word in email if word != '']

        # stop-word removal
        email = [word for word in email if (word not in self.stop_words)]

        # lower-casing
        email = [word.lower() for word in email]

        # lemmatization
        email = [self.lemmatizer.lemmatize(word, self.get_wordnet_pos(word)) for word in email]
        
        return email
    
    def predict_email(self, email):
        email = [" ".join(self.preprocess_email(email))]
        counts = self.vectorizer.transform(email)
        prediction = self.model.predict(counts)
        if prediction[0] == 'spam':
            return 'Spam'
        else:
            return "Ham"
