# 🤖 Gemini LangGraph Chatbot

A lightweight, terminal-based conversational AI chatbot powered by **Gemini 2.0 Flash Lite** and orchestrated with **LangGraph**. This project demonstrates how to create a goal-driven chatbot with memory, using a state machine flow and real-time conversation logging.

---

## 🔍 Overview

This chatbot accepts user input from the terminal, uses Google’s Gemini model to generate intelligent responses, and logs the entire conversation in a `log.json` file. The flow of the conversation is managed using `LangGraph`’s `StateGraph`, making it extensible for future development like memory, tools, or external APIs.

---

## 🚀 Features

- 🧠 Powered by **Gemini 2.0 Flash Lite**
- ⚙️ Built using **LangGraph** for modular state transitions
- 💬 Remembers full chat history during the session
- 📝 Logs conversation to `log.json`
- 🔐 Loads API key from `.env` securely
- 🧪 Fully terminal-driven – no UI needed

---

## 📦 Tech Stack

| Tool / Library | Purpose |
|----------------|---------|
| 🌐 Gemini API (via LangChain) | LLM responses |
| 🧱 LangGraph | State management |
| 🐍 Python | Core scripting |
| 🧪 Terminal / CLI | User interaction |
| 🔑 dotenv | API key management |
| 📂 JSON | Conversation logging |

---

