import os
import csv
from textblob import TextBlob

def load_questions(filename="questions.txt"):
    if not os.path.exists(filename):
        return [
            "Tell me about yourself.",
            "What are your strengths?",
            "Why should we hire you?",
            "Describe a challenge you overcame.",
            "Where do you see yourself in 5 years?"
        ]
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def analyze_answer(answer):
    feedback = []
    words = answer.split()
    long_words = [w for w in words if len(w) > 6]

    if len(words) < 10:
        feedback.append("Try to give a longer answer with more detail.")
    else:
        feedback.append("Nice length. You explained well.")

    if not answer.strip().endswith('.'):
        feedback.append("Consider ending with proper punctuation.")

    if len(long_words) < 3:
        feedback.append("Try using more descriptive vocabulary.")

    blob = TextBlob(answer)
    polarity = round(blob.sentiment.polarity, 2)
    sentiment_type = (
        "Positive 😊" if polarity > 0.1 else
        "Negative 😕" if polarity < -0.1 else
        "Neutral 😐"
    )

    return feedback, polarity, sentiment_type

def save_to_csv(question, answer, feedback, polarity, sentiment_type, filename="answers.csv"):
    file_exists = os.path.exists(filename)
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Question', 'Answer', 'Feedback', 'Sentiment Score', 'Sentiment Type'])
        writer.writerow([question, answer, "; ".join(feedback), polarity, sentiment_type])

def main():
    print("🤖 AI Interview Bot (Offline + Sentiment)\n")
    questions = load_questions()

    for idx, question in enumerate(questions, start=1):
        print(f"\nQ{idx}: {question}")
        answer = input("📝 Your Answer (type 'exit' to quit):\n> ")

        if answer.strip().lower() in ['exit', 'quit']:
            print("\n👋 Interview ended by user. Goodbye!")
            break

        feedback, polarity, sentiment_type = analyze_answer(answer)

        print("\n✅ Feedback:")
        for fb in feedback:
            print(f" - {fb}")
        
        print(f"\n💬 Sentiment Score: {polarity} → {sentiment_type}")
        print("-" * 50)

        save_to_csv(question, answer, feedback, polarity, sentiment_type)

    print("\n🎉 Interview simulation completed! Great job!")

if __name__ == "__main__":
    main()
