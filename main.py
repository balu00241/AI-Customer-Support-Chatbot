from speech_input import get_audio
from speech_output import speak
from chatbot import load_dataset, get_response

def main():
    dataset = load_dataset()
    speak("Hello, how can I assist you today?")
    while True:
        user_input = get_audio()
        if user_input in ["exit", "bye", "stop"]:
            speak("Goodbye!")
            break
        response = get_response(user_input, dataset)
        speak(response)

if __name__ == "__main__":
    main()
