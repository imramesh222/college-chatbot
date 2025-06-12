# ml/vectorizer.py
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from pathlib import Path

class Vectorizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=5000,
            stop_words='english'
        )
        self.filepath = Path(__file__).parent / "vectorizer.pkl"

    def fit(self, texts):
        self.vectorizer.fit(texts)
        joblib.dump(self.vectorizer, self.filepath)

    def transform(self, texts):
        if not self.filepath.exists():
            raise ValueError("Vectorizer not fitted yet!")
        vectorizer = joblib.load(self.filepath)
        return vectorizer.transform(texts)

    def fit_transform(self, texts):
        X = self.vectorizer.fit_transform(texts)
        joblib.dump(self.vectorizer, self.filepath)
        return X