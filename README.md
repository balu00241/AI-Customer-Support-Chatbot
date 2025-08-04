# 🤖 AI Chatbot for Automated Customer Support

This is a **voice-enabled AI chatbot** project developed in Python to automate customer support tasks. Users interact via microphone; the assistant speaks the responses using text-to-speech and can answer both fixed, domain-specific questions (from a local dataset) and generic items (via OpenAI, if configured). For hospital-related queries, the bot can email directions automatically.

## 🔧 Features

- **Voice input** using your microphone  
- **Text-to-speech output** using `pyttsx3`
- **Local Q&A**: Answers from a customizable dataset for domain-specific queries
- **OpenAI fallback**: Optionally answer out-of-domain queries using ChatGPT
- **Email directions** for hospital queries with Gmail SMTP
- **Python-only, modular** code — runs on desktops, Raspberry Pi, and kiosks

## 📁 Folder and File Structure

```
AI-Customer-Support-Chatbot/
│
├── main.py           # Main script to run the chatbot
├── chatbot.py        # Chatbot logic (dataset/OpenAI)
├── speechinput.py    # Speech-to-text helper
├── speechoutput.py   # Text-to-speech helper
├── dataset.json      # Local dataset: Q&A pairs
├── README.md         # Full project documentation (you're reading it)
```

## 📦 Installation & Requirements

### 1. **Prerequisites**
- Python 3.7 or higher (check with `python --version`)

### 2. **Required Libraries**

Install these packages in your terminal or command prompt:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install openai
pip install pyaudio
```

*If you get errors installing pyaudio (common on Windows):*

```bash
pip install pipwin
pipwin install pyaudio
```

> **Note:**  
> `smtplib` and `email` are built-in Python libraries — do **not** install them separately!

## 🚀 How to Run the Project

1. **Download or clone** this repo  
2. Make any necessary changes to email settings (see below for email setup)  
3. In your terminal (inside the project folder), run:
   ```bash
   python main.py
   ```

4. **Speak into your microphone.** Try these example questions:
    - “Where is the hospital?”
    - “Who is the principal?”
    - “Where is the ATM?”

5. **Listen for the chatbot’s spoken reply.** For hospital queries, check the recipient email for directions.

## 🗂 Sample Dataset (`dataset.json`)

Your Q&A data file should look like this:

```json
{
  "where is the atm": "The ATM is located near the front entrance.",
  "who is the principal": "Dr. Sudha Rani is the principal of our institution.",
  "where is the hospital": "The nearest hospital is Apollo. I have sent directions to your email."
}
```
## 💡 Example Conversation Flow

**User:** “Where is the hospital?”  
**Bot (voice):** “The nearest hospital is Apollo. I have sent directions to your email.”  

**User:** “Who is the principal?”  
**Bot (voice):** “Dr. Sudha Rani is the principal of our institution.”

## 🧠 Future Enhancements

- Web interface (Flask)
- Mobile app version (Kivy)
- Multilingual support (Telugu, Hindi, etc.)
- Logging & analytics
- Camera integration for on-site support

## 👨💻 Author

**Badam Balaji**  
- 📧 Email: badambalu8@gmail.com
- 🌐 LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/badam-balaji-ab0523235/)  
- 🏫 Bachelor of Technology – ECE, TKR College of Engineering and Technology, JNTUH

## 📄 License

**MIT License**

> Permission is hereby granted, free of charge, to any person obtaining a copy  
> of this software and associated documentation files (the “Software”), to deal  
> in the Software without restriction, including without limitation the rights  
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
> copies of the Software, and to permit persons to whom the Software is  
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in  
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
> THE SOFTWARE.

> **Feel free to modify and use this code for your own projects! If you enjoyed using this assistant, star the repo or connect for improvements.**
