import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download tokenizer (only first time)
nltk.download('punkt')

# FAQ DATA
questions = [
    "What is artificial intelligence?",
    "What is machine learning?",
    "What is deep learning?",
    "What is python?",
    "What is data science?",
    "What is NLP?",
    "What is frontend development?",
    "What is backend development?",
    "What is HTML?",
    "What is CSS?"
]

answers = [
    "Artificial Intelligence is the simulation of human intelligence in machines.",
    "Machine Learning is a subset of AI that learns from data automatically.",
    "Deep Learning is a type of machine learning using neural networks.",
    "Python is a popular programming language used in AI and web development.",
    "Data Science involves analyzing data to extract insights.",
    "NLP stands for Natural Language Processing.",
    "Frontend development focuses on user interface and design.",
    "Backend development handles server, database, and logic.",
    "HTML is used to structure web pages.",
    "CSS is used to style web pages."
]

def preprocess(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    return text

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

def get_response(user_input):
    user_input = preprocess(user_input)
    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, question_vectors)
    max_score = similarity.max()
    index = similarity.argmax()

    if max_score < 0.3:
        return "Sorry, I don't understand that. Please ask something related."

    return answers[index]

print("\n🤖 FAQ Chatbot is Ready!")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye 👋")
        break

    if user_input.lower() in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")
        continue

    response = get_response(user_input)
    print("Bot:", response)