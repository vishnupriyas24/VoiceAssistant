import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return ""
        return command.lower()
def respond_to_command(command):
    if "hello" in command:
        response = "Hello! How can I help you today?"
        speak(response)
    elif "time" in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        response = f"The current time is {current_time}"
        speak(response)
    elif "date" in command:
        today = datetime.today().strftime('%Y-%m-%d')
        response = f"Today's date is {today}"
        speak(response)
    elif "search" in command:
        speak("What do you want to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            response = f"Here are the search results for {query}"
            speak(response)
    else:
        response = "I can only respond to 'hello', 'time', 'date', and 'search' commands."
        speak(response)
def main():
    speak("Initializing the voice assistant.")
    while True:
        command = listen()
        if command:
            respond_to_command(command)
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
if __name__ == "__main__":
    main()
