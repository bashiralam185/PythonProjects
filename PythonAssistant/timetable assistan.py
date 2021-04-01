import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
    speak("sir, your timetable is as follow")
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'Monday' in query:
            speak("Sir, you have Maths class at 9:00am, then you have cultural Studies At 11 am. After lunch you have IT class at 3'o clock .Have a nice day. ")
            break
        elif "tuesday" in query:
            speak(" Sir, You have geography class at 11 o clock and then you have kyrgyz language class at 1:30. have a nice day")
            break
        elif "wednessday" in query:
            speak("Sir, wednessday is you busiest day. You have maths class at 9, culture at 11, geography at 1:30 and finally IT class at 3 o clock. have a nice day")
