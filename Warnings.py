import asyncio
import tkinter
from tkinter import ttk
import customtkinter
from Buttons import Button, Label
from USB import Usb_drive
import json
# _______ Colors _________
SELECTED_BLUE = "#008fd7"
NOT_SELECTED = "#44657e"
FONT_NOT_SELECTED = "gray60"
FONT_SELECTED = "gray94"
ROW_EVEN = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1]
# ________ Font ___________
FONT_HEADER = ("Roboto", 17, "bold")
FONT_TABLE = ("Roboto", 15, "bold")
FONT_LABEL_ERROR = ("Roboto", 18, "bold")
# _________ Tab Names _______
TAB_NAME = ["Design Folders", "Config Files", "Machine Files"]



class Error_message(tkinter.ttk.Treeview):

    def __init__(self, message, time, **kwargs):
        self.frame()
        self.flash=Button.flash
        super(). __init__(master=self.box)
        self.buttons(message=message)
        self.close_frame()


    def frame(self):
        self.box = customtkinter.CTkToplevel()
        self.box.geometry("500x250")
        self.box.minsize(width=500, height=250)
        self.box.maxsize(width=500, height=250)
        self.box.title("Error")
        self.box.rowconfigure(0, weight=1)
        self.box.rowconfigure(1, minsize=60)
        self.box.rowconfigure(2, minsize=20)
        self.box.columnconfigure(0, weight=1)


    def buttons(self, message):
        self.button_accept = Button(master=self.box, text="Accept", sticky=None, row=1, column=0,
                                    command=self.box.destroy)
        label = Label(master=self.box, text=f"{message}", row=0, column=0)
        label.configure(text_color=SELECTED_BLUE, font=FONT_LABEL_ERROR)

    def close_frame(self, time=8000):
        self.after(time, lambda: self.box.destroy())


class Exception_message(tkinter.ttk.Treeview):
    def __init__(self, message, time, **kwargs):
        self.frame()
        self.flash = Button.flash
        super().__init__(master=self.box)
        self.buttons()
        self.text_box(message=message)
        self.close_frame()
    def frame(self):
        self.box = customtkinter.CTkToplevel()
        self.box.geometry("500x250")
        self.box.minsize(width=500, height=250)
        self.box.maxsize(width=500, height=250)
        self.box.title("Error")
        self.box.rowconfigure(0, weight=1)
        self.box.rowconfigure(1, minsize=60)
        self.box.rowconfigure(2, minsize=20)
        self.box.columnconfigure(0, weight=1)
    def buttons(self):
        self.button_accept = Button(master=self.box, text="Accept", sticky=None, row=1, column=0,
                                    command=self.box.destroy)
    def close_frame(self, time=8000):
        self.after(time, lambda: self.box.destroy())
    def text_box(self, message):
        self.text_frame = customtkinter.CTkTextbox(master=self.box, wrap="word", state="normal", font=FONT_LABEL_ERROR,
                                                   text_color=SELECTED_BLUE, border_spacing=10)
        self.text_frame.grid(row=0, column=0, sticky="nsew")
        self.text_frame.insert("0.0", f"{message}")
        self.text_frame.configure(state="disabled")




