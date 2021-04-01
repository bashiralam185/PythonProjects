import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
from getpass import getpass

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'details' in query:
            query=query.replace("could you please give me details about","")
            speak('Searching for details...')
            query = query.replace("details", "")
            results = wikipedia.summary(query, sentences=2)
            speak("The details are")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            
            query=query.replace("open youtube and play", "")
            driver=webdriver.Chrome()
            driver.get('http://www.youtube.com/')
            
            search_box=driver.find_element_by_id('search')
            search_box.send_keys(query)
            
            login_btn=driver.find_element_by_id("search-icon-legacy")
            login_btn.submit()
            open_vedio=driver.find_element_by_id("contents")
            open_vedio.click()
            break
        elif "outlook" in query:
            outlook="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\outlook"
            os.startfile(os.path.join(outlook))
            break
        elif "open google" in query:
            query=query.replace("open google and search", "")
            driver=webdriver.Chrome()
            driver.get("httpp://www.google.com/")
            
            search_box= driver.find_elements_by_class_name("gLFyf gsfi")
            search_box.send_keys(query)
            
            search_btn=driver.find_element_by_class_name("wFncld z1asCe MZy1Rb")
            search_btn.submit()
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\bashir.alam\\Documents\\Zapya\\Music\\20191229_0121'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            break
        elif 'thank you' in query:
            break

