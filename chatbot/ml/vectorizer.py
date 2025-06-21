import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from pathlib import Path

class Vectorizer:
    def __init__(self):
        self.vectorizer = None
        self.filepath = Path(__file__).parent / "vectorizer.pkl"

    def fit(self, texts):
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=5000,
            stop_words='english'
        )
        self.vectorizer.fit(texts)
        joblib.dump(self.vectorizer, self.filepath)

    def transform(self, texts):
        if self.vectorizer is None:
            if not self.filepath.exists():
                raise ValueError("Vectorizer not fitted yet!")
            self.vectorizer = joblib.load(self.filepath)
        return self.vectorizer.transform(texts)

    def fit_transform(self, texts):
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=5000,
            stop_words='english'
        )
        X = self.vectorizer.fit_transform(texts)
        joblib.dump(self.vectorizer, self.filepath)
        return X