import json
import os.path
import pathlib
from tkinter import *
from Pandas import CSV
from tkinter import filedialog
import customtkinter
from PIL import Image
from USB import Usb_drive
import shutil
from datetime import datetime
from UsbError import Message_box
import re
from MainTreeveiw import MainTree
from Widgets import Button
from Warnings import Exception_message, Error_message
from AddDesigns import Add_design
import threading
from UsbManagment import File_mangment
from EarthworkUI import Earthwork, Control
from Frames import Frames
FILES = File_mangment()

USB = Usb_drive()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



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


panda = CSV ()
PATH_SITEWORK_DIR = r"C:\Trimble Synchronizer Data\PC\Trimble SCS900 Data"
PATH_DESKTOP = pathlib.Path("~\\Desktop").expanduser()
# - ----- Program's Titles, Names ----------
PROGRAM_NAME = "File Manager"
FRAME_PICK_YOUR_SYSTEM = "Choose your system"

#--------------------- Tabs Name ------------------
TAB_NAME=["Design Folders", "Config Files", "Machine Files"]

# ---------------Buttons Size------------------------
MAIN_WIDTH = 120
MAIN_HEIGHT = 45
SECONDARY_WIDTH = 120
SECONDARY_HEIGHT = 40
TAB_BUTTON_WIDTH = 120
TAB_BUTTON_HEIGHT = 40
ENTRY_WIDTH = 350
ENTRY_HEIGHT = 40
ENTRY_2_WIDTH = 170
ENTRY_2_HEIGHT = 40


# -------COLORS_--------
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

#  -------------------------------------------------------USB Data -------------------------------------
USB_PATH = Usb_drive.USB_PATH
LIST_DESIGN = USB.list_designs()
LIST_CFG = USB.list_cfg()
LIST_MCG = USB.list_mch()






# ------------------- Images ------------------------
image_add_folder = customtkinter.CTkImage(light_image=Image.open("./Images/add_folder_light.png"), size=(30, 30))
image_create_file = customtkinter.CTkImage(light_image=Image.open("./Images/create_fileV2.png"), size=(30, 30))
image_save_name = customtkinter.CTkImage(light_image=Image.open(("./Images/saveV2.png")), size=(30, 30))
image_teichert_logo_blue = customtkinter.CTkImage(light_image=Image.open("./Images/teichert-Logo_blue_2.png"), size=(180, 180))



class Interface(customtkinter.CTk):
    # ---APP Size-----
    WIDTH = 1280 - 320
    HEIGHT = 800 - 200
    def __init__(self):
        super().__init__()
    # ------- Main Screen SetUP --- - --
        self.title(PROGRAM_NAME)
        self.geometry(f"{Interface.WIDTH}x{Interface.HEIGHT}")
        self.wm_iconbitmap("./Images/teichert-ico.ico")

        # Setting up grid values for the main app window with values as follows (index, weight, minsize)
        grid_main_loop = {"rows":[(0, 0, 50), (1, 0, 300), (2, 0, 10), (3, 3, 0), (4, 0, 20)],
                          "columns":[(0, 0, 20), (1, 0, 300), (2, 0, 45), (3, 2, 0), (4, 0, 20)]}
        self.main_window = Frames(master=self, value=grid_main_loop)


        # Function that calls its self back searching for the USB data
        self.after(4000, self.usb_search)

    #------------------------ Frames ---------------------------
        self.frame_col_1_1()
        self.frame_col_3_1()
        self.frame_message_box()
        self.left_side_app()
        self.tab_1()
        # self.tab_2()
        self.frame_tab_2()
        self.create_buttons_tabs()
        self.create_buttons_add_design()
        self.TAB_NAME()
        self.message_box_m2()
        self.frame_earthwork()


    def event_gcs_900(self):
        try:
            if self.button_gcs_900_choice.cget("fg_color") == NOT_SELECTED:
                self.button_earth_work_choice.configure(fg_color=NOT_SELECTED)
                self.frame_1_earth.grid_forget()
                self.frame_3_1.grid(row=1, column=3, rowspan=3, sticky="sewn")
            else:
                self.frame_1_earth.grid_forget()
                self.frame_3_1.grid(row=1, column=3, rowspan=3, sticky="sewn")
                self.button_earth_work_choice.configure(fg_color=NOT_SELECTED)
                self.button_gcs_900_choice.configure(fg_color=SELECTED_BLUE)
        except AttributeError:
            pass


    def event_earthwork_btn(self):
        try:
            if self.button_earth_work_choice.cget("fg_color") == NOT_SELECTED:
                self.button_gcs_900_choice.configure(fg_color=NOT_SELECTED)
                self.frame_3_1.grid_forget()
                self.frame_1_earth.grid(row=1, column=3, rowspan=3, sticky="sewn")

            else:
                self.button_earth_work_choice.configure(fg_color=SELECTED_BLUE)
                self.button_gcs_900_choice.configure(fg_color=NOT_SELECTED)
                self.frame_3_1.grid_forget()
                self.frame_1_earth.grid(row=1, column=3, rowspan=3, sticky="sewn")
        except AttributeError:
            pass



    def frame_earthwork(self):
        self.frame_1_earth = customtkinter.CTkTabview(master=self, corner_radius=25, height=900,
                                                  segmented_button_selected_color=SELECTED_BLUE,
                                                  segmented_button_unselected_color=NOT_SELECTED,
                                                  segmented_button_selected_hover_color=SELECTED_BLUE)
        self.frame_1_earth.grid(row=1, column=3, rowspan=3, sticky="sewn")
        for button in self.frame_3_1._segmented_button._buttons_dict.values():
            button.configure(width=180, font=FONT)

        self.frame_1_earth.add("Convert to Design")
        # Setting up grid values for the frame with values as follows (index, weight, minsize)

        grid_frame_1_earth = {"rows": [(0, 1, 0)], "columns": [(0, 1, 0)]}
        self.window_frame_1_earth = Frames(master=self.frame_1_earth.tab("Convert to Design"), value=grid_frame_1_earth)

        self.Econrol = Control()

        self.frame_earth_frame = Earthwork(master=self.frame_1_earth.tab("Convert to Design"), row=0, column=0, command=self.Econrol.select_btn)
        self.frame_1_earth.grid_forget()

        #
    # ------------- Lable Frames -----------------
    def frame_col_1_1 (self):
        self.frame_1_1 = customtkinter.CTkFrame(master=self, corner_radius=25, height=215)
        self.frame_1_1.grid(row=3, column=1, sticky="swe")
        # Setting up grid values for the frame with values as follows (index, weight, minsize)
        grid_frame_1_1 = {"rows": [(0, 0, 10), (1, 1, 0), (2, 0, 10), (3, 1, 0), (4, 0, 5)],
                          "columns": [(0, 0, 10), (1, 1, 0), (2, 0, 10)]}
        self.window_1_1 = Frames(master=self.frame_1_1, value=grid_frame_1_1)

        self.frame_1_1.grid_propagate(False)
        return self.frame_1_1


    def frame_col_3_1 (self):
        self.frame_3_1 = customtkinter.CTkTabview(master=self, corner_radius=25, height=900,
                                                  segmented_button_selected_color=SELECTED_BLUE,
                                                  segmented_button_unselected_color=NOT_SELECTED,
                                                  segmented_button_selected_hover_color=SELECTED_BLUE)
        self.frame_3_1.add("USB Files")
        self.frame_3_1.add("Add Design")
        self.frame_3_1.add("Create Point File (.csv)")

        self.frame_3_1.grid(row=1, column=3, rowspan=3, sticky="sewn")
        for button in self.frame_3_1._segmented_button._buttons_dict.values():
            button.configure(width=180,  font=FONT)

        #----------------------------Columns----------------------
        # Setting up grid values for the frame with values as follows (index, weight, minsize)
        grid_usb_files = {"rows": [(0, 0, 5), (1, 0, 40), (2, 0, 5), (3, 5, 0), (4, 0, 10), (5, 1, 0)],
                          "columns": [(0, 0, 5), (1, 1, 0), (2, 1, 0), (3, 1, 0), (4, 0, 5)]}

        grid_add_design = {"rows": [(0, 0, 5), (1, 1, 0), (2, 0, 5), (3, 1, 0), (4, 0, 5), (5, 1, 0), (6, 0, 5),
                                    (7, 1, 0), (8, 0, 5), (9, 1, 0), (10, 0, 5), (11, 1, 0), (12, 0, 5)],
                          "columns": [(0, 0, 10), (1, 2, 0), (2, 0, 10), (3, 1, 0), (4, 0, 10)]}

        grid_create_point = {"rows": [(0, 0, 10), (1, 1, 0), (2, 1, 0), (3, 1, 0), (4, 0, 15), (5, 0, 260), (6, 0, 5)],
                           "columns": [(0, 0, 10), (1, 1, 0), (2, 0, 10), (3, 1, 0), (4, 0, 10)]}

        self.window_3_1_usb_files = Frames(master=self.frame_3_1.tab("USB Files"), value=grid_usb_files)
        self.window_3_1_add_design = Frames(master=self.frame_3_1.tab("Add Design"), value=grid_add_design)
        self.window_3_1_crete_point = Frames(master=self.frame_3_1.tab("Create Point File (.csv)"),
                                             value=grid_create_point)

    def frame_message_box(self):
        self.frame_3_3 = customtkinter.CTkFrame(master=self.frame_3_1.tab("Create Point File (.csv)"), corner_radius=25)
        self.frame_3_3.grid(row=5, column=0, columnspan=5, rowspan=3, sticky="news")

        # Setting up grid values for the frame with values as follows (index, weight, minsize)
        grid_message_box = {"rows": [(0, 0, 5), (1, 1, 0), (2, 1, 0), (3, 1, 0), (4, 1, 0), (5, 0, 5)],
                           "columns": [(0, 0, 5), (1, 2, 0), (2, 0, 5)]}
        self.window_3_1 = Frames(master=self.frame_3_3, value=grid_message_box)

    def frame_tab_2 (self):
        self.frame_tab_2 = customtkinter.CTkTabview(master=self.frame_3_1.tab("USB Files"),
                                                    corner_radius=25,
                                                    segmented_button_selected_color=SELECTED_BLUE,
                                                    segmented_button_unselected_color=NOT_SELECTED,
                                                    segmented_button_selected_hover_color=SELECTED_BLUE,
                                                    command=self.click_segmented_3_but)
        self.frame_tab_2.add("Design Folders")
        self.frame_tab_2.add("Config Files")
        self.frame_tab_2.add("Machine Files")
        self.frame_tab_2.grid(row=3, column=0, sticky="news", columnspan=5, rowspan=1)

        for button in self.frame_tab_2._segmented_button._buttons_dict.values():
            button.configure(width=150, font=FONT_SMALL)

        # Setting up grid values for the frame with values as follows (index, weight, minsize)
        # combine values for the three tabs as it is same grid pattern
        grid_tab_2_combined =  {"rows": [(0, 1, 0),], "columns": [(0, 1, 0), (1, 0, 15)]}
        self.window_tab_2_design = Frames(self.frame_tab_2.tab("Design Folders"), value=grid_tab_2_combined)
        self.window_tab_2_machine = Frames(self.frame_tab_2.tab("Machine Files"), value=grid_tab_2_combined)
        self.window_tab_2_config = Frames(self.frame_tab_2.tab("Config Files"), value=grid_tab_2_combined)

    def create_buttons_tabs (self):
            self.button_tab_2_keep = Button(master=self.frame_3_1.tab("USB Files"), text="Keep", sticky="e",
                                            row=1, column=0, command=self.but_tr_keep,
                                            width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

            self.button_tab_2_delete = Button(master=self.frame_3_1.tab("USB Files"), text="Delete", sticky="e",
                                              row=1, column=1, command=self.but_tr_delete,
                                              width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

            self.button_tab_2_add = Button(master=self.frame_3_1.tab("USB Files"), text="ADD", sticky="e",
                                           row=1, column=2, command=self.but_tr_add,
                                           width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

            self.button_tab_2_create_ds = Button(master=self.frame_3_1.tab("USB Files"), text="Create",
                                                 sticky="e", row=1, column=3, state="disabled",
                                                 command=lambda: [self.but_tr_cr()],
                                                 width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

    def create_buttons_add_design(self):
        self.button_tab_3_save_ds = Button(master=self.frame_3_1.tab("Add Design"), text="Save", sticky="e",
                                           row=1, column=3, width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT,
                                           command=self.event_button_add_design)

        self.button_tab_3_svd_ds = Button(master=self.frame_3_1.tab("Add Design"), text="Add-svd/.svl", sticky="e",
                                          row=5, column=3, width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT,
                                          command=self.event_button_add_file, state="disabled")

        self.button_tab_3_cfg_ds = Button(master=self.frame_3_1.tab("Add Design"), text="Add-.cfg", sticky="e",
                                          row=9, column=3, width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT,
                                          state="disabled", command=self.event_button_cfg)

        self.button_tab_3_create_ds = Button(master=self.frame_3_1.tab("Add Design"), text="Create", sticky="e",
                                             row=11, column=1, width=MAIN_WIDTH, height=TAB_BUTTON_HEIGHT,
                                             command=self.event_button_create_design, state="disabled")


        self.entry_design_name = customtkinter.CTkEntry(master=self.frame_3_1.tab("Add Design"), placeholder_text="Type Design Name",
                                                         corner_radius=15, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        self.entry_design_name.grid(column=1, row=1, sticky="w",)
        # Adding binding to the entry widget to display digital keyboard
        self.entry_design_name.bind("<FocusIn>", self.keyboard_pop_out)


        self.label_tab_3_m = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"), text_color=SELECTED_BLUE,
                                                    font=FONT_BIGGER_LABEL, text="Design Files", width=200)
        self.label_tab_3_m.grid(row=3, column=1, sticky="e")

        self.label_tab_3_svd = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"), font=FONT_LABEL_BLUE,
                                                      text="Surface file  .svd", text_color=SELECTED_BLUE)
        self.label_tab_3_svd.grid(row=5, column=1, sticky="w")

        self.label_tab_3_svd_name = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"), font=FONT_LABEL_BOLD,
                                                           text="Selected  '.svd'", height=5)
        self.label_tab_3_svd_name.grid(row=4, column=1, sticky="e")

        self.label_tab_3_svd_name_selected = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"),
                                                                    font=FONT_LABEL_SMALL, text="None")
        self.label_tab_3_svd_name_selected.grid(row=5, column=1, sticky="e")

        self.label_tab_3_svl = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"), font=FONT_LABEL_BLUE,
                                                      text="Line-work file  .svl", text_color=SELECTED_BLUE)
        self.label_tab_3_svl.grid(row=7, column=1, sticky="w")

        self.label_tab_3_svl_name = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"), font=FONT_LABEL_BOLD,
                                                           text="Selected  '.svl'", height=5)
        self.label_tab_3_svl_name.grid(row=6, column=1, sticky="e")

        self.label_tab_3_svl_name_selected = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"),
                                                                    font=FONT_LABEL_SMALL, text="None")
        self.label_tab_3_svl_name_selected.grid(row=7, column=1, sticky="e")

        self.label_tab_3_cfg = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"), text_color=SELECTED_BLUE,
                                                      font=FONT_LABEL_BLUE, text="Calibration file  .cfg")
        self.label_tab_3_cfg.grid(row=9, column=1, sticky="w")

        self.label_tab_3_cfg_name = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"), height=5,
                                                           font=FONT_LABEL_BOLD, text="Selected '.cfg'")
        self.label_tab_3_cfg_name.grid(row=8, column=1, sticky="e")

        self.label_tab_3_cfg_name_selected = customtkinter.CTkLabel(master=self.frame_3_1.tab("Add Design"),
                                                                    font=FONT_LABEL_SMALL, text="None")
        self.label_tab_3_cfg_name_selected.grid(row=9, column=1, sticky="e")



    def message_box_m2(self):
            self.message_box_tab_2_all = customtkinter.CTkFrame(master=self.frame_3_1.tab("USB Files"),
                                                                corner_radius=25)
            self.message_box_tab_2_all.grid(row=5, column=0, columnspan=4, sticky="news")

            # Setting up grid values for the frame with values as follows (index, weight, minsize)
            grid_message_box_tab_2 = {"rows": [(0, 1, 0), (1, 1, 0), (2, 1, 0), (3, 1, 0)],
                                "columns": [(0, 1, 0), (1, 1, 0)]}
            self.window_message_box_tab_2 = Frames(master=self.message_box_tab_2_all, value=grid_message_box_tab_2)

            # ------------------------------------------------------ Message Box labels ---------------------------------
            self.label_info_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all, text=" -- System info --")
            self.label_info_m2.grid(row=0, column=0, columnspan=2)

            if self.entry_machine_name.get() != "":
                self.label_machine_name_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Machine name :  {self.entry_machine_name.get()}")
            else:
                self.label_machine_name_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Machine name :  None")
            self.label_machine_name_m2.grid(row=1, column=0, sticky="w", padx=35)

            self.label_selected_file_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                text="Selected File:  None")
            self.label_selected_file_m2.grid(row=2, column=0, sticky="w", padx=35)

            self.label_created_file_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                 text="File Created:  None")
            self.label_created_file_m2.grid(row=3, column=0, sticky="w", padx=35)


            try:
                self.label_design_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Design Files: -- {len(LIST_DESIGN)}")
                self.label_design_files_m2.grid(row=1, column=1, sticky="w", padx=15)
            except TypeError:
                self.label_design_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Design Files: --None")
                self.label_design_files_m2.grid(row=1, column=1, sticky="w", padx=15)

            try:
                self.label_config_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Config Files: -- {len(LIST_CFG)}")
                self.label_config_files_m2.grid(row=2, column=1, sticky="w", padx=15)
            except TypeError:
                self.label_config_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Config Files: --None")
                self.label_config_files_m2.grid(row=2, column=1, sticky="w", padx=15)


            try:
                self.label_machine_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                     text=f"Machine Files: --{len(LIST_MCG)}")
                self.label_machine_files_m2.grid(row=3, column=1, sticky="w", padx=15)
            except TypeError:
                self.label_machine_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                     text=f"Machine Files: --None")
                self.label_machine_files_m2.grid(row=3, column=1, sticky="w", padx=15)


    def TAB_NAME(self):

        self.tree_tab_D = MainTree(master=self.frame_tab_2.tab("Design Folders"), data=USB.list_designs())
        self.tree_tab_C = MainTree(master=self.frame_tab_2.tab("Config Files"), data=USB.list_cfg())
        self.tree_tab_M = MainTree(master=self.frame_tab_2.tab("Machine Files"), data=USB.list_mch())

    def click_design(self):
        global LIST_DESIGN
        count = 0
        row_count = 1
        index = 0

        try:
            for find_index in LIST_DESIGN:
                selected_item = self.tree_tab_D.item(self.tree_tab_D.focus())
                if find_index == selected_item["values"]:
                    index = LIST_DESIGN.index(find_index)
                    LIST_DESIGN.pop(index)
        except IndexError or KeyError:
            pass
        for item in range(len(self.tree_tab_D.get_children())):
            selected_item = self.tree_tab_D.get_children()[0]
            self.tree_tab_D.delete(selected_item)
        for record in LIST_DESIGN:
            if count % 2 == 0:
                self.tree_tab_D.insert(parent="", index="end", text=row_count, iid=count,
                                       values=(record[0], record[1]), tags=("odd",))
            else:
                self.tree_tab_D.insert(parent="", index="end", text=row_count, iid=count,
                                       values=(record[0], record[1]), tags=("even",))
            count += 1
            row_count += 1
        try:
            self.tree_tab_D.focus_set()
            self.tree_tab_D.focus(index)
            self.tree_tab_D.selection_add(index)
        except TclError:
            if index > 0:
                self.tree_tab_D.focus_set()
                self.tree_tab_D.focus(index - 1)
                self.tree_tab_D.selection_add(index - 1)
            else:
                pass

    def click_cfg(self):
        global LIST_CFG
        count = 0
        row_count = 1
        index = 0
        try:
            for find_index in LIST_CFG:
                selected_item = self.tree_tab_C.item(self.tree_tab_C.focus())
                if find_index == selected_item["values"]:
                    index = LIST_CFG.index(find_index)
                    LIST_CFG.pop(index)
        except IndexError or KeyError:
                    pass
        for item in range(len(self.tree_tab_C.get_children())):
            selected_item = self.tree_tab_C.get_children()[0]
            self.tree_tab_C.delete(selected_item)
        for record in LIST_CFG:
            if count % 2 == 0:
                self.tree_tab_C.insert(parent="", index="end", text=row_count, iid=count,
                                       values=(record[0], record[1]), tags=("odd",))
            else:
                self.tree_tab_C.insert(parent="", index="end", text=row_count, iid=count,
                                       values=(record[0], record[1]), tags=("even",))
            count += 1
            row_count += 1
        try:
            self.tree_tab_C.focus_set()
            self.tree_tab_C.focus(index)
            self.tree_tab_C.selection_add(index)
        except TclError:
            if index > 0:
                self.tree_tab_C.focus_set()
                self.tree_tab_C.focus(index - 1)
                self.tree_tab_C.selection_add(index - 1)
            else:
                pass


    def click_mch(self):
        global LIST_MCG
        count = 0
        row_count = 1
        index = 0

        try:
            for find_index in LIST_MCG:
                selected_item = self.tree_tab_M.item(self.tree_tab_M.focus())
                if find_index == selected_item["values"]:
                    index = LIST_MCG.index(find_index)
                    LIST_MCG.pop(index)
        except IndexError or KeyError:
            pass
        for item in range(len(self.tree_tab_M.get_children())):
            selected_item = self.tree_tab_M.get_children()[0]
            self.tree_tab_M.delete(selected_item)
        for record in LIST_MCG:
            if count % 2 == 0:
                self.tree_tab_M.insert(parent="", index="end", text=row_count, iid=count,
                                       values=(record[0], record[1]), tags=("odd",))
            else:
                self.tree_tab_M.insert(parent="", index="end", text=row_count, iid=count,
                                       values=(record[0], record[1]), tags=("even",))
            count += 1
            row_count += 1
        try:
            self.tree_tab_M.focus_set()
            self.tree_tab_M.focus(index)
            self.tree_tab_M.selection_add(index)
        except TclError:
            if index > 0:
                self.tree_tab_M.focus_set()
                self.tree_tab_M.focus(index - 1)
                self.tree_tab_M.selection_add(index - 1)
            else:
                pass

    def left_side_app(self):

        # -------------------------------Select System----------------------------------------------------
        self.button_gcs_900_choice = Button(master=self.frame_1_1, text="GCS 900", sticky=None, row=1, column=1,
               width=MAIN_WIDTH, height=MAIN_HEIGHT, command=self.event_gcs_900)

        self.button_earth_work_choice = Button(master=self.frame_1_1, text="Earthwork", sticky=None, row=3, column=1,
                                               width=MAIN_WIDTH, height=MAIN_HEIGHT, command=self.event_earthwork_btn)

        self.button_earth_work_choice.configure(fg_color=NOT_SELECTED)

        #     ------------------------------------ Teichert-Logo -----------------------------------------
        self.image_teichert_logo = customtkinter.CTkLabel(master=self, text="", image=image_teichert_logo_blue)
        self.image_teichert_logo.grid(row=1, column=1, rowspan=2, pady=30)




    def tab_1(self):

        self.button_machine_save = Button(master=self.frame_3_1.tab("Create Point File (.csv)"), text="Save  ",
                                          row=1, column=4, image=image_save_name, compound=RIGHT, sticky=None,
                                          command=lambda: [self.save_machine_name(), self.message_save()],
                                          )

        self.entry_machine_name = customtkinter.CTkEntry(master=self.frame_3_1.tab("Create Point File (.csv)"),
                                                         corner_radius=15, width=ENTRY_WIDTH, height=ENTRY_HEIGHT,
                                                         placeholder_text="Enter Machine Name")
        self.entry_machine_name.grid(column=1, row=1, sticky="w")
        # Adding binding to the entry widget to display digital keyboard
        self.entry_machine_name.bind("<FocusIn>", self.keyboard_pop_out)

        if panda.get_machine_name() != "":
            self.entry_machine_name.insert(0, panda.get_machine_name())
        else:
            pass

    # ------------------------------------------Select Button and Label --------------------------------
        self.button_rover_file = Button(master=self.frame_3_1.tab("Create Point File (.csv)"), text="Select  ",
                                        row=2, column=4, image=image_add_folder, compound=RIGHT, sticky=None,
                                        command=lambda: [self.event_button_select(), self.message_selected()])

        self.label_select_file = customtkinter.CTkLabel(master=self.frame_3_1.tab("Create Point File (.csv)"),
                                                        text="""  Select a Points-File ".csv" """,
                                                        font=FONT_LABEL, width=ENTRY_WIDTH, anchor="sw")
        self.label_select_file.grid(row=2, column=1)

        # -------------------------------------- Create Button and Label -----------------------------------------------
        self.button_create = Button(master=self.frame_3_1.tab("Create Point File (.csv)"), text="Create  ", state="disabled",
                                    row=3, column=4, image=image_create_file, compound=RIGHT, sticky=None,
                                    command=lambda: [panda.create_file(), self.message_created(),
                                    self.event_button_create()])

        self.label_create_file = customtkinter.CTkLabel(master=self.frame_3_1.tab("Create Point File (.csv)"),
                                                        text= """  File in the folder "Points GCS 900" """,
                                                        width=ENTRY_WIDTH, anchor="sw", font=FONT_LABEL)
        self.label_create_file.grid(column=1, row=3)


    # #    --------------------------------------Message-Box -----------------------------------------------------------
        self.label_created = customtkinter.CTkLabel(master=self.frame_3_3, text="--- System Info ---",
                                                    font=FONT_LABEL,
                                                    width=400, anchor="s")
        self.label_created.grid(row=1, column=1)

        if self.entry_machine_name.get() != "":
            self.label_machine_name = customtkinter.CTkLabel(master=self.frame_3_3,
                                                         text=f"Machine name:{' '*17}- {self.entry_machine_name.get()}",
                                                         font=FONT_MESSAGE, width=400, anchor="sw")
        else:
            self.label_machine_name = customtkinter.CTkLabel(master=self.frame_3_3, width=400, anchor="sw",
                                                             text=f"Machine name:{' ' * 17}- None", font=FONT_MESSAGE)
        self.label_machine_name.grid(row=2, column=1, columnspan=2, padx=20)

        self.label_selelected = customtkinter.CTkLabel(master=self.frame_3_3, text=f"Selected File:{' '*20}- File not selected",
                                                       font=FONT_MESSAGE, width=400, anchor="sw")
        self.label_selelected.grid(row=3, column=1)

        self.label_created = customtkinter.CTkLabel(master=self.frame_3_3, text=f"File Created:{' '*21}- File not created",
                                                    font=FONT_MESSAGE,
                                                    width=400, anchor="sw")
        self.label_created.grid(row=4, column=1)



        self.label_copy_rights = customtkinter.CTkLabel(master=self, text="@VITALII_VOVK", font=FONT_COPY_RIGHTS)
        self.label_copy_rights.grid(row=4, column=0, sticky="news")




    def message_save (self):
        new_text_m1 = f"Machine name:{' '*17}- {self.entry_machine_name.get()}"
        new_text_m2 = f"Machine name:  {self.entry_machine_name.get()}"
        self.label_machine_name.configure(text=new_text_m1)
        self.label_machine_name_m2.configure(text=new_text_m2)

    def message_selected(self):
        with open("TempFile.json", "r") as file:
            loaded_file = json.load(file)
        try:
            selected = pathlib.Path(str(loaded_file["Selected File"])).name
            self.button_tab_2_create_ds.configure(state="normal")
        except KeyError:
            selected = ""
        if selected == "":
            new_text_m1 = f"Selected File:{' '*20}- File not selected "
            new_text_m2 = f"Selected File:  None"
            self.label_selelected.configure(text=new_text_m1)
            self.label_selected_file_m2.configure(text=new_text_m2)
        else:
            new_text_m1 = f"Selected File:{' '*20}- {selected}"
            new_text_m2 = f"Selected File:  {selected}"
            self.label_selelected.configure(text=new_text_m1)
            self.label_selected_file_m2.configure(text=new_text_m2)

    def message_created(self):
        new_text ="File Created:          - Desktop/Points GCS 900/"

        self.label_created.configure(text=new_text)
        new_text_m1 = "File Created:          - Desktop/Points GCS 900/"
        new_text_m2 = "File Created:  Desktop/Points GCS 900/"
        self.label_created.configure(text=new_text_m1)
        self.label_created_file_m2.configure(text=new_text_m2)
        Error_message(message="File is created", time=2000)

    def event_button_create(self):
        self.button_tab_2_create_ds.configure(state="disabled")
        self.button_create.configure(state="disabled")

    def save_machine_name(self, **kwargs):
        if kwargs:
            machine_name = kwargs["machine_name"]
            self.entry_machine_name.delete(0, END)
            self.entry_machine_name.insert(0, machine_name)
            self.label_machine_name.configure(f"Machine name:{' '*17}- {machine_name}")
            self.label_machine_name_m2.configure(text=f"Machine name :  {machine_name}")
        else:
            machine_name = self.entry_machine_name.get()
        try:
            with open("Settings.json", "w") as file:
                upload_date = {"Machine Name": machine_name}
                json.dump(upload_date, file, indent=4)
        except Exception as e:
            Exception_message(message=e)
            return



    def event_button_select(self):
        global TAB_NAME, PATH_SITEWORK_DIR
        file_type = (("Point File", "*.csv"), ("All Files", "*.*"))
        # chechking if path is valid
        if pathlib.Path(PATH_SITEWORK_DIR).exists():
            select = filedialog.askopenfilename(initialdir=PATH_SITEWORK_DIR, filetypes=file_type)
        else:
            select = filedialog.askopenfilename(initialdir=PATH_DESKTOP, filetypes=file_type)
        if select.lower().endswith(".csv"):
            self.button_tab_2_create_ds.configure(state="normal")
            self.button_create.configure(state="normal")
            self.frame_tab_2.set(TAB_NAME[0])
            try:
                with open("TempFile.json", "w") as file:
                    upload_file = {"Selected File":select}
                    json.dump(upload_file, file, indent=4)

            except Exception as e:
                Exception_message(message=e)
            return select
        else:
            Error_message(message="File not selected", time=3000)
            return

    def but_tr_keep (self):
        global TAB_NAME
        global LIST_DESIGN
        global LIST_CFG
        global LIST_MCG
        list_pick = [LIST_DESIGN, LIST_CFG, LIST_MCG]
        selected_tab = self.frame_tab_2.get()
        trees = [self.tree_tab_D, self.tree_tab_C, self.tree_tab_M]
        try:
            for tab in range(0, len(TAB_NAME)):
                index = 0
                if TAB_NAME[tab] == selected_tab:
                    count = 0
                    row_count = 1
                    for find_index in list_pick[tab]:
                        selected_item = trees[tab].item(trees[tab].focus())

                        if find_index == selected_item["values"]:
                            index = list_pick[tab].index(find_index)
                            list_pick[tab].pop(index)
                    for item in range(len(trees[tab].get_children())):
                        selected_item = trees[tab].get_children()[0]
                        trees[tab].delete(selected_item)
                    for record in list_pick[tab]:
                        if count % 2 == 0:
                            trees[tab].insert(parent="", index="end", text=row_count, iid=count,
                                              values=(record[0], record[1]), tags=("odd",))
                        else:
                            trees[tab].insert(parent="", index="end", text=row_count, iid=count,
                                              values=(record[0], record[1]), tags=("even",))
                        count += 1
                        row_count += 1
                    try:
                        trees[tab].focus_set()
                        trees[tab].focus(index)
                        trees[tab].selection_add(index)
                    except TclError:
                        if index > 0:
                            trees[tab].focus_set()
                            trees[tab].focus(index-1)
                            trees[tab].selection_add(index-1)
                        else:
                            pass
        except TypeError:
            pass

    def but_tr_delete (self):
        global TAB_NAME
        selected_tab = self.frame_tab_2.get()
        trees = [self.tree_tab_D, self.tree_tab_C, self.tree_tab_M]
        for tab in range(0, len(TAB_NAME)):
            try:
                if TAB_NAME[tab] == selected_tab:
                    selected_item = trees[tab].item(trees[tab].selection()[0])
                    src = pathlib.Path(USB.current_path).joinpath(selected_item["values"][0])
                    src = pathlib.Path(src)
                    dst = pathlib.WindowsPath("~\\Desktop\\USB Deleted Files").expanduser()
                    if not dst.exists():
                        folders = ["Designs", "Machine Files", "Config Files"]
                        for folder in range(0, len(folders)):
                            dst.joinpath(folders[folder]).mkdir(parents=True, exist_ok=True)

                    if src.is_dir():
                        dst_file = dst.joinpath("Designs").joinpath(pathlib.Path(src).name)
                        src_file = src
                        dst_to_pr_folder = dst.joinpath("Designs")
                        self.click_design()
                        self.label_design_files_m2.configure(text=f"Design Files: -- {len(LIST_DESIGN)}")
                        task = threading.Thread(target=FILES.delete_dsn, kwargs={"src": src_file, "dst": dst_file,
                                                      "usb_path": USB_PATH, "dst_parent_folder": dst_to_pr_folder})
                        task.daemon = True
                        task.start()

                    elif src.is_file():
                        source = str(src)
                        if source.lower().endswith(".cfg"):
                            self.click_cfg()
                            self.label_config_files_m2.configure(text=f"Config Files: -- {len(LIST_CFG)}")
                            task = threading.Thread(target=FILES.delete_file, kwargs={"src": src, "dst": dst,
                                                                                     "dst_parent_folder": "Config Files"})
                            task.daemon = True
                            task.start()

                        elif source.lower().endswith(".mch"):
                            self.click_mch()
                            self.label_machine_files_m2.configure(text=f"Machine Files: -- {len(LIST_MCG)}")
                            task = threading.Thread(target=FILES.delete_file, kwargs={"src": src, "dst": dst,
                                                                                      "dst_parent_folder": "Machine Files"})
                            task.daemon = True
                            task.start()
                        else:
                            Error_message(message="File was not deleted")
                    else:
                        Error_message(message="Something went wrong")

            except IndexError:
                Error_message(message="No file to selected", time=3000)



    def but_tr_add(self):
        global TAB_NAME
        global LIST_DESIGN
        global LIST_CFG
        global LIST_MCG
        try:
            if self.frame_tab_2.get() == TAB_NAME[0]:
                selected_folder = filedialog.askdirectory(initialdir=PATH_DESKTOP)
                if selected_folder:
                    folder_name = pathlib.Path(selected_folder).name
                    dst = pathlib.Path(USB.current_path).joinpath(folder_name)
                    match = r"(?i).+?\.(svd|svl)"
                    dst_1 = os.listdir(selected_folder)
                    switch = 0
                    for check_file in dst_1:
                        if re.fullmatch(string=check_file, pattern=match):
                            switch += 1
                    if switch > 0:
                        if dst.exists():
                            shutil.rmtree(dst)
                            shutil.copytree(src=selected_folder, dst=dst)
                        else:
                            shutil.copytree(src=selected_folder, dst=dst)
                        count = 0
                        row_count = 1
                        file_to_append = [os.path.basename(str(dst)),
                                          datetime.fromtimestamp(os.path.getmtime(str(dst))).strftime('%m/%d/%Y')]
                        for i in self.tree_tab_D.get_children():
                            self.tree_tab_D.delete(i)
                        LIST_DESIGN.insert(0, file_to_append)
                        for record in LIST_DESIGN:
                            if count % 2 == 0:
                                self.tree_tab_D.insert(parent="", index="end", text=row_count, iid=count,
                                                       values=(record[0], record[1]), tags=("odd",))
                            else:
                                self.tree_tab_D.insert(parent="", index="end", text=row_count, iid=count,
                                                       values=(record[0], record[1]), tags=("even",))
                            count += 1
                            row_count += 1
                            self.tree_tab_D.focus_set()
                            self.tree_tab_D.focus(0)
                            self.tree_tab_D.selection_add(0)
                    else:
                        Error_message(message="Folder can not be added\n")
                        pass
            elif self.frame_tab_2.get() == TAB_NAME[1] or self.frame_tab_2.get() == TAB_NAME[2]:
                file_type = (("Machine Files", ("*.cfg", "*.mch")), ("All Files", "*.*"))
                selected_file = filedialog.askopenfilename(initialdir=PATH_DESKTOP, filetypes=file_type)
                if selected_file:
                    file_name = pathlib.Path(selected_file).name
                    dst = pathlib.Path(USB.current_path).joinpath(file_name)
                    match = r"(?i).+?\.(cfg|mch)"
                    switch = 0
                    if re.fullmatch(string=selected_file, pattern=match):
                        switch += 1
                    if switch > 0:
                        if dst.exists():
                            dst.unlink()
                            shutil.copy(src=selected_file, dst=dst)
                        else:
                            shutil.copy(src=selected_file, dst=dst)
                        count = 0
                        row_count = 1
                        file_to_append = [os.path.basename(str(dst)),
                                          datetime.fromtimestamp(os.path.getmtime(str(dst))).strftime('%m/%d/%Y')]
                        if re.fullmatch(string=selected_file, pattern=r"(?i).+?\.(cfg)"):
                            for i in self.tree_tab_C.get_children():
                                self.tree_tab_C.delete(i)
                            LIST_CFG.insert(0, file_to_append)
                            for record in LIST_CFG:
                                if count % 2 == 0:
                                    self.tree_tab_C.insert(parent="", index="end", text=row_count, iid=count,
                                                           values=(record[0], record[1]), tags=("odd",))
                                else:
                                    self.tree_tab_C.insert(parent="", index="end", text=row_count, iid=count,
                                                           values=(record[0], record[1]), tags=("even",))
                                count += 1
                                row_count += 1
                                self.tree_tab_C.focus_set()
                                self.tree_tab_C.focus(0)
                                self.tree_tab_C.selection_add(0)
                                if self.frame_tab_2.get() != TAB_NAME[1]:
                                    self.frame_tab_2.set(TAB_NAME[1])
                        else:
                            for i in self.tree_tab_M.get_children():
                                self.tree_tab_M.delete(i)
                            LIST_MCG.insert(0, file_to_append)
                            for record in LIST_MCG:
                                if count % 2 == 0:
                                    self.tree_tab_M.insert(parent="", index="end", text=row_count, iid=count,
                                                           values=(record[0], record[1]), tags=("odd",))
                                else:
                                    self.tree_tab_M.insert(parent="", index="end", text=row_count, iid=count,
                                                           values=(record[0], record[1]), tags=("even",))
                                count += 1
                                row_count += 1
                                self.tree_tab_M.focus_set()
                                self.tree_tab_M.focus(0)
                                self.tree_tab_M.selection_add(0)
                                if self.frame_tab_2.get() != TAB_NAME[2]:
                                    self.frame_tab_2.set(TAB_NAME[2])

                    else:
                        Error_message(message="Could not add selected file")
                        pass
        except Exception as e:
            Exception_message(message=e)

    def but_tr_cr(self):
        try:
            selected = self.tree_tab_D.item(self.tree_tab_D.focus())
            selected_file = selected["values"]
            design_name = selected_file[0]
            path = pathlib.Path(os.path.join(USB_PATH, ".Field-Data"))
            if path.exists():
                design_path = path.joinpath(design_name)
                if path.exists():
                    self.label_selelected.configure(text="Selected File:         - File not selected")
                    self.label_created_file_m2.configure(text="File Created: Desktop/Points GCS 900")
                    self.label_created.configure(text="File Created:         - Desktop/Points GCS 900")
                    # self.button_tab_2_create_ds.configure(state="disabled")
                    self.event_button_create()
                    if not design_path.exists():
                        pathlib.Path(design_path).mkdir()
                        panda.create_file(str(design_path))
                        Error_message(message="Point file is created")
                    else:
                        panda.create_file(str(design_path))
                        Error_message(message="Point file is created")
                else:
                    pass
            else:
                message = "Can not create point file  \n" \
                          "BOX version is below 13.15\n" \
                          "or\n" \
                          "not a GSC900 Backup file"

                Error_message(message=message)
        except IndexError:
            Error_message(message="Select design folder first")


    def click_segmented_3_but(self):
        global TAB_NAME
        with open("TempFile.json", "r") as file:
            loaded_file = json.load(file)
            if self.frame_tab_2.get() == TAB_NAME[0] and self.button_create.cget("state") == "normal":
                try:
                    if re.fullmatch(string=loaded_file["Selected File"], pattern=r".+\.csv"):
                        self.button_tab_2_create_ds.configure(state="normal")
                    else:
                        self.button_tab_2_create_ds.configure(state="disabled")
                except KeyError:
                    self.button_tab_2_create_ds.configure(state="disabled")
            else:
                self.button_tab_2_create_ds.configure(state="disabled")

    def multiple_files_usb(self):
        path = os.listdir(USB_PATH)
        check = r"(?i)Backup.+|All"
        matches = [i for i in path if re.fullmatch(check, i) and pathlib.Path(USB_PATH).joinpath(i).is_dir()]
        if len(matches) > 1:
            files_to_show = []
            for file in matches:
                path = pathlib.Path(USB_PATH).joinpath(file)
                time = datetime.fromtimestamp(path.stat().st_ctime).strftime('%m/%d/%Y')
                files_to_show.append([file, time])
            self.message_tree = Message_box(data=files_to_show, ui_command=self.populate_treeveiw)
        else:
            self.populate_treeveiw()

    def populate_treeveiw(self):
        global LIST_DESIGN, LIST_CFG, LIST_MCG, USB_PATH
        try:
            path = self.message_tree.file_selection()
        except AttributeError:
            path = Usb_drive.USB_PATH

        try:
            USB.current_path = str(pathlib.Path(USB_PATH).joinpath(path))
            USB_PATH = USB.current_path
        except TypeError:
            pass
        check = r"(?i).+MachIne Control Data.+Backup_MHG.+"
        LIST_DESIGN = USB.list_designs()
        LIST_CFG = USB.list_cfg()
        LIST_MCG = USB.list_mch()
        self.TAB_NAME()
        self.message_box_m2()
        try:
            self.catch_m_name(path=USB.current_path)
            self.label_machine_name.configure(text=f"Machine name:{' ' * 17}- {self.entry_machine_name.get()}")
        except AttributeError:
            pass

    def catch_m_name(self, path):
        name_check = r"(?i).+Backup_(.+?)_.+"
        if re.fullmatch(string=path, pattern=name_check):
            machine_name = re.findall(string=path, pattern=name_check)[0]
            self.save_machine_name(machine_name=machine_name)

    def usb_search(self):
        global USB_PATH
        if Usb_drive.USB_PATH == "":
            Usb_drive().detect_usb()
            if Usb_drive.USB_PATH != "":
                USB_PATH =Usb_drive.USB_PATH
                self.multiple_files_usb()
                self.after(2000, self.usb_search)
            else:
                self.after(5000, self.usb_search)
        else:
            if not pathlib.Path(USB_PATH).exists():
                Usb_drive().detect_usb()
                if pathlib.Path(USB_PATH).exists():
                    USB_PATH = Usb_drive.USB_PATH
                    self.multiple_files_usb()
                    self.after(5000, self.usb_search)
                else:
                    Usb_drive.USB_PATH = ""
                    self.after(2000, self.usb_search)
            else:
                self.after(2000, self.usb_search)


#     --------------------------------      Add Design Tab ------------------------------------------------

    def event_button_add_design(self):
        task = threading.Thread(Add_design().save_btn_event(design=self.entry_design_name.get(), usb_path=USB_PATH,
                                                            event_save=self.event_button_save_name))
        task.start()

    def event_button_add_file(self):
        Add_design().add_file(event_svd=self.even_tab3_svd)
        self.change_label_none()

    def event_button_cfg(self):
        Add_design().add_cfg(usb_path=USB_PATH, event_btn=None)
        self.change_label_none()

    def event_button_create_design(self):
        global LIST_DESIGN
        Add_design().create_design()
        self.button_tab_3_svd_ds.configure(state="disabled")
        self.button_tab_3_cfg_ds.configure(state="disabled")
        self.button_tab_3_create_ds.configure(state="disabled")
        # --------------- Add Design to the list -----------
        try:
            count = 0
            row_count = 1
            dst = Add_design.DESIGN_PATH
            file_to_append = [os.path.basename(str(dst)),
                              datetime.fromtimestamp(os.path.getmtime(str(dst))).strftime('%m/%d/%Y')]
            for i in self.tree_tab_D.get_children():
                self.tree_tab_D.delete(i)
            LIST_DESIGN.insert(0, file_to_append)
            for record in LIST_DESIGN:
                if count % 2 == 0:
                    self.tree_tab_D.insert(parent="", index="end", text=row_count, iid=count,
                                           values=(record[0], record[1]), tags=("odd",))
                else:
                    self.tree_tab_D.insert(parent="", index="end", text=row_count, iid=count,
                                           values=(record[0], record[1]), tags=("even",))
                count += 1
                row_count += 1
                self.tree_tab_D.focus_set()
                self.tree_tab_D.focus(0)
                self.tree_tab_D.selection_add(0)
            self.after(1000, lambda: self.change_label_none())
        except (AttributeError, FileNotFoundError):
            Error_message(message="USB not connected")
            return



    def event_button_save_name(self):
        self.button_tab_3_svd_ds.configure(state="normal")
        self.button_tab_3_cfg_ds.configure(state="disabled")
        self.button_tab_3_create_ds.configure(state="disabled")
        self.change_label_none()



    def even_tab3_svd(self):
        self.button_tab_3_create_ds.configure(state="normal")
        self.button_tab_3_cfg_ds.configure(state="normal")

    def change_label_none(self):
        try:
            with open("Add_design.json", "r") as file:
                data = json.load(file)
            svd = pathlib.Path(data["SVD_Path"]).name
            svl = pathlib.Path(data["SVL_Path"]).name
            cfg = pathlib.Path(data["CFG_Path"]).name
            self.label_tab_3_svd_name_selected.configure(text=svd)
            self.label_tab_3_svl_name_selected.configure(text=svl)
            self.label_tab_3_cfg_name_selected.configure(text=cfg)

        except Exception as e:
            Exception_message(message=e)

    # Adding pop out digital keyboard when focus on entry widget
    def keyboard_pop_out(self, event):
        try:
            os.system('wmic process where name="TabTip.exe" delete')
            os.system("C:\\PROGRA~1\\COMMON~1\\MICROS~1\\ink\\tabtip.exe")
        except Exception:
            os.system("C:\\PROGRA~1\\COMMON~1\\MICROS~1\\ink\\tabtip.exe")








































