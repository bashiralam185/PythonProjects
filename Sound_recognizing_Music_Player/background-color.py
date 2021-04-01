from tkinter import *

bc=Tk()
bc.title("Background-color")
bc.geometry("300x300")
bc.configure(background="lightblue")


def back():
    colors=Tk()
    colors.title("colors")
    colors.geometry("50x160")
    def purple():
        bc.configure(background="purple")
    def green():
        bc.configure(background="green")
    def lightgreen():
        bc.configure(background="lightgreen")
    def pink():
        bc.configure(background="pink")
    def lavender():
        bc.configure(background="lavender")
    def white():
        bc.configure(background="white")
    def wheat():
        bc.configure(background="wheat")

    radio= Checkbutton(colors, text=" purple", command=purple).place(x=0, y=0)
    radio= Checkbutton(colors, text=" green", command=green).place(x=0, y=120)
    radio= Checkbutton(colors, text=" lightgreen", command=lightgreen).place(x=0, y=20)
    radio=Checkbutton(colors, text=" pink", command=pink).place(x=0, y=40)
    radio= Checkbutton(colors, text=" lavender", command=lavender).place(x=0, y=60)
    radio= Checkbutton(colors, text=" white", command=white).place(x=0, y=80)
    radio= Checkbutton(colors, text=" wheat", command=wheat).place(x=0, y=100)

    colors.mainloop()


button1= Button(bc, text="background", bg="beige", relief= RIDGE, command=back )
button1.pack()




bc.mainloop()