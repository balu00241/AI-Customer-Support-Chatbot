import pyttsx3

engine = pyttsx3.init()

# List available voices (optional for debugging)
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.languages}")

# Set desired voice (you can change index here)
engine.setProperty('voice', voices[0].id)  # Female voice example

# 🔉 Set speaking speed (default ~200, lower = slower)
engine.setProperty('rate', 150)  # Try values between 100 and 160 for slower speech

def speak(text):
    print(f"🤖 AI ChatBot: {text}")
    engine.say(text)
    engine.runAndWait()
