import customtkinter
import tkinter

class Button(customtkinter.CTkButton):
    def __init__(self, master, text, command, sticky, row, column, **kwargs):
        super().__init__(master=master, text=text, width=120, height=40, fg_color="#008fd7", font=("Roboto", 16),
                         text_color="gray94", text_color_disabled="gray60", hover=False)
        self.configure(**kwargs, command=command)
        self.grid(row=row, column=column, sticky=sticky)

    def flash(self):
        self.change_color("#44657e")
        self.after(300, lambda: self.change_color("#008fd7"))

    def change_color(self, color):
        self.configure(fg_color=color)


