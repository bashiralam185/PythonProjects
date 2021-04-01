from tkinter import *
from ttkthemes import themed_tk as tk
from PIL import ImageTk, Image
from tkinter import ttk

assistant=tk.ThemedTk()
assistant.get_themes()
assistant.configure(background="teal")
assistant.set_theme("keramik") # ( blue, aquativo, elegance, clearlooks, keramik, radiance, winxpblue, black, )
assistant.title("Personal Assistant")
assistant.geometry("400x200")
def main():
    pass
def outlook():
    pass
def pc():
    pass
def off():
    pass
main_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\personal assistant\\main.png")
btn1=Button(assistant, text="", image=main_image, command=main, bg="teal")
btn1.place(x=140, y=30)
world_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\personal assistant\\worldwide.png")
btn2=ttk.Button(assistant, text="", image=world_image, command=online)
btn2.place(x=50, y=20)
outlook_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\personal assistant\\outlook.png")
btn3=ttk.Button(assistant, text="", image=outlook_image, command=outlook)
btn3.place(x=50, y=136)
pc_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\personal assistant\\pc.png")
btn4=ttk.Button(assistant, text="", image=pc_image, command=pc)
btn4.place(x=335, y=20)
exit_image=PhotoImage(file="C:\\Users\\bashir.alam\\Documents\\subjects\\it\\projects\\personal assistant\\power.png")
btn5=ttk.Button(assistant, text="", image=exit_image, command=off)
btn5.place(x=335, y=136)

assistant.mainloop()
