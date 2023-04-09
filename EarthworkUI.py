import glob
import re
import tkinter
import num2words as n2w
import shutil
import customtkinter
from Widgets import Button, Label
from Frames import Frames
from tkinter import filedialog
from Warnings import Error_message
import pathlib
import os
import logging

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

PATH_SITEWORK_DIR = r"C:\Trimble Synchronizer Data\PC\Trimble SCS900 Data"
PATH_DESKTOP = pathlib.Path("~\\Desktop").expanduser()
PATH_EARTH_PART_1 = r"ProjectLibrary\Projects"
PATH_EARTH_PART_2 = r"OfficeData\Designs"


class Earthwork(customtkinter.CTk):
    def __init__(self, master, row, column, avail_usb):
        super().__init__()
        self.frame = customtkinter.CTkFrame(master=master)
        self.frame.grid(sticky="news", row=row, column=column, rowspan=3, columnspan=3)
        grid_layout = {"rows": [(0, 0, 50), (1, 1, 0), (2, 0, 20), (3, 1, 0), (4, 0, 20), (5, 1, 0), (6, 0, 20),
                                    (7, 1, 0), (8, 1, 0), (9, 0, 20)],
                       "columns": [(0, 0, 50), (1, 1, 0), (2, 0, 40), (3, 1, 0), (4, 0, 50)]}
        self.grid = Frames(master=self.frame, value=grid_layout)
        self.widgets(avai_usb=avail_usb)
        self.selected_folder = None
        self.logger = logging.getLogger("App_." + __name__)

    def widgets(self, avai_usb):
        self.select_button = Button(master=self.frame, text="Select", sticky="n", row=3, column=3)
        self.select_button.configure(width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT, command=lambda:[self.select_btn(avail_usb=avai_usb)])

        self.confirm_btn = Button(master=self.frame, text="Confirm", sticky="n", row=6, column=3,
                                  command=lambda:[self.creating_design(avail_usb=avai_usb)])
        self.confirm_btn.configure(width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

        self.entry_project = customtkinter.CTkEntry(master=self.frame, width=ENTRY_WIDTH, height=ENTRY_HEIGHT, placeholder_text="Project Name")
        self.entry_project.grid(row=5, column=1, columnspan=2, sticky="nw")

        self.entry_design = customtkinter.CTkEntry(master=self.frame, width=ENTRY_WIDTH, height=ENTRY_HEIGHT,
                                                    placeholder_text="Design Name")
        self.entry_design.grid(row=6, column=1, columnspan=2, sticky="nw")

        self.label_select = Label.label_blue_bold(master=self.frame, row=3, column=1,
                                                  text="Choose folder with machine files", sticky="nw")

        self.label_format = Label.label_blue_bold(master=self.frame, row=1, column=1,
                                                  text="Select your format preference", sticky="nw")

        self.label_message_row6 = Label.label_small(master=self.frame, row=7, column=1, sticky="nw",
                                                    text="More info is comming")

        self.label_message_row7 = Label.label_small(master=self.frame, row=8, column=1, sticky="nw",
                                                    text="More info is comming")
        self.label_message_row6.grid(columnspan=4)
        self.label_message_row7.grid(columnspan=4)

        self.radio_var = customtkinter.IntVar(value=1)

        self.btn_radio_dsz = customtkinter.CTkRadioButton(master=self.frame, variable=self.radio_var, text="DSZ", value=1,
                                                          width=50, hover_color=SELECTED_BLUE, text_color=FONT_SELECTED,
                                                          fg_color=SELECTED_BLUE, hover=None)
        self.btn_radio_dsz.grid(row=1, column=3, sticky="wn")
        self.btn_radio_vcl = customtkinter.CTkRadioButton(master=self.frame, variable=self.radio_var, text="VCL", value=2,
                                                          width=50, hover_color=SELECTED_BLUE, text_color=FONT_SELECTED,
                                                          fg_color=SELECTED_BLUE, hover=None)
        self.btn_radio_vcl.grid(row=1, column=3, sticky="en")


    def select_btn(self, avail_usb):
        if pathlib.Path(PATH_SITEWORK_DIR).exists():
            self.selected_folder = filedialog.askdirectory(initialdir=PATH_SITEWORK_DIR)
        else:
            self.selected_folder = filedialog.askdirectory(initialdir=PATH_DESKTOP)
        # verifying if folder was selected
        if self.selected_folder != "":
            self.validation(path=self.selected_folder)
            if self.source is not None:
                self.design_names(entry_value=self.entry_project.get(), file_folder=self.selected_folder, avail_usb=avail_usb)
        else:
            Error_message(message="Folder not selected")

    def validation(self, path, dsz=True):
        # changing dsz depending on which radio button is selected True if variable 1 and False if variable 2
        if self.radio_var.get() == 2:
            dsz = False

        # Making sure values are not assign to the source
        self.source = None
        # checking if folder has a svd, svl or vcl files
        containing_file = [str(p) for p in pathlib.Path(path).glob("*.*") if
                           re.fullmatch(pattern="(?i).*\.svd$|.*\.svl$|.*\.vcl$", string=str(p))]
        # Counting available files
        svd_count = [f for f in containing_file if f.endswith(".svd")]
        svl_count = [f for f in containing_file if f.endswith(".svl")]
        vcl_count = [f for f in containing_file if f.endswith(".vcl")]
        # determining if design can be created and what files can be used
        if dsz and len(svd_count) == 1 and len(svl_count)==1:
            self.source = [svd_count[0],svl_count[0]]
        elif dsz and len(vcl_count) == 1 and (len(svd_count)!= 1 or len(svl_count != 1)):
            self.source = vcl_count
        elif not dsz and len(vcl_count) == 1:
            self.source = vcl_count
        elif not dsz and len(vcl_count) !=1 and len(svd_count) == 1 and len(svl_count) == 1:
            self.source = [svd_count, svl_count]
        else:
            # converting digit files count to words
            svd_number = n2w.num2words(len(svd_count)).capitalize()
            svl_number = n2w.num2words(len(svl_count)).capitalize()
            vcl_number = n2w.num2words(len(vcl_count)).capitalize()
            # Error message
            message = f"{' '*20}Failed!!!\nFolder should contain\nOne .svd  and One .svl or One .vcl" \
                      f"\ninstead  folder contains\n" \
                      f"{svd_number} .svd,  {svl_number} .svl,  {vcl_number} .vcl"
            # Warning pop our file
            warning = Error_message(message=message, time=10000)
            warning.label.configure(justify="left", anchor="center")

    def design_names(self, entry_value, file_folder, avail_usb):
        #  checkin if folder was selected
        if entry_value == "":
            #  finding project name and design
            project_name = self.name_adjustment(str(pathlib.Path(file_folder).parent.parent.name))
            design_name = self.name_adjustment(str(pathlib.Path(file_folder).name))
            # incrementing design name  if design name is already exist on the USB
            path = pathlib.Path(list(avail_usb)[0]).joinpath(PATH_EARTH_PART_1).joinpath(project_name).joinpath(
                PATH_EARTH_PART_2).joinpath(design_name)
            design_name = self.if_it_exist(path)
            #  checking length of the name to make sure it is fitting inside entry tab
            if len(project_name) > 40:
                project_name_limited = project_name[:40]
                self.entry_project.insert(0, project_name_limited)
            else:
                self.entry_project.insert(0, project_name)
            if len(design_name) > 40:
                design_name_limited = project_name[:40]
                self.entry_project.insert(0, design_name_limited)
            else:
                self.entry_design.insert(0, design_name)
    def creating_design(self, avail_usb):
#          extracting name of the project and design from the entry tabs
        project_name = self.entry_project.get()
        design_name = self.entry_design.get()
        if self.name_validation(project_name=project_name, design_name=design_name):
            path = pathlib.Path(list(avail_usb)[0]).joinpath(PATH_EARTH_PART_1).joinpath(project_name).joinpath(PATH_EARTH_PART_2).joinpath(design_name)
            if not path.exists():
                os.makedirs(path, exist_ok=True)
                self.move_design(source=self.source, dst=str(path))
            else:
                Error_message("Design name is already exist\n change design name\n ")
        else:
            Error_message(message="Invalid name !!!\n\n(No symbols like %!^& etc.)")
            return

    #  correcting name that were extracted from project folders
    def name_adjustment(self, name):
        pattern_1 = r"^[-.]"
        name = re.sub(pattern_1, "_", name)
        pattern = r"[^a-z0-9 ._\-]"
        name = re.sub(pattern, "_", name, flags=re.IGNORECASE)
        name = re.sub(r"\s+", " ", name)
        name = name.strip()
        return name

    # Validating the name again cause user might change after the extraction
    def name_validation (self, project_name, design_name):
        pattern = r"^[^-.]?[a-z0-9 ._\-]*$"
        return bool(re.fullmatch(pattern=pattern, string=project_name, flags=re.IGNORECASE)) and bool(
            re.fullmatch(pattern=pattern, string=design_name, flags=re.IGNORECASE))


    #  increment function if file is already exist in the dst
    def if_it_exist(self, path):
        design_name = path
        pattern = r"-(\d+)$"
        while pathlib.Path(design_name).exists():
            match = re.search(pattern=pattern, string=str(design_name))
            if match and match.group(1):
                counter = int(match.group(1))
                if counter is not None:
                    counter += 1
                    c_pattern =r"\d+$"
                    # replacing the value at the end of the folder name
                    design_name = re.sub(c_pattern, str(counter), str(design_name))
            else:
                design_name = str(design_name) + "-1"
        else:
            return pathlib.Path(design_name).name
    #  creates zip file and renames in dsz if len of the list (source) is more than one otherwise copying
    #  file to the destination directory
    def move_design(self, source:list, dst:str)-> None:
        if len(source) == 1:
            src = source[0]
            shutil.copy(src=src, dst=dst)
        elif len(source) == 2:
            src_1 = source[0]
            src_2 = source[1]
        else:
            self.logger.error(f"Move design function failed with the source: {source} at destination {dst}")
            Error_message(message="Something went wrong\n while creating design")

    def zip_to_dsz(self, file_1, file_2):
        pass















