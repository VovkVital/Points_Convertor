import customtkinter
import tkinter
#  _________ Font _________
FONT_BUTTON = ("Roboto", 16)
FONT_LABEL = ("Roboto", 16)

#  _________Color _________
SELECTED_BLUE = "#008fd7"
NOT_SELECTED = "#44657e"
FONT_NOT_SELECTED = "gray60"
FONT_SELECTED = "gray94"

class Button(customtkinter.CTkButton):
    def __init__(self, master, text, sticky, row, column, **kwargs):
        super().__init__(master=master, text=text, width=120, height=40, fg_color=SELECTED_BLUE, font=FONT_BUTTON,
                         text_color=FONT_SELECTED, text_color_disabled=FONT_NOT_SELECTED, hover=False)
        self.configure(**kwargs)
        self.grid(row=row, column=column, sticky=sticky)
        if kwargs:
            try:
                if kwargs["command"]:
                    self.configure(command=lambda: [self.flash(), kwargs["command"]()])
                else:
                    self.configure(command=self.flash)
            except BaseException:
                self.configure(command=self.flash)
        else:
            self.configure(command=self.flash)




    def flash(self):
        self.change_color(NOT_SELECTED)
        self.after(300, lambda: self.change_color(SELECTED_BLUE))

    def change_color(self, color):
        self.configure(fg_color=color)

class Label(customtkinter.CTkLabel):
    def __init__(self, master, text, row, column, **kwargs):
        super().__init__(master=master, text=text, text_color=FONT_SELECTED, font=FONT_LABEL, **kwargs)
        self.grid(row=row, column=column, **kwargs)
        self.configure(**kwargs)



