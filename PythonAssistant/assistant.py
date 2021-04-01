from tkinter import *
from ttkthemes import themed_tk as tk
from PIL import ImageTk, Image
from tkinter import ttk
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
from getpass import getpass

assistant=tk.ThemedTk()
assistant.get_themes()
assistant.configure(background="teal")
assistant.set_theme("keramik") # ( blue, aquativo, elegance, clearlooks, keramik, radiance, winxpblue, black, )
assistant.title("Personal Assistant")
assistant.geometry("400x200")

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
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
        wishMe()

def main():
    speak("sir how may i help you")
    while True:
        # if 1:
        query = takeCommand().lower()

            # Logic for executing tasks based on query
        if 'details' in query:
            query=query.replace("could you please give me details about","")
            speak('Searching for details...')
            query = query.replace("find details about", "")
            results = wikipedia.summary(query, sentences=2)
            speak("The details are")
            print(results)
            speak(results)

def online():
    speak("sir what you want to search")
    while True:
        # if 1:
        query = takeCommand().lower()
        if 'open youtube' in query:
            
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
        elif "open google" in query:
            driver=webdriver.Chrome()
            driver.get("httpp://www.google.com/")
            break
        elif "subjects" in query:
            driver=webdriver.Chrome()
            driver.get("https://ucaelearning.org/login/index.php?sesskey=F2RQ9m5DjOLog%20in")
            user_box=driver.find_element_by_id('username')
            user_box.send_keys("552529")
            pass_box=driver.find_element_by_id('password')
            pass_box.send_keys("Wellcome85%")
            log_in=driver.find_element_by_id("loginbtn")
            log_in.submit()
            break
        elif "thank you" in query:
            break
        
    
def outlook():
    speak("which messages app you want to open")
    while True:
        query = takeCommand().lower()
        if "outlook" in query:
            outlook="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\outlook"
            os.startfile(os.path.join(outlook))
            break
        elif "whatsapp" in query:
            whatsapp="C:\\Users\\bashir.alam\\AppData\\Local\\WhatsApp\\WhatsApp"
            os.startfile(os.path.join(whatsapp))
            break
        elif" thank you" in query:
            break
            
def pc():
    pass
def off():
    pass
main_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\freshman\\computer science\\personal assistant\\main.png")
btn1=Button(assistant, text="", image=main_image, command=main, bg="teal")
btn1.place(x=140, y=30)
world_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\freshman\\computer science\\personal assistant\\worldwide.png")
btn2=ttk.Button(assistant, text="", image=world_image, command=online)
btn2.place(x=50, y=20)
outlook_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\freshman\\computer science\\personal assistant\\outlook.png")
btn3=ttk.Button(assistant, text="", image=outlook_image, command=outlook)
btn3.place(x=50, y=136)
pc_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\freshman\\computer science\\personal assistant\\pc.png")
btn4=ttk.Button(assistant, text="", image=pc_image, command=pc)
btn4.place(x=335, y=20)
exit_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\freshman\\computer science\\personal assistant\\power.png")
btn5=ttk.Button(assistant, text="", image=exit_image, command=off)
btn5.place(x=335, y=136)

assistant.mainloop()

