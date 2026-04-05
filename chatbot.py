import nltk
from nltk.tokenize import word_tokenize

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break

    words = nltk.word_tokenize(user_input)

    if "hello" in words or "hi" in words:
        print("Chatbot: Hi there!")

    elif "how" in words:
        print("Chatbot: I'm doing great!")

    elif "name" in words:
        print("Chatbot: I'm your AI chatbot.")

    elif "college" in words or "student" in words:
        print("Chatbot: I am here to help students!")

    elif "help" in words:
        print("Chatbot: Sure! Ask me anything.")

    else:
        print("Chatbot: Sorry, I don't understand.")