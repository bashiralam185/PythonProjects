from tkinter import *
from pygame import mixer

setting= Tk()
mixer.init()
setting.title("Settings")
setting.geometry("400x30")

#changing the icon
music= PhotoImage('music.icon')
setting.iconbitmap(r'music')

#buttons on the setting menu
def volume():
    def set_volume(val):
        volume=int(val)/100
        mixer.music.set_volume(volume)
    v=Tk()
    v.title("volume")
    volume= Scale(v, from_=0, to =100, orient="horizontal", command=set_volume).pack()
    
    
    


    v.mainloop()

button1= Button(setting, text="Volume", bg="beige", relief= RIDGE, command=volume )
button1.place(x=0, y=1)


setting.mainloop()