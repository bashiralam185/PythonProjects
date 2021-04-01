import speech_recognition as sr
import pyttsx3

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak( audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening,,,,")
        r.pause_threshold=1
        audio= r.listen(source)

    try:
        print("recogning")
        query= r.recognize_google(audio)
        print(query)
    except: 
        print("please speek again")


if __name__== "__main__":
    speak("hay, Bashir")
    takeCommand()