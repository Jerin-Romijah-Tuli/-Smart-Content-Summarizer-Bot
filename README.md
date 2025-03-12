# 🤖 Smart Content Summarizer Bot

## 🌟 Overview
**Smart Content Summarizer** is an AI-powered Telegram bot that helps users extract and summarize key insights from:
- 📄 **PDF documents**
- 🎥 **YouTube videos** (via transcript extraction)

Using advanced **Natural Language Processing (NLP)**, the bot delivers structured, concise summaries with key takeaways.

---

## 🚀 Features
✅ **Summarizes PDFs effortlessly** 📄
✅ **Extracts & summarizes YouTube transcripts** 🎥
✅ **Generates structured insights with AI** 🧠
✅ **Formats responses neatly in Markdown** 📝

---

## 🛠️ Tech Stack
- 🐍 **Python** (Core Programming Language)
- 🤖 **Telegram Bot API** (For bot interactions)
- 📄 **PyPDF2** (For PDF text extraction)
- 🎥 **YouTubeTranscriptApi** (For video transcript retrieval)
- 🏋️‍♂️ **Hugging Face Transformers** (For AI summarization)
- 🗂️ **Tempfile & OS** (For efficient file handling)

---

## 🤖 How to Get a Telegram Bot Token
To use this bot, you need a Telegram bot token. Follow these steps:

1. Open Telegram and search for **BotFather** or click [here](https://t.me/botfather).
2. Start a chat and type `/newbot`.
3. Follow the instructions and choose a **unique name** and **username** for your bot.
4. Once done, BotFather will provide you with a **bot token** (a long string).
5. Copy the token and replace the `TOKEN` variable in your script with your bot’s token.

---

## 🏗️ Installation & Setup
### Prerequisites
1. Install Python (>=3.8)
2. Obtain a Telegram Bot Token from [BotFather](https://t.me/botfather)
3. Install dependencies:

```sh
pip install python-telegram-bot PyPDF2 youtube-transcript-api transformers torch
```

### Running the Bot
1. Clone this repository:
```sh
git clone https://github.com/your-username/telegram-summarizer-bot.git
cd telegram-summarizer-bot
```
2. Update the `TOKEN` variable with your bot token.
3. Start the bot:
```sh
python bot.py
```

---

## 🚢 Deployment (Push to GitHub)
### Step 1: Initialize Git
```sh
git init
git add .
git commit -m "Initial commit"
```

### Step 2: Create a New GitHub Repository
1. Go to [GitHub](https://github.com/)
2. Click **New Repository**
3. Set the repository name (e.g., `telegram-summarizer-bot`)
4. Copy the repository URL

### Step 3: Push the Code to GitHub
```sh
git remote add origin https://github.com/your-username/telegram-summarizer-bot.git
git branch -M main
git push -u origin main
```

🚀 Now your project is live on GitHub! 🎉

---

## 🎯 Usage Guide
- **Start the bot**: `/start`
- **Upload a PDF** 📄: The bot extracts and summarizes the document.
- **Share a YouTube link** 🎥: The bot fetches and summarizes the transcript.

💡 **Pro Tip**: The bot provides an executive summary along with key points!

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 👩‍💻 Contributors
Developed with ❤️ by **Zerin Romjah Tuli** 🚀

