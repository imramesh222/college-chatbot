import sys
import joblib
from chatbot.ml.nlp_utils import preprocess_text

# Load model and vectorizer using joblib
model = joblib.load('chatbot/ml/model.pkl')
vectorizer = joblib.load('chatbot/ml/vectorizer.pkl')

intent_responses = {
    "admission_info": "You can find admission details on our website or contact the admissions office.",
    "exam_schedule": "The exam schedule is available on the student portal.",
    "location_query": "The college is located at 123 Main St.",
    "program_info": "We offer various programs in science, arts, and commerce."
}

def get_bot_response(user_input):
    cleaned = preprocess_text(user_input)
    X = vectorizer.transform([cleaned])
    intent = model.predict(X)[0]
    response = intent_responses.get(intent, "Sorry, I don't have information on that.")
    return response

if __name__ == "__main__":
    print("Chatbot ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", get_bot_response(user_input))