import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime

engine = pyttsx3.init()
engine.setProperty('voice', 'english')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your assistant. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except:
        print("Sorry, I didn't understand. Please say that again.")
        return "None"
    return query.lower()

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_now}")

        elif 'open notepad' in query:
            os.system("notepad.exe")

        elif 'open calculator' in query:
            os.system("calc.exe")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            break
