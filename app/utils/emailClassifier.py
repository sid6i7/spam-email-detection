from joblib import load
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from config import MODEL_PATH
from sklearn.feature_extraction.text import CountVectorizer


class Classifier:

    def __init__(self) -> None:
        self.model = load(MODEL_PATH)
        self.vectorizer = CountVectorizer()
    
    def predict_email(self, email):
        counts = vec
        prediction = self.model.pr
