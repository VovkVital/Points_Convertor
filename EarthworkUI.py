import customtkinter
from Buttons import Button
from Frames import Frames
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
        grid_layout = {"rows": [(0, 0, 20), (1, 1, 0), (2, 0, 20), (3, 1, 0), (4, 0, 20), (5, 1, 0), (6, 0, 20),
                                    (7, 1, 0), (8, 0, 20)],
                       "columns": [(0, 0, 20), (1, 1, 0), (2, 0, 40), (3, 1, 0), (4, 0, 20)]}
        self.grid = Frames(master=self.frame, value=grid_layout)
        self.buttons()

    def buttons(self):
        self.select_button = Button(master=self.frame, text="Select", sticky="n", row=3, column=3)
        self.select_button.configure(width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

        self.confirm_btn = Button(master=self.frame, text="Confirm", sticky="n", row=5, column=3)
        self.confirm_btn.configure(width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

