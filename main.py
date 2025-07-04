import datetime
import webbrowser
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition

engine = pyttsx3.init()  # initialise pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-2 range for different voices
voicespeed = 140  # setting speed
engine.setProperty('rate', voicespeed)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Listen for a command from the user and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:

        print()
        return "---"
    return query

def time():
    """Speak the current time."""
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)

def wishme():
    speak("welcome back sir")

    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak('Good morning')
    elif hour>=12 and hour<=18:
        speak('Good afternoon')
    elif hour>=18 and hour<=24:
        speak('Good evening')
    else:
        speak('good night')

    speak('How can i help you today')

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        print(query)

        if "good morning" in query:
            speak("good morning sir")

        elif "time" in  query:
            time()

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open github" in query:
            webbrowser.open("https://github.com/yogeshwaran8731")

        elif "open typing club" in query:
            webbrowser.open("https://www.edclub.com/sportal/program-3.game")

        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com/in/yogeshwaran-v-200785303/")