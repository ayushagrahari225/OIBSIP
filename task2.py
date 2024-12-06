import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
        return ""

def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = get_command()
        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "time" in command:
            now = datetime.now()
            speak(f"The current time is {now.strftime('%H:%M')}.")
        elif "date" in command:
            today = datetime.today()
            speak(f"Today's date is {today.strftime('%B %d, %Y')}.")
        elif "search" in command:
            speak("What should I search for?")
            search_query = get_command()
            if search_query:
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                speak("Here are the search results.")
        elif "exit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
