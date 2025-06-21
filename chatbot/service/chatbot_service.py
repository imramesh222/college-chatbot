import spacy
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class ChatbotService:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.questions = [
            "What is the academic calendar?",
            "Tell me about course information.",
            "How do I get to campus?",
            "Where can I find results and notices?",
            "What are the FAQs?",
            "How do I contact you?",
            "What is the admission process?",
            "What are the library timings?"
        ]
        self.answers = [
            "Here are the academic calendar dates...",
            "Here is information about courses...",
            "Here are the campus directions...",
            "Here are the latest results and notices...",
            "Here are some frequently asked questions...",
            "Here is the contact information...",
            "The admission process is as follows...",
            "The library is open from 9am to 8pm."
        ]
        self.preprocessed_questions = [self.preprocess(q) for q in self.questions]
        self.question_embeddings = self.model.encode(self.preprocessed_questions)
        self.history = []  # Stores (user_question, response) tuples

    def preprocess(self, text):
        doc = self.nlp(text.lower())
        tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        return " ".join(tokens)

    async def process_message(self, request, threshold=0.75):
        user_input = self.preprocess(request.message)
        user_embedding = self.model.encode([user_input])
        similarities = cosine_similarity(user_embedding, self.question_embeddings)[0]
        best_idx = np.argmax(similarities)
        if similarities[best_idx] > threshold:
            response = self.answers[best_idx]
        else:
            response = "I don’t understand. Please contact admin."
        # Remember the interaction
        self.history.append((request.message, response))
        return {"response": response}

    def get_history(self):
        # Returns the list of previous questions and answers
        return self.history

    def analyze_history(self):
        # Example: Count unique questions asked
        unique_questions = set(q for q, _ in self.history)
        return {"total_questions": len(self.history), "unique_questions": len(unique_questions)}