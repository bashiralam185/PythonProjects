from tkinter import *
import time
tk=Tk()
tk.geometry("300x300")


seconds=0
minutes=0
list=[0]
for i in range(0, len(list)):
    while True:
        item=str(minutes)+":" +str(seconds)
        list.append(item)
        seconds=seconds+1
        time.sleep(1)
        if seconds==60:
            seconds=0
            minutes+=1
        break
    timebar= Label(tk, text="time")
    timebar.place(x=0, y=0)
    timebar['text']=list[-1]
list1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
times=Label(tk, text="time")
times.place(x=0, y=20)
for i in list1:
    index=0
    times['text']=i
    time.sleep(1)
    index+=1
    



tk.mainloop()