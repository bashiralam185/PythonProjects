import pyttsx3 as ts
import datetime

engine=ts.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voice:", voices[0].id)
hour= int(datetime.datetime.now().hour)
if hour>=0 and hour<=12:
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    speak("Good Morning. I am your helper. How can I help you")

if hour>12 and hour<18:
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    speak("Good afternoon. I am your helper. How can I help you")


if hour>18 and hour<24:
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    speak("Good  evening. I am your helper. How can I help you")