import speech_recognition as sr
import pyttsx3
import datetime

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        query = None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        query = None

    return query

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def main():
    greet()
    speak("How can I assist you today?")

    while True:
        query = listen()

        if query:
            if "hello" in query.lower():
                speak("Hello there!")
            elif "time" in query.lower():
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}.")
            elif "date" in query.lower():
                current_date = datetime.datetime.now().strftime("%B %d, %Y")
                speak(f"Today is {current_date}.")
            elif "bye" in query.lower():
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't know how to help with that.")

if __name__ == "__main__":
    main()
