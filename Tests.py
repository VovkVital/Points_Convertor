import tkinter
import customtkinter
from MainTreeveiw import MainTree

from tkinter import ttk

data = [["Vovk", 1],["Vovk", 2],["Vovk", 3],["Vovk", 4]]



app = tkinter.Tk()
app.title("Second Test")
app.geometry("800x800")
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

frame = customtkinter.CTkFrame(master=app)
frame.grid(row=0, column=0, sticky="news")

tree = MainTree(data=data, master=frame)

app.mainloop()