import sys
from chatbot.ml.nlp_utils import preprocess_text, extract_entities
# Import your trained model and vectorizer here

def get_bot_response(user_input):
    cleaned = preprocess_text(user_input)
    # X = vectorizer.transform([cleaned])
    # intent = model.predict(X)[0]
    # response = ... # Lookup or generate response based on intent
    response = f"Processed: {cleaned}"  # Placeholder
    return response

if __name__ == "__main__":
    print("Chatbot ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", get_bot_response(user_input))