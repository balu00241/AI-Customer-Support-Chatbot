# 🤖 AI Chatbot for Automated Customer Support

This project is a **voice-enabled AI chatbot** developed using Python. It automates basic customer support tasks by recognizing speech input, generating appropriate responses using a custom dataset or AI model, and responding with synthesized voice. It also includes a feature to send **hospital directions via email** when requested.

---

## 📌 Table of Contents

- [🔧 Features](#-features)
- [🧠 Use Cases](#-use-cases)
- [📁 Project Structure](#-project-structure)
- [📦 Requirements](#-requirements)
- [🚀 How to Run](#-how-to-run)
- [📧 Email Notification Setup](#-email-notification-setup)
- [🎯 Future Scope](#-future-scope)
- [📸 Screenshots / Demo](#-screenshots--demo)
- [👨‍💻 Author](#-author)
- [📄 License](#-license)

---

## 🔧 Features

- 🎙️ Accepts **voice input** from the user
- 🗣️ Replies with **text-to-speech**
- 📚 Handles domain-specific queries using a **custom dataset**
- 💡 AI-powered fallback using OpenAI for dynamic answers
- 📧 Sends hospital directions to registered emails (Gmail SMTP used)
- 🧩 Modular code (easy to maintain and extend)
- 🧠 Offline & online capabilities

---

## 🧠 Use Cases

- Customer support in hospitals, banks, and educational institutions
- Interactive kiosks or help desks
- Elderly-friendly voice assistant
- Smart embedded chatbot using Raspberry Pi (future scope)

---

## 📁 Project Structure

```plaintext
AI-Customer-Support-Chatbot/
│
├── chatbot.py          # Core logic: handles user input and finds a matching response
├── dataset.json        # Domain-specific questions and answers (editable)
├── main.py             # Entry point of the application
├── speechinput.py      # Captures and converts voice to text
├── speechoutput.py     # Converts chatbot text response to voice
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies (optional)
└── LICENSE             # License file (MIT)
