import os
import sys
import joblib
import pandas as pd
from pathlib import Path
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from .vectorizer import Vectorizer
from .nlp_utils import preprocess_text

class IntentClassifier:
    def __init__(self):
        self.vectorizer = Vectorizer()
        self.model = None

    def load_data(self):
        return pd.read_csv(Path(__file__).parents[2] / "data" / "training_data.csv")

    def save_model(self):
        joblib.dump(self.model, Path(__file__).parent / "model.pkl")
        joblib.dump(self.vectorizer, Path(__file__).parent / "vectorizer.pkl")

    def train(self, test_size=0.2, random_state=42):
        try:
            df = self.load_data()
            print(f"Loaded {len(df)} training examples")
            if 'cleaned_question' not in df.columns:
                df['cleaned_question'] = df['question'].apply(preprocess_text)
            X = self.vectorizer.fit_transform(df['cleaned_question'])
            y = df['intent']
            n_classes = y.nunique()
            n_samples = len(y)
            min_test_size = n_classes / n_samples
            if test_size < min_test_size:
                print(f"test_size={test_size} too small for {n_classes} classes; using test_size={min_test_size:.2f}")
                test_size = min_test_size
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state, stratify=y)
            self.model = SVC(probability=True, random_state=random_state)
            self.model.fit(X_train, y_train)
            y_pred = self.model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            print("\nModel Evaluation:")
            print(classification_report(y_test, y_pred))
            print(f"Accuracy: {acc:.2f}")
            self.save_model()
            return self.model
        except Exception as e:
            print(f"Training failed: {str(e)}", file=sys.stderr)
            raise

if __name__ == "__main__":
    clf = IntentClassifier()
    clf.train()