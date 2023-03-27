import customtkinter
from Buttons import Button
#  Fonts #
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

# - Sizes #
MAIN_WIDTH = 120
MAIN_HEIGHT = 45
TAB_BUTTON_WIDTH = 120
TAB_BUTTON_HEIGHT = 40
ENTRY_WIDTH = 350
ENTRY_HEIGHT = 40
ENTRY_2_WIDTH = 170
ENTRY_2_HEIGHT = 40

class Earthwork(customtkinter.CTk):
    def __init__(self, master, row, column):
        super().__init__()
        self.frame = customtkinter.CTkFrame(master=master)
        self.frame.grid(sticky="news", row=row, column=column, rowspan=3, columnspan=3)
        self.frame.grid_columnconfigure(0, minsize=20)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, minsize=40)
        self.frame.grid_columnconfigure(3, weight=1)
        self.frame.grid_columnconfigure(4, minsize=20)

        self.frame.grid_rowconfigure(0, minsize=20)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, minsize=20)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, minsize=20)
        self.frame.grid_rowconfigure(5, weight=1)
        self.frame.grid_rowconfigure(6, minsize=20)
        self.frame.grid_rowconfigure(7, weight=1)
        self.frame.grid_rowconfigure(8, minsize=20)
        self.buttons()


    def buttons(self):
        self.select_button = Button(master=self.frame, text="Select", sticky="n", row=3, column=3)
        self.select_button.configure(width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

        self.confirm_btn = Button(master=self.frame, text="Confirm", sticky="n", row=5, column=3)
        self.confirm_btn.configure(width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

