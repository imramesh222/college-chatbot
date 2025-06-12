# ml/nlp_utils.py
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from typing import List, Dict

# Set custom NLTK data directory
nltk_data_dir = '/Users/rameshrawat/college-chatbot/nltk_data'
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

nltk.download('stopwords', download_dir=nltk_data_dir)
nltk.download('wordnet', download_dir=nltk_data_dir)
nltk.download('omw-1.4', download_dir=nltk_data_dir)


class TextPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.special_tokens = {
            'bsc csit': 'bsc_csit',
            'it department': 'it_department'
        }

    def preprocess_text(self, text: str) -> str:
        """Full text preprocessing pipeline"""
        text = self._normalize_special_tokens(text)
        text = self._clean_text(text)
        tokens = self._tokenize(text)
        tokens = self._remove_stopwords(tokens)
        tokens = self._lemmatize(tokens)
        return ' '.join(tokens)

    def _normalize_special_tokens(self, text: str) -> str:
        """Handle special college-specific terms"""
        for term, replacement in self.special_tokens.items():
            text = text.replace(term, replacement)
        return text

    def _clean_text(self, text: str) -> str:
        """Basic text cleaning"""
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9_\s]', '', text)
        return text.strip()

    def _tokenize(self, text: str) -> List[str]:
        """Simple whitespace tokenization"""
        return text.split()

    def _remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove stopwords and short tokens"""
        return [t for t in tokens
                if t not in self.stop_words and len(t) > 2]

    def _lemmatize(self, tokens: List[str]) -> List[str]:
        """Lemmatize tokens"""
        return [self.lemmatizer.lemmatize(t) for t in tokens]


def preprocess_text(text: str) -> str:
    """Convenience function for text preprocessing"""
    return TextPreprocessor().preprocess_text(text)


def extract_entities(text: str) -> Dict[str, str]:
    """Extract college-specific entities from text"""
    entities = {}
    text_lower = text.lower()

    # Academic terms
    academic_terms = {
        'semester': ['semester', 'term'],
        'exam': ['midterm', 'final', 'exam'],
        'program': ['bsc csit', 'bsc_csit', 'bachelor', 'master']
    }

    for entity, keywords in academic_terms.items():
        for kw in keywords:
            if kw in text_lower:
                entities[entity] = kw.replace(' ', '_')
                break

    # Location detection
    locations = ['library', 'lab', 'cafeteria', 'admin', 'office']
    for loc in locations:
        if loc in text_lower:
            entities['location'] = loc
            break

    return entities