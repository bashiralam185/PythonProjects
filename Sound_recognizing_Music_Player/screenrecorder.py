import sounddevice as sd
from scipy.io.wavfile import write
import os
from tkinter import *

tk= Tk()
tk.geometry("300x30")

def recorder():
    t=Tk()
    t.geometry("300x40")
    

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

btn=Button(tk, text="recorder", command=recorder)
btn.place(x=0, y=0)

tk.mainloop()

