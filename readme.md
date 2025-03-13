# 🤖 Simple AI Chatbot with Streamlit & Langchain

## 🚀 Overview
This is a simple chatbot built using **Langchain** and **Streamlit**. It utilizes **Groq** for language processing, allowing users to interact with an AI assistant in a web-based chat interface.

## 📌 Features
- User-friendly chat interface powered by **Streamlit**
- Conversational memory using **Langchain**
- Secure API key input for **Groq**
- Lightweight and easy to set up

## 🔧 Installation & Setup
Follow these steps to set up and run the chatbot:

### 1️⃣ Clone the Repository
```sh
git clone <repository-url>
cd <repository-folder>
```

### 2️⃣ Install Dependencies
Install the required Python packages one by one:
```sh
pip install streamlit
pip install langchain
pip install langchain_groq
```

### 3️⃣ Run the Application
Start the chatbot by running:
```sh
streamlit run filename.py
```

### 4️⃣ Input API Key & Chat 💬
- A **web application** will open in your browser.
- Enter your **Groq API Key** (Get one for free at [Groq Console](https://console.groq.com/playground)).
- Start chatting with your AI assistant!

## 📜 How It Works
1. The **user inputs a message** in the chat.
2. The chatbot processes it using **Langchain’s ConversationChain**.
3. The **Groq AI model (Llama3-70b-8192)** generates a response.
4. The conversation is **stored in memory** for context-aware responses.

## 🛠️ Built With
- **Python** 🐍
- **Streamlit** 🌐
- **Langchain** 🔗
- **Groq API** 🤖

## 🎯 Future Improvements
- Enhance UI with custom styles
- Support multiple language models
- Add voice input and output support
