import customtkinter

#  _________Color _________
SELECTED_BLUE = "#008fd7"
NOT_SELECTED = "#44657e"
FONT_NOT_SELECTED = "gray60"
FONT_SELECTED = "gray94"

# -------------- Fonts -----------------------------
FONT = ("Robot", 15, "bold")
FONT_SMALL = ("Roboto", 14, "bold")
FONT_CONVERSION = ("Roboto", 16)
FONT_BUTTON = ("Roboto", 16)
FONT_LABEL = ("Roboto", 16)
FONT_LABEL_BOLD = ("Roboto", 16, "bold")
FONT_LABEL_SMALL = ("Roboto", 12)
FONT_BIGGER_LABEL = ("Roboto", 24, "bold")
FONT_COPY_RIGHTS = ("Roboto", 6)
FONT_MESSAGE = ("Roboto", 14)
FONT_LABEL_BLUE = ("Roboto", 18, "bold")


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

    def command_flash(self, args):
        self.flash()
        self.after(400, args)

    def change_color(self, color):
        self.configure(fg_color=color)


class Label(customtkinter.CTkLabel):
    text_color = FONT_SELECTED
    text_size = FONT_LABEL

    def __init__(self, master, text, row, column, sticky, **kwargs):
        if kwargs:
            if kwargs["text_color"]:
                self._font_color = kwargs["text_color"]
            if kwargs["font"]:
                self._font_size = kwargs["font"]
        else:
            self._font_color = self.text_color
            self._font_size = self.text_size

        self._text = text
        super().__init__(master=master, text=self._text, text_color=self._font_color, font=self._font_size)

        self.grid(row=row, column=column, sticky=sticky, )
        # self.configure(**kwargs)

    @property
    def label_text(self):
        return self.cget("text")

    @label_text.setter
    def label_text(self, value):
        self.configure(text=value)

    @property
    def label_size(self):
        return self.cget("font")

    @label_size.setter
    def label_size(self, value):
        self.configure(font=value)

    @property
    def label_color(self):
        return self.cget("text_color")

    @label_color.setter
    def label_color(self, value):
        self.configure(text_color=value)

    # alternative constructors for the labels
    @classmethod
    def label_blue_bold(cls, master, text, row, column, sticky):
        return cls(master=master, text=text, row=row, column=column, sticky=sticky, font=FONT_LABEL_BLUE,
                   text_color=SELECTED_BLUE)


    @classmethod
    def label_blue_big(cls, master, text, row, column, sticky):
        return cls(master=master, text=text, row=row, column=column, sticky=sticky, text_color=SELECTED_BLUE,
                   font=FONT_BIGGER_LABEL)

    @classmethod
    def label_small(cls, master, text, row, column, sticky):
        return cls(master=master, text=text, row=row, column=column, sticky=sticky, text_color=FONT_SELECTED,
                   font=FONT_LABEL_SMALL)
