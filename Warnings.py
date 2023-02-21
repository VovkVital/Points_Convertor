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



class Message_box(tkinter.ttk.Treeview):

    def __init__(self, data, message, **kwargs):
        self.frame()
        self.flash=Button.flash
        super(). __init__(master=self.message_frame)
        self.data = data
        self.buttons(message=message)
        self.close_frame(time=6)

    def frame(self):
        self.box = customtkinter.CTkToplevel()
        self.box.geometry("500x250")
        self.box.minsize(width=500, height=250)
        self.box.maxsize(width=500, height=250)
        self.box.title("Error")
        self.box.rowconfigure(0, weight=1, minsize=60)
        self.box.rowconfigure(1, weight=2)
        self.box.rowconfigure(2, minsize=10)
        self.box.rowconfigure(3, weight=1, minsize=40)
        self.box.rowconfigure(4, minsize=15)
        self.box.columnconfigure(0, weight=1)
        self.box.columnconfigure(1, weight=1)
        self.message_frame = customtkinter.CTkFrame(master=self.box)
        self.message_frame.grid(row=1, column=0, columnspan=2, sticky="news")
        self.message_frame.rowconfigure(0, weight=1)
        self.message_frame.columnconfigure(0, weight=1)

    def buttons(self, message):
        self.button_accept = Button(master=self.box, text="Accept", sticky=None, row=3, column=0)
        label = Label(master=self.box, text=f"{message}", row=0, column=0)
        label.grid(columnspan=2)
        label.configure(text_color=SELECTED_BLUE, font=FONT_LABEL_ERROR)

    def close_frame(self, time=800):
        self.after(time, lambda: self.box.destroy())





