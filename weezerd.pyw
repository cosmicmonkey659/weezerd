from tkinter import *
from tkinter import messagebox
import webbrowser

def click():
    messagebox.showerror(title='get weezerd',message='you got weezerd')
    webbrowser.open_new("https://www.youtube.com/watch?v=Kjr7US2Z9aY")

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()