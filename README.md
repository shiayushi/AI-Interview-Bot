# AI-Interview-Bot
# 🤖 AI Interview Bot (Offline Version)

<img width="1918" height="861" alt="image" src="https://github.com/user-attachments/assets/1beac664-2b9b-48bd-9cef-c67bce6bda84" />


An interactive offline interview practice bot built using **Streamlit**, **NLTK**, and **LanguageTool**.  
It helps you:
- Answer real interview questions
- Get grammar-based improvements
- Analyze sentiment of your answers  
All without needing an internet connection or API key! 🔌✨

---

## 🚀 Features

- 📌 Select real interview questions from CSV
- 🗣️ Write your answer in text area
- ✨ Grammar-checked improved response (offline)
- 🧠 Sentiment analysis using NLTK
- 💻 Fully local — no API or billing needed!

---

## 📁 Folder Structure

AI Interview Bot/
├── ai_interview_bot.py # Streamlit app
├── utilsanalysis.py # Sentiment analysis logic
├── data/
│ └── questions.csv # List of interview questions
├── requirements.txt # Python dependencies
└── run_bot.bat # One-click launcher (Windows)


---

## 🛠 Installation & Setup

### 1️⃣ Clone the repo

```bash
git clone https://github.com/yourusername/ai-interview-bot.git
cd ai-interview-bot

### 2️⃣ Install required packages

```bash
pip install -r requirements.txt

### 3️⃣ Run the app

```bash
streamlit run ai_interview_bot.py
Or simply double-click run_bot.bat on Windows 💻
