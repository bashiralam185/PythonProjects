from tkinter import *
from pygame import mixer
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter import ttk
from mutagen.mp3 import MP3
from ttkthemes import themed_tk as tk
from PIL import ImageTk, Image
import datetime
import pyttsx3 as ts
import smtplib
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write


#main screen of player
player=tk.ThemedTk() # this themes is used to design our whole player
player.get_themes()
player.set_theme("blue") # ( blue, aquativo, elegance, clearlooks, keramik, radiance, winxpblue, black, )
mixer.init()  # to start the mixer which is used to play the music
player.title("Ramz Player")
player.geometry("500x237")
player.configure(background="lightblue")
music= PhotoImage('music.icon')
player.iconbitmap(r'music')
heading=Label(player, text="Make Some Noise", bg="lightblue")
heading.place(x=240, y=0)
statusbar =ttk.Label(player, text="Welcome to Ramz music player")
statusbar.pack(side=BOTTOM, fill=X, anchor=W)# w stands for west...it will put the text at the left side
volum=Label(player, text="Volume", bg="lightblue" )
volum.place(x=405, y=50)
plist=Label(player, text="Play List", bg="lightblue")
plist.place(x=33, y=10)
timebar=Label(player, text="--:--", bg="lightblue")
timebar.place(x=400, y=0)


#The frames of the player
#menu bar

def open_file():
    global filename
    filename= filedialog.askopenfilename()
    add_t0_play_list(filename)
    
def exit_player():
    exit()
    
def about():
    #Welcome speech
    engine=ts.init("sapi5")
    voices= engine.getProperty("voices")
    engine.setProperty("voice:", voices[0].id)
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        def morning(text):
            engine.say(text)
            engine.runAndWait()

        morning("Good Morning. Thanks for using Raamzz player. This player is made by Python coding. The libraries that are used in the coding are tkinter, pygame, pyttsx3, datetime, os, pyaudio, datetime, speech recognition, sound device and PIL. This is multi-player, It can be controlled by user speech command and by manual buttons as well. It can play mp3, m4a and wav format audio files")

    if hour>12 and hour<18:
        def noon(text):
            engine.say(text)
            engine.runAndWait()

        noon("Good afternoon. Thanks for using Raamzz player. This player is made by Python coding. The libraries that are used in the coding are tkinter, pygame, datetime, os , pyaudio, speech recognition, sound decive and PIL.  This is multi-player, It can be controlled by user speech command and by manual buttons as well. It can play mp3, m4a and wav format audio files")


    if hour>18 and hour<24:
        def night(text):
            engine.say(text)
            engine.runAndWait()

        night("Good  evening. Thanks for using Raamzz player. This player is made by Python coding. The libraries that are used in the coding are tkinter, pygame, datetime, os , pyaudio, speech recognition, soun device and PIL.  This is multi-player, It can be controlled by user speech command and by manual buttons as well. It can play mp3, m4a, and wav format audio files")
    

def help():
    #Welcome speech
    engine=ts.init("sapi5")
    voices= engine.getProperty("voices")
    engine.setProperty("voice:", voices[0].id)
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        def morning(text):
            engine.say(text)
            engine.runAndWait()
        morning("Good Morning. How may I help you")
        engine = ts.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()  

                

        def takeCommand():
            #It takes microphone input from the user and returns string output

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")    
                query = r.recognize_google(audio)
                print(f"User said: {query}\n")

            except Exception:
                # print(e)    
                speak("please say it again. I couldn't hear your commands properly")  
                return "None"
            return query

        if __name__ == "__main__":
            speak("Sir. what you want to change")
            while True:
                query = takeCommand().lower()
        
                if "background color" in query:
                    speak("You can change the background color by commanding through your speech. To activate the assistant click on ASC and then your can commad your assistant to change background color for you. If you need more colors, then go to the settings and select background color for yourself")
                    break
                if "song" in query:
                    speak("You can add song to your play list by adding songs. Once you play a song you can controll it by your speech commands. To activate your player assitant click on audio command")
                    break
                if " record " in query:
                    speak(" click on recorder button. then you can select the time duration for recording. Once you select the time your recording will be start and it will stop when the selcted time up")
                    break
                if "thank you" in query:
                    break
                else:
                    speak("sir. please say it again. i coundn't hear your commands properly")
                    break
    if hour>12 and hour<18:
        def afternoon(text):
            engine.say(text)
            engine.runAndWait()
        afternoon("Good afternoon. How may I help you")
        engine = ts.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        def speaker(audio):
            engine.say(audio)
            engine.runAndWait()  

                

        def takeCommand1():
            #It takes microphone input from the user and returns string output

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")    
                query = r.recognize_google(audio)
                print(f"User said: {query}\n")

            except Exception:
                # print(e)    
                print("Say that again please...")  
                return "None"
            return query

        if __name__ == "__main__":
            while True:
                query = takeCommand1().lower()
        
                if "background color" in query:
                    speaker("You can change the background color by commanding through your speech. To activate the assistant click on ASC and then your can commad your assistant to change background color for you. If you need more colors, then go to the settings and select background color for yourself")
                    break
                if "song" in query:
                    speaker("You can add song to your play list by adding songs. Once you play a song you can controll it by your speech commands. To activate your player assistant click on audio command")
                    break
                if " record " in query:
                    speaker(" click on recorder button. then you can select the time duration for recording. Once you select the time your recording will be start and it will stop when the selcted time up")
                    break
                if "thank you" in query:
                    break
                else:
                    speaker("sir. please say it again. i coundn't hear your commands properly")
                    break
    if hour>18 and hour<24:
        def evening(text):
            engine.say(text)
            engine.runAndWait()
        evening("Good  evening. How may I help you")
        engine = ts.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        def speak1(audio):
            engine.say(audio)
            engine.runAndWait()  

                

        def takeCommand2():
            #It takes microphone input from the user and returns string output

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")    
                query = r.recognize_google(audio)
                print(f"User said: {query}\n")

            except Exception:
                # print(e)    
                print("Say that again please...")  
                return "None"
            return query

        if __name__ == "__main__":
            speak1("Sir. what you want to change")
            while True:
                query = takeCommand2().lower()
        
                if "background color" in query:
                    speak1("You can change the background color by commanding through your speech. To activate the assistant click on ASC and then your can commad your assistant to change background color for you. If you need more colors, then go to the settings and select background color for yourself")
                    break
                if "song" in query:
                    speak1("You can add song to your play list by adding songs. Once you play a song you can controll it by your speech commands. To activate your player assitant click on audio command")
                    break
                if " record " in query:
                    speak1(" click on recorder button. then you can select the time duration for recording. Once you select the time your recording will be start and it will stop when the selcted time up")
                    break
                if "thank you" in query:
                    break
                else:
                    speak1("sir. please say it again. i coundn't hear your commands properly")
                    break
        

def setting():
    setting=tk.ThemedTk() # this themes is used to design our whole player
    setting.get_themes()
    setting.set_theme("blue")
    mixer.init()
    setting.title("Settings")
    setting.geometry("400x35")

    #changing the icon
    music= PhotoImage('music.icon')
    setting.iconbitmap(r'music')

    def volume():
        def set_volume(val):
            volume=int(val)/100
            mixer.music.set_volume(volume)
            
        v=Tk()
        v.title("volume")
        volume= Scale(v, from_=0, to =100, orient="horizontal", command=set_volume)
        volume.pack()
        v.mainloop()
    button1= ttk.Button(setting, text="Volume", command=volume)
    button1.place(x=0, y=1)

    def colors():
        colors=tk.ThemedTk()
        player.get_themes()
        player.set_theme("blue")
        colors.title("colors")
        colors.geometry("50x160")
        def salmon():
            player.configure(background="light salmon")
            timebar.configure(background= "light salmon")
            heading.configure(background="light salmon")
            lst.configure(background="salmon")
            volum.configure(background="light salmon")
            plist.configure(background="light salmon")
        def green():
            player.configure(background="lime green")
            timebar.configure(background= "lime green")
            heading.configure(background="lime green")
            lst.configure(background="lightgreen")
            volum.configure(background="lime green")
            plist.configure(background="lime green")
        def lightgreen():
            player.configure(background="lightgreen")
            timebar.configure(background= "lightgreen")
            heading.configure(background="lightgreen")
            lst.configure(background="lime green")
            volum.configure(background="lightgreen")
            plist.configure(background="lightgreen")
        def pink():
            player.configure(background="pink")
            timebar.configure(background= "pink")
            heading.configure(background="pink")
            lst.configure(background="tomato")
            volum.configure(background="pink")
            plist.configure(background="pink")
        def lavender():
            player.configure(background="lavender")
            timebar.configure(background= "lavender")
            heading.configure(background="lavender")
            lst.configure(background="lightblue")
            volum.configure(background="lavender")
            plist.configure(background="lavender")
        def white():
            player.configure(background="white")
            timebar.configure(background= "white")
            heading.configure(background="white")
            lst.configure(background="lavender")
            volum.configure(background="white")
            plist.configure(background="white")
        def wheat():
            player.configure(background="wheat")
            timebar.configure(background= "wheat")
            heading.configure(background="wheat")
            lst.configure(background="moccasin")
            volum.configure(background="wheat")
            plist.configure(background="wheat")

        def default():
            player.configure(background="lightblue")
            timebar.configure(background= "lightblue")
            heading.configure(background="lightblue")
            lst.configure(background="sky blue")
            volum.configure(background="lightblue")
            plist.configure(background="lightblue")

        btn1=Checkbutton(colors, text=" Salmon", command=salmon)
        btn1.place(x=5, y=0)
        btn2= Checkbutton(colors, text=" green", command=green)
        btn2.place(x=5, y=120)
        btn3= Checkbutton(colors, text=" lightgreen", command=lightgreen)
        btn3.place(x=5, y=20)
        btn4=Checkbutton(colors, text=" pink", command=pink)
        btn4.place(x=5, y=40)
        btn5= Checkbutton(colors, text=" lavender", command=lavender)
        btn5.place(x=5, y=60)
        btn6= Checkbutton(colors, text=" white", command=white)
        btn6.place(x=5, y=80)
        btn7= Checkbutton(colors, text=" wheat", command=wheat)
        btn7.place(x=5, y=100)
        btn8=Checkbutton( colors, text="default", command= default)
        btn8.place(x=5, y=140)

        colors.mainloop()
    button2= ttk.Button(setting, text="Background color", command=colors)
    button2.place(x=80, y=1)

    setting.mainloop()

#creating the menu bar   
menu=Menu(player)
player.config(menu=menu)

submenu1=Menu(menu)
menu.add_cascade(label="file", menu=submenu1)
submenu1.add_command(label="open...",  command=open_file)
submenu1.add_command(label="exit",  command=exit_player)

submenu2=Menu(menu)
menu.add_cascade(label="option",menu=submenu2)
submenu2.add_command(label="about", command=about)

submenu3=Menu(menu)
menu.add_cascade(label="Help", menu= submenu3)
submenu3.add_command(label="Help", command=help)

submenu4= Menu(menu)
menu.add_cascade(label="settings", menu=submenu4)
submenu4.add_command(label=" open settngs", command=setting)
#buttons 1>play  2>stop  3>pause  music playing 

#play buttons functions

def play1():
    global Play 
    Play = True
    try:  # this oortion checks for the pause.. if it is paused the code will executed and if not it will go to the except
        paused
    except NameError:
        try:
            selected_song= lst.curselection()
            selected_song= int(selected_song[0])
            play_it= playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text']='playing music'+' '+ os.path.basename(filename)
        
           
        except:
            engine=ts.init("sapi5")
            voices= engine.getProperty("voices")
            engine.setProperty("voice:", voices[0].id)
            def play_error(text):
                engine.say(text)
                engine.runAndWait()
            play_error("Dear user, Currently have not selected any song. First add some songs to the play list and then select the song from play list which you want to play")
    else:
        mixer.music.unpause()

def pause1():
    global paused
    paused= True
    try:
        Play
        mixer.music.pause()
        statusbar["text"]="music has been paused"
    except NameError:
        engine=ts.init("sapi5")
        voices= engine.getProperty("voices")
        engine.setProperty("voice:", voices[0].id)
        def pause_error(text):
            engine.say(text)
            engine.runAndWait()
        pause_error("Dear user, Currently you are not playing any song. To pause a song you must first play it")

def stop1():
    try:
        Play
        mixer.music.stop()
        statusbar["text"]=" music has been stopped"
    except NameError:
        engine=ts.init("sapi5")
        voices= engine.getProperty("voices")
        engine.setProperty("voice:", voices[0].id)
        def stop_error(text):
            engine.say(text)
            engine.runAndWait()
        stop_error("Dear user, Currently you are not playing any song. To stop a song you must first play it")


def set_volume(val):
    volume=float(val)/400
    mixer.music.set_volume(volume)
def reverse1():
    try:
        try:
            Play
            mixer.music.play()
        except:
            engine=ts.init("sapi5")
            voices= engine.getProperty("voices")
            engine.setProperty("voice:", voices[0].id)
            def reverse_error(text):
                engine.say(text)
                engine.runAndWait()
            reverse_error("Dear user, Please first play a song to replay it again")
            
    except NameError:
        engine=ts.init("sapi5")
        voices= engine.getProperty("voices")
        engine.setProperty("voice:", voices[0].id)
        def reverse_error(text):
            engine.say(text)
            engine.runAndWait()
        reverse_error("Dear user, Please first play a song to replay it again")

muted= False
def volume_button():
    global muted
    if muted:
        mixer.music.set_volume(0.7)
        mute_button.configure(image=not_mute)
        volume.set(60)
        muted=False
    else:
        mixer.music.set_volume(0)
        mute_button.configure(image=mute)
        volume.set(0)
        muted=True

playlist=[]

def add_t0_play_list(f):
    f=os.path.basename(f)
    index=0
    lst.insert(index, f)
    playlist.insert(index, filename)
    index+=1
def delete_file():
    selected_song= lst.curselection()
    selected_song= int(selected_song[0])
    lst.delete(selected_song)
    playlist.pop(selected_song)

def Acommand():
    engine = ts.init('sapi5')
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
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")

        except Exception:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query

    if __name__ == "__main__":
        speak("Hey Bashir Alam. I am your assistant. Please tell me how may I help you") 
        while True:
        # if 1:
            query = takeCommand().lower()
            if 'stop' in query:
                Play
                mixer.music.stop()
                statusbar["text"]=" music has been stopped"
                break
            elif 'full' in query:
                mixer.music.set_volume(1)
                volume.set(100)
            elif "mute" in query:
                mixer.music.set_volume(0)
                volume.set(0)
            elif 'thank you' in query:
                break
def ASC():
    engine = ts.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()  

            

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")

        except Exception:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query

    if __name__ == "__main__":
        speak("Sir. what you want to change")
        while True:
            query = takeCommand().lower()
    
            if "pink" in query:
                player.configure(background="pink")
                player.configure(background="pink")
                timebar.configure(background= "pink")
                heading.configure(background="pink")
                lst.configure(background="lavender")
                volum.configure(background="pink")
                plist.configure(background="pink")
                speak("background color has been changed to pink")
                break
            elif "green" in query:
                player.configure(background="lightgreen")
                timebar.configure(background= "lightgreen")
                heading.configure(background="lightgreen")
                lst.configure(background="green")
                volum.configure(background="lightgreen")
                plist.configure(background="lightgreen")
                speak("background color has been changed to green")
                break
            elif "white" in query:
                timebar.configure(background= "white")
                heading.configure(background="white")
                lst.configure(background="lavender")
                volum.configure(background="white")
                plist.configure(background="white")
                player.configure(background="white")
                speak("background color has been changed to white")
                break
            else:
                speak("sir. you can select only three colors by using speech commands. you can choose either pink, white or green. for more colors please go to settings")
                break
def recorder():
        t=tk.ThemedTk()
        t.get_themes()
        t.set_theme("blue")
        t.geometry("300x50")
        t.title("Recorder")
        music= PhotoImage('music.icon')
        player.iconbitmap(r'music')
        engine=ts.init("sapi5")
        voices= engine.getProperty("voices")
        engine.setProperty("voice:", voices[0].id)
        def play_error(text):
            engine.say(text)
            engine.runAndWait()
        play_error("Dear user, once you select time, you recording will start")

        def thirty():
            fs = 44100  # this is the frequency sampling; also: 4999, 64000
            seconds = 30  # Duration of recording

            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            print("Starting: Speak now!")
            sd.wait()  # Wait until recording is finished
            print("finished")
            write('output.wav', fs, myrecording)  # Save as WAV file
            os.startfile("output.wav")
        def one():
            fs = 44100  # this is the frequency sampling; also: 4999, 64000
            seconds = 60  # Duration of recording

            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            print("Starting: Speak now!")
            sd.wait()  # Wait until recording is finished
            print("finished")
            write('output.wav', fs, myrecording)  # Save as WAV file
            os.startfile("output.wav")
        def three():
            fs = 44100  # this is the frequency sampling; also: 4999, 64000
            seconds = 180  # Duration of recording

            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            print("Starting: Speak now!")
            sd.wait()  # Wait until recording is finished
            print("finished")
            write('output.wav', fs, myrecording)  # Save as WAV file
            os.startfile("output.wav")
        def five():
            fs = 44100  # this is the frequency sampling; also: 4999, 64000
            seconds = 300  # Duration of recording

            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            print("Starting: Speak now!")
            sd.wait()  # Wait until recording is finished
            print("finished")
            write('output.wav', fs, myrecording)  # Save as WAV file
            os.startfile("output.wav")

        btn1=Button(t, text="30 sec", command=thirty)
        btn1.place(x=0, y=20)
        btn2=Button(t, text="1 mint", command=one)
        btn2.place(x=80, y=20)
        btn3=Button(t, text="3 mint", command=three)
        btn3.place(x=160, y=20)
        btn4=Button(t, text="5 mint", command=five)
        btn4.place(x=240, y=20)
        t.mainloop()
            

#length of audio player 
#play buttons displays and theirs commands

play= PhotoImage( file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\music player\\play.png")
play_button= Button(player, image= play, command=play1, bg="black")
play_button.place(x= 200, y= 30)

pause= PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\music player\\pause.png")
pause_button= Button(player, image=pause,  command=pause1, bg="black")
pause_button.place(x=250, y=30)

stop= PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\music player\\stop.png")
stop_button= Button(player, image=stop, command=stop1, bg="black")
stop_button.place(x=300, y=30)

volume= ttk.Scale(player, from_=0, to =100, orient="horizontal", command=set_volume)
volume.set(60)
volume.place(x= 385, y= 30)

sound= PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\music player\\play.png")

reverse_button= ttk.Button(player, text="Play Again", command=reverse1)
reverse_button.place(x=395, y=75)

mute=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\music player\\mute.png")
not_mute=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\music player\\volume.png")
mute_button=Button(player, image=not_mute, command= volume_button , bg="black")
mute_button.place(x=343, y=30)

add= ttk.Button(player, text="Add Song", command=open_file)
add.place(x=200, y=75)

delt= ttk.Button(player, text="Delete Song", command=delete_file)
delt.place(x=293, y=75)
audio_command=ttk.Button(player, text="Audio Command", command=Acommand)
audio_command.place(x=269, y=115)
say1=ttk.Button(player, text="ASC", command=ASC)
say1.place(x=200, y=115)

record=ttk.Button(player, text="Recorder", command=recorder)
record.place(x=406, y=115)
#list box
lst=Listbox(player, bg="sky blue", width="20")
lst.place(x=5, y=30)



player.mainloop()