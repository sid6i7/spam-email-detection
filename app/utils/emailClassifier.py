from joblib import load
import sys
sys.path.append('app')
from config import *


class Classifier:

    def __init__(self) -> None:
        model, vectorizer = load(MODEL_PATH)
        self.model = model
        self.vectorizer = vectorizer
    
    def predict_email(self, email):
        counts = self.vectorizer.transform(email)
        prediction = self.model.predict(counts)

        if prediction[0] == 1:
            return 'Spam'
        else:
            return "Not spam"
