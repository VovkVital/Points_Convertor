import tkinter

import customtkinter
from Widgets import Button, Label
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

DARK = "#2C3639"
HIGHLIGHT_GREEN = "#54B435"
BROWN = "#A27B5C"
CREAM = "#DCD7C9"
LIGHT_GREY = "#EDEDED"
GREY = "#D8D9CF"
SELECTED_BLUE = "#008fd7"
NOT_SELECTED = "#44657e"
FONT_NOT_SELECTED = "gray60"
FONT_SELECTED = "gray94"
ROW_EVEN = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1]


class Earthwork(customtkinter.CTk):
    def __init__(self, master, row, column):
        super().__init__()
        self.frame = customtkinter.CTkFrame(master=master)
        self.frame.grid(sticky="news", row=row, column=column, rowspan=3, columnspan=3)
        grid_layout = {"rows": [(0, 0, 50), (1, 1, 0), (2, 0, 20), (3, 1, 0), (4, 0, 20), (5, 1, 0), (6, 0, 20),
                                    (7, 1, 0), (8, 0, 20)],
                       "columns": [(0, 0, 50), (1, 1, 0), (2, 0, 40), (3, 1, 0), (4, 0, 50)]}
        self.grid = Frames(master=self.frame, value=grid_layout)
        self.widgets()

    def widgets(self):
        self.select_button = Button(master=self.frame, text="Select", sticky="n", row=3, column=3)
        self.select_button.configure(width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

        self.confirm_btn = Button(master=self.frame, text="Confirm", sticky="n", row=5, column=3)
        self.confirm_btn.configure(width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

        self.entry = customtkinter.CTkEntry(master=self.frame, width=ENTRY_WIDTH, height=ENTRY_HEIGHT, placeholder_text="Design Name")
        self.entry.grid(row=5, column=1, columnspan=2, sticky="nw")

        self.label_select = Label.label_blue_bold(master=self.frame, row=3, column=1,
                                                  text="Choose folder with machine files", sticky="nw")

        self.label_format = Label.label_blue_bold(master=self.frame, row=1, column=1,
                                                  text="Select your format preference", sticky="nw")

        self.label_message_row6 = Label.label_small(master=self.frame, row=6, column=1, sticky="nw",
                                                    text="More info is comming")

        self.label_message_row7 = Label.label_small(master=self.frame, row=7, column=1, sticky="nw",
                                                    text="More info is comming")
        self.label_message_row6.grid(columnspan=4)
        self.label_message_row7.grid(columnspan=4)

        radio_var = customtkinter.IntVar(value=1)

        self.btn_radio_dsz = customtkinter.CTkRadioButton(master=self.frame, variable=radio_var, text="DSZ", value=1,
                                                          width=50, hover_color=SELECTED_BLUE, text_color=FONT_SELECTED,
                                                          fg_color=SELECTED_BLUE)
        self.btn_radio_dsz.grid(row=1, column=3, sticky="wn")
        self.btn_radio_vcl = customtkinter.CTkRadioButton(master=self.frame, variable=radio_var, text="VCL", value=2,
                                                          width=50, hover_color=SELECTED_BLUE, text_color=FONT_SELECTED,
                                                          fg_color=SELECTED_BLUE)
        self.btn_radio_vcl.grid(row=1, column=3, sticky="en")


