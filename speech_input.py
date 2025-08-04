import speech_recognition as sr

def get_audio():
    recognizer = sr.Recognizer()
    
    # Optional tuning for better recognition
    recognizer.pause_threshold = 0.5       # Accepts slightly longer pauses
    recognizer.energy_threshold = 200       # Sensitivity to sound energy
    
    with sr.Microphone() as source:
        print("🎤 Please Speak... Chatbot is Listening...")
        
        # Adjust to ambient noise for 1 second
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            print(f"🗣️ Your Response: {text}")
            return text.lower()
        
        except sr.WaitTimeoutError:
            print("⏳ Listening timed out while waiting for phrase.")
            return ""
        except sr.UnknownValueError:
            print("😕 Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("❌ Could not request results from the recognition service.")
            return ""
