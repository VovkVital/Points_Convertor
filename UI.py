import glob
import json
import os.path
import pathlib
import time
import tkinter.ttk
from tkinter import *
from Pandas import CSV
from tkinter import filedialog, ttk
import customtkinter
import tkinter
from PIL import Image, ImageTk
import pandas as pd
# import os
from USB import Usb_drive
import shutil
from glob import glob
from datetime import datetime
from UsbError import Message_box
import re
from MainTreeveiw import MainTree
from Buttons import Button
import asyncio

USB = Usb_drive()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



# -------------- Fonts -----------------------------
FONT = ("Robot", 15, "bold")
FONT_CONVERSION = ("Roboto", 16)
FONT_BUTTON = ("Roboto", 16)
FONT_LABEL = ("Roboto", 16)
FONT_COPY_RIGHTS = ("Roboto", 6)
FONT_MESSAGE = ("Roboto", 14)


panda = CSV ()
SELECT_FILE_PATH = r"C:\Trimble Synchronizer Data\PC\Trimble SCS900 Data"
# - ----- Program's Titles, Names ----------
PROGRAM_NAME = "Points Convertor"
FRAME_PICK_YOUR_SYSTEM = "Choose your system"

#--------------------- Tabs Name ------------------
TAB_NAME=["Design Folders", "Config Files", "Machine Files"]

# ---------------Buttons Size------------------------
MAIN_WIDTH = 210
MAIN_HEIGHT = 70
SECONDARY_WIDTH = 120
SECONDARY_HEIGHT = 40
TAB_BUTTON_WIDTH = 120
TAB_BUTTON_HEIGHT = 40
ENTRY_WIDTH = 343
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

image_teichert_logo = customtkinter.CTkImage(light_image=Image.open("./Images/teichert-logo.png"), size=(300, 300))
image_teichert_logo_blue = customtkinter.CTkImage(light_image=Image.open("./Images/teichert-Logo_blue_2.png"),size=(300, 300))



class Interface(customtkinter.CTk):
    # ---APP Size-----
    WIDTH = 1280 - 320
    HEIGHT = 800 - 200
    def __init__(self):
        super().__init__()
    # ------- Main Screen SetUP --- - --
        self.title(PROGRAM_NAME)
        self.geometry(f"{Interface.WIDTH}x{Interface.HEIGHT}")
        self.grid_columnconfigure(0, minsize=20)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, minsize=45)
        self.grid_columnconfigure(3, weight=2)
        self.grid_columnconfigure(4, minsize=20)

        self.grid_rowconfigure(0, minsize=50)
        self.grid_rowconfigure(1, minsize=300)
        self.grid_rowconfigure(2, minsize=10)
        self.grid_rowconfigure(3, weight=3)
        self.grid_rowconfigure(4, minsize=20)

    #------------------------ Frames ---------------------------
        self.frame_col_1_1()
        self.frame_col_3_1()
        self.frame_message_box()
        self.left_side_app()
        self.tab_1()
        # self.tab_2()
        self.frame_tab_2()
        self.create_buttons_tabs()
        self.TAB_NAME()
        self.message_box_m2()

    # ------------- Lable Frames -----------------
    def frame_col_1_1 (self):
        self.frame_1_1 = customtkinter.CTkFrame(master=self, corner_radius=25, height=350)
        self.frame_1_1.grid(row=3, column=1, sticky="swe", pady=0)
        self.frame_1_1.columnconfigure(0, minsize=10)
        self.frame_1_1.columnconfigure(1, weight=1)
        self.frame_1_1.columnconfigure(2, minsize=10)

        self.frame_1_1.rowconfigure(0, minsize=10)
        self.frame_1_1.rowconfigure(1, weight=1)
        self.frame_1_1.rowconfigure(2, minsize=10)
        self.frame_1_1.rowconfigure(3, weight=1)
        self.frame_1_1.rowconfigure(4, minsize=5)
        self.frame_1_1.grid_propagate(False)
        return self.frame_1_1


    def frame_col_3_1 (self):
        self.frame_3_1 = customtkinter.CTkTabview(master=self, corner_radius=25, height=900,
                                                  segmented_button_selected_color=SELECTED_BLUE)
        self.frame_3_1.add("Simple Point Conversion")
        self.frame_3_1.add("Restore box Conversion")
        self.frame_3_1.grid(row=1, column=3, rowspan=3, sticky="sewn")
        self.frame_3_1.tab("Simple Point Conversion").grid_columnconfigure(0, minsize=10)
        self.frame_3_1.tab("Simple Point Conversion").grid_columnconfigure(1, weight=1)
        self.frame_3_1.tab("Simple Point Conversion").grid_columnconfigure(2, minsize=10)
        self.frame_3_1.tab("Simple Point Conversion").grid_columnconfigure(3, weight=1)
        self.frame_3_1.tab("Simple Point Conversion").grid_columnconfigure(4, minsize=10)

        self.frame_3_1.tab("Simple Point Conversion").grid_rowconfigure(0, minsize=10)
        self.frame_3_1.tab("Simple Point Conversion").grid_rowconfigure(1, weight=1)
        self.frame_3_1.tab("Simple Point Conversion").grid_rowconfigure(2, weight=1)
        self.frame_3_1.tab("Simple Point Conversion").grid_rowconfigure(3, weight=1)
        self.frame_3_1.tab("Simple Point Conversion").grid_rowconfigure(4, minsize=15)
        self.frame_3_1.tab("Simple Point Conversion").grid_rowconfigure(5, minsize=260)
        self.frame_3_1.tab("Simple Point Conversion").grid_rowconfigure(6, minsize=5)


        #----------------------------Columns----------------------
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(0, minsize=5)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(1, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(2, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(3, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(4, minsize=5)

        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(0, minsize=5)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(1, minsize=60)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(2, minsize=5)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(3, weight=5)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(4, minsize=10)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(5, weight=1)


    def frame_message_box(self):
        self.frame_3_3 = customtkinter.CTkFrame(master=self.frame_3_1.tab("Simple Point Conversion"), corner_radius=25)
        self.frame_3_3.grid(row=5, column=0, columnspan=5, rowspan=3, sticky="news")
        self.frame_3_3.grid_rowconfigure(0, minsize=5)
        self.frame_3_3.grid_rowconfigure(1, weight=1)
        self.frame_3_3.grid_rowconfigure(2, weight=1)
        self.frame_3_3.grid_rowconfigure(3, weight=1)
        self.frame_3_3.grid_rowconfigure(4, weight=1)
        self.frame_3_3.grid_rowconfigure(5, minsize=5)

        self.frame_3_3.grid_columnconfigure(0, minsize=5)
        self.frame_3_3.grid_columnconfigure(1, weight=1)
        self.frame_3_3.grid_columnconfigure(2, minsize=5)


    def frame_tab_2 (self):
        self.frame_tab_2 = customtkinter.CTkTabview(master=self.frame_3_1.tab("Restore box Conversion"), corner_radius=25,
                                                    segmented_button_selected_color=SELECTED_BLUE,
                                                    command=self.click_segmented_3_but)
        self.frame_tab_2.add("Design Folders")
        self.frame_tab_2.add("Config Files")
        self.frame_tab_2.add("Machine Files")
        self.frame_tab_2.grid(row=3, column=0, sticky="news", columnspan=5, rowspan=1)

        self.frame_tab_2.tab("Design Folders").grid_columnconfigure(0, weight=1)
        self.frame_tab_2.tab("Design Folders").grid_columnconfigure(1, minsize=15)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(0, weight=1)

        self.frame_tab_2.tab("Machine Files").grid_columnconfigure(0, weight=1)
        self.frame_tab_2.tab("Machine Files").grid_columnconfigure(1, minsize=15)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(0, weight=1)

        self.frame_tab_2.tab("Config Files").grid_columnconfigure(0, weight=1)
        self.frame_tab_2.tab("Config Files").grid_columnconfigure(1, minsize=15)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(0, weight=1)


    def create_buttons_tabs (self):
            self.button_tab_2_keep = Button(master=self.frame_3_1.tab("Restore box Conversion"), text="Keep", sticky="e",
                                            row=1, column=0, command=self.but_tr_keep,
                                            width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

            self.button_tab_2_delete = Button(master=self.frame_3_1.tab("Restore box Conversion"), text="Delete", sticky="e",
                                              row=1, column=1, command=self.but_tr_delete,
                                              width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

            self.button_tab_2_add = Button(master=self.frame_3_1.tab("Restore box Conversion"), text="ADD", sticky="e",
                                           row=1, column=2, command=self.but_tr_add,
                                           width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

            self.button_tab_2_create_ds = Button(master=self.frame_3_1.tab("Restore box Conversion"), text="Create",
                                                 sticky="e", row=1, column=3, command=self.but_tr_cr, state="disabled",
                                                 width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)


    def message_box_m2(self):
            self.message_box_tab_2_all = customtkinter.CTkFrame(master=self.frame_3_1.tab("Restore box Conversion"),
                                                                corner_radius=25)
            self.message_box_tab_2_all.grid(row=5, column=0, columnspan=4, sticky="news")
            self.message_box_tab_2_all.rowconfigure(0, weight=1)
            self.message_box_tab_2_all.rowconfigure(1, weight=1)
            self.message_box_tab_2_all.rowconfigure(2, weight=1)
            self.message_box_tab_2_all.rowconfigure(3, weight=1)

            self.message_box_tab_2_all.columnconfigure(0, weight=1)
            self.message_box_tab_2_all.columnconfigure(1, weight=1)

            # ------------------------------------------------------ Message Box labels ---------------------------------
            self.label_info_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all, text=" -- System info --")
            self.label_info_m2.grid(row=0, column=0, columnspan=2)

            self.label_machine_name_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all, text=f"Machine name :  {self.entry_machine_name.get()}")
            self.label_machine_name_m2.grid(row=1, column=0, sticky="w", padx=15)

            self.label_selected_file_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                text="Selected File:  None")
            self.label_selected_file_m2.grid(row=2, column=0, sticky="w", padx=15)

            self.label_created_file_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                 text="File Created:  File not created")
            self.label_created_file_m2.grid(row=3, column=0, sticky="w", padx=15)


            try:
                self.label_design_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Design Files: -- {len(LIST_DESIGN)}")
                self.label_design_files_m2.grid(row=1, column=1, sticky="w", padx=15)
            except TypeError:
                self.label_design_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Design Files: --...")
                self.label_design_files_m2.grid(row=1, column=1, sticky="w", padx=15)

            try:
                self.label_config_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Config Files: -- {len(LIST_CFG)}")
                self.label_config_files_m2.grid(row=2, column=1, sticky="w", padx=15)
            except TypeError:
                self.label_config_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                    text=f"Config Files: --...")
                self.label_config_files_m2.grid(row=2, column=1, sticky="w", padx=15)


            try:
                self.label_machine_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                     text=f"Machine Files: --{len(LIST_MCG)}")
                self.label_machine_files_m2.grid(row=3, column=1, sticky="w", padx=15)
            except TypeError:
                self.label_machine_files_m2 = customtkinter.CTkLabel(master=self.message_box_tab_2_all,
                                                                     text=f"Machine Files: --...")
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
               width=MAIN_WIDTH, height=MAIN_HEIGHT)

        self.button_earth_work_choice = Button(master=self.frame_1_1, text="Earthwork", sticky=None, row=3, column=1,
                                               width=MAIN_WIDTH, height=MAIN_HEIGHT, state="disabled")

        #     ------------------------------------ Teichert-Logo -----------------------------------------
        self.image_teichert_logo = customtkinter.CTkLabel(master=self, text="", image=image_teichert_logo_blue)
        self.image_teichert_logo.grid(row=1, column=1)

    def tab_1(self):

        self.button_machine_save = Button(master=self.frame_3_1.tab("Simple Point Conversion"), text="Save  ",
                                          row=1, column=4, image=image_save_name, compound=RIGHT, sticky=None,
                                          command=lambda: [self.save_machine_name(), self.message_save()],
                                          )

        self.entry_machine_name = customtkinter.CTkEntry(master=self.frame_3_1.tab("Simple Point Conversion"),
                                                         corner_radius=15, width=ENTRY_WIDTH, height=ENTRY_HEIGHT )
        self.entry_machine_name.grid(column=1, row=1)
        self.entry_machine_name.insert(0, panda.get_machine_name())

    # ------------------------------------------Select Button and Label --------------------------------
        self.button_rover_file = Button(master=self.frame_3_1.tab("Simple Point Conversion"), text="Select  ",
                                        row=2, column=4, image=image_add_folder, compound=RIGHT, sticky=None,
                                        command=lambda: [self.event_button_select(), self.message_selected()])

        self.label_select_file = customtkinter.CTkLabel(master=self.frame_3_1.tab("Simple Point Conversion"),
                                                        text="""  Select a Points-File ".csv" """,
                                                        font=FONT_LABEL, width=ENTRY_WIDTH, anchor="sw")
        self.label_select_file.grid(row=2, column=1)

        # -------------------------------------- Create Button and Label -----------------------------------------------
        self.button_create = Button(master=self.frame_3_1.tab("Simple Point Conversion"), text="Create  ", state="disabled",
                                    row=3, column=4, image=image_create_file, compound=RIGHT, sticky=None,
                                    command=lambda: [panda.create_file(), self.message_created(),
                                    self.event_button_create()])

        # self.button_create = customtkinter.CTkButton(master=self.frame_3_1.tab("Simple Point Conversion"), text="Create  ",
        #                                              image=image_create_file, compound="right", corner_radius=15,
        #                                              fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
        #                                              command=lambda:[panda.create_file(), self.message_created(),
        #                                                              self.event_button_create()],
        #                                              width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT, font=FONT_BUTTON,
        #                                              state="disabled")
        # self.button_create.grid(row=3, column=4)

        self.label_create_file = customtkinter.CTkLabel(master=self.frame_3_1.tab("Simple Point Conversion"),
                                                        text= """  Creates file in the folder "Points GCS 900" """,
                                                        width=ENTRY_WIDTH, anchor="sw", font=FONT_LABEL)
        self.label_create_file.grid(column=1, row=3)


    # #    --------------------------------------Message-Box -----------------------------------------------------------
        self.label_created = customtkinter.CTkLabel(master=self.frame_3_3, text="--- System Information ---",
                                                    font=FONT_LABEL,
                                                    width=400, anchor="s")
        self.label_created.grid(row=1, column=1)


        self.label_machine_name = customtkinter.CTkLabel(master=self.frame_3_3,
                                                         text=f"Machine name:     - {self.entry_machine_name.get()}",
                                                         font=FONT_MESSAGE, width=400, anchor="sw")
        self.label_machine_name.grid(row=2, column=1)

        self.label_selelected = customtkinter.CTkLabel(master=self.frame_3_3, text="Selected File:         - File not selected",
                                                       font=FONT_MESSAGE, width=400, anchor="sw")
        self.label_selelected.grid(row=3, column=1)

        self.label_created = customtkinter.CTkLabel(master=self.frame_3_3, text="File Created:          - File not created",
                                                    font=FONT_MESSAGE,
                                                    width=400, anchor="sw")
        self.label_created.grid(row=4, column=1)



        self.label_copy_rights = customtkinter.CTkLabel(master=self, text="@VITALII_VOVK", font=FONT_COPY_RIGHTS)
        self.label_copy_rights.grid(row=4, column=0, sticky="news")




    def message_save (self):
        new_text_m1 = f"Machine name:     - {self.entry_machine_name.get()}"
        new_text_m2 = f"Machine name:  {self.entry_machine_name.get()}"
        self.label_machine_name.configure(text=new_text_m1)
        self.label_machine_name_m2.configure(text=new_text_m2)

    def message_selected(self):
        with open("TempFile.json", "r") as file:
            loaded_file = json.load(file)
        selected = pathlib.Path(str(loaded_file["Selected File"])).name
        self.button_tab_2_create_ds.configure(state="normal")
        if selected == "":
            new_text_m1 = f"Selected File:         - File not selected "
            new_text_m2 = f"Selected File:  None"
            self.label_selelected.configure(text=new_text_m1)
            self.label_selected_file_m2.configure(text=new_text_m2)
        else:
            new_text_m1 =f"Selected File:         - {selected}"
            new_text_m2 = f"Selected File:  {selected}"
            self.label_selelected.configure(text=new_text_m1)
            self.label_selected_file_m2.configure(text=new_text_m2)

    def message_created(self):
        machine_name = panda.get_machine_name()
        new_text ="File Created:          - Desktop/Points GCS 900/"

        self.label_created.configure(text=new_text)
        new_text_m1 = "File Created:          - Desktop/Points GCS 900/"
        new_text_m2 = "File Created:  Desktop/Points GCS 900/"
        self.label_created.configure(text=new_text_m1)
        self.label_created_file_m2.configure(text=new_text_m2)

    def event_button_create(self):
        self.button_tab_2_create_ds.configure(state="disabled")

    def save_machine_name(self):
        machine_name = self.entry_machine_name.get()
        try:
            with open("Settings.json", "w") as file:
                upload_date = {"Machine Name": machine_name}
                json.dump(upload_date, file, indent=4)
        except:
            pass

    def event_button_select(self):
        self.button_tab_2_create_ds.configure(state="normal")
        self.button_create.configure(state="normal")
        select = filedialog.askopenfilename(initialdir=SELECT_FILE_PATH)
        # self.button_create.configure(fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED)
        try:
            with open ("TempFile.json", "w") as file:
                upload_file = {"Selected File":select}
                json.dump(upload_file, file, indent =4)

        except:
            print("Except  file explorer Error  ")

        return select

    def but_tr_keep (self):
        global TAB_NAME
        global LIST_DESIGN
        global LIST_CFG
        global LIST_MCG
        list_pick = [LIST_DESIGN, LIST_CFG, LIST_MCG]
        selected_tab = self.frame_tab_2.get()
        trees = [self.tree_tab_D, self.tree_tab_C, self.tree_tab_M]
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

    def but_tr_delete (self):
        global TAB_NAME
        selected_tab = self.frame_tab_2.get()
        trees = [self.tree_tab_D, self.tree_tab_C, self.tree_tab_M]
        for tab in range(0, len(TAB_NAME)):
            try:
                if TAB_NAME[tab] == selected_tab:
                    index = 0
                    selected_item = trees[tab].item(trees[tab].selection()[0])
                    src = pathlib.Path(USB.current_path).joinpath(selected_item["values"][0])
                    src = pathlib.Path(src)
                    dst = pathlib.WindowsPath("~\\Desktop\\PC Deleted Files").expanduser()
                    if not dst.exists():
                        folders = ["Designs", "Machine Files", "Config Files"]
                        for folder in range(0, len(folders)):
                            dst.joinpath(folders[folder]).mkdir(parents=True, exist_ok=True)

                    if src.is_dir():
                        if dst.joinpath("Designs").joinpath(pathlib.Path(src).name).exists():
                            shutil.rmtree(dst.joinpath("Designs").joinpath(pathlib.Path(src).name))
                            shutil.move(src, dst.joinpath("Designs"))
                            self.click_design()
                            self.label_design_files_m2.configure(text=f"Design Files: -- {len(LIST_DESIGN)}")
                        else:
                            shutil.move(src, dst.joinpath("Designs"))
                            self.click_design()
                            self.label_design_files_m2.configure(text=f"Design Files: -- {len(LIST_DESIGN)}")

                    if src.is_file():
                        files = glob(os.path.join(str(src.parent), "*.cfg"))
                        for match in range(0, len(files)):
                            if str(src) == files[match]:
                                if dst.joinpath("Config Files").joinpath(pathlib.Path(src).name).exists():
                                    pathlib.Path(dst.joinpath("Config Files").joinpath(pathlib.Path(src).name)).unlink()
                                    shutil.move(src, dst.joinpath("Config Files"))
                                    self.click_cfg()
                                    self.label_config_files_m2.configure(text=f"Config Files: -- {len(LIST_CFG)}")
                                else:
                                    shutil.move(src, dst.joinpath("Config Files"))
                                    self.click_cfg()
                                    self.label_config_files_m2.configure(text=f"Config Files: -- {len(LIST_CFG)}")

                    if src.is_file():
                        files = glob(os.path.join(str(src.parent), "*.MCH"))
                        for match in range(0, len(files)):
                            if str(src) == files[match]:
                                if dst.joinpath("Machine Files").joinpath(pathlib.Path(src).name).exists():
                                    pathlib.Path(dst.joinpath("Machine Files").joinpath(pathlib.Path(src).name)).unlink()
                                    shutil.move(src, dst.joinpath("Machine Files"))
                                    self.click_mch()
                                    self.label_machine_files_m2.configure(text=f"Config Files: -- {len(LIST_MCG)}")
                                else:
                                    shutil.move(src, dst.joinpath("Machine Files"))
                                    self.click_mch()
                                    self.label_machine_files_m2.configure(text=f"Config Files: -- {len(LIST_MCG)}")
            except IndexError:
                pass
                # trees[tab].focus_set()
                # trees[tab].focus(0)
                # trees[tab].selection_add(0)



    def but_tr_add(self):
        global TAB_NAME
        global LIST_DESIGN
        global LIST_CFG
        global LIST_MCG
        list_pick = [LIST_DESIGN, LIST_CFG, LIST_MCG]
        selected_file = pathlib.Path(filedialog.askopenfilename(initialdir=pathlib.Path("~\\Desktop").expanduser()))
        selected_tab = self.frame_tab_2.get()
        trees = [self.tree_tab_D, self.tree_tab_C, self.tree_tab_M]
        for tab in range(0, len(TAB_NAME)):
            if TAB_NAME[1] == selected_tab:
                list_glob = glob(os.path.join(str(selected_file.parent), "*.cfg"))
                self.label_config_files_m2.configure(text=f"Config Files: -- {len(LIST_CFG)}")
                for math_file in range(0, len(list_glob)):
                    if str(selected_file) == list_glob[math_file]:
                        shutil.copy(selected_file, str(USB.current_path))
                        file_to_append = [os.path.basename(selected_file), datetime.fromtimestamp(os.path.getmtime(selected_file)).strftime('%m/%d/%Y')]
                        list_pick[tab].append(file_to_append)
                        count = 0
                        row_count = 1
                        for item in range(len(trees[tab].get_children())):
                            item = trees[tab].get_children()[0]
                            trees[tab].delete(item)
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
            if TAB_NAME[2] == selected_tab:
                list_glob = glob(os.path.join(str(selected_file.parent), "*.MCH"))
                self.label_machine_files_m2.configure(text=f"Config Files: -- {len(LIST_MCG)}")
                for math_file in range(0, len(list_glob)):
                    if str(selected_file) == list_glob[math_file]:
                        shutil.copy(selected_file, str(USB_PATH))
                        file_to_append = [os.path.basename(selected_file),
                                          datetime.fromtimestamp(os.path.getmtime(selected_file)).strftime('%m/%d/%Y')]
                        list_pick[tab].append(file_to_append)
                        count = 0
                        row_count = 1
                        for item in range(len(trees[tab].get_children())):
                            item = trees[tab].get_children()[0]
                            trees[tab].delete(item)
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
    def but_tr_cr(self):
        selected = self.tree_tab_D.item(self.tree_tab_D.focus())
        selected_file = selected["values"]
        design_name = selected_file[0]
        path = pathlib.Path(os.path.join(USB.detect_usb(), ".Field-Data"))
        self.label_selelected.configure(text="Selected File:         - File not selected")
        self.label_selected_file_m2.configure(text="File Created: File not selected")
        self.button_tab_2_create_ds.configure(state="disabled")
        if path.exists():
            design_path = path.joinpath(design_name)
            if path.exists():
                if not design_path.exists():
                    pathlib.Path(design_path).mkdir()
                    panda.create_file(str(design_path))
                else:
                    panda.create_file(str(design_path))

            else:
                pass
    def click_segmented_3_but(self):
        global TAB_NAME
        with open("TempFile.json", "r") as file:
            loaded_file = json.load(file)
        for active_tab in TAB_NAME:
            selected_tab =self.frame_tab_2.get()
            if selected_tab != "Design Folders":
                self.button_tab_2_create_ds.configure(state="disabled")
            else:
                try:
                    if bool(loaded_file["Selected File"]):
                        self.button_tab_2_create_ds.configure(state="normal")
                    else:
                        pass
                except KeyError:
                    self.button_tab_2_create_ds.configure(state="disabled")
    async def multiple_files_usb(self):
        path = os.listdir(USB_PATH)
        check = r"Backup.+|[aA][lL][lL]"
        matches = [i for i in path if re.fullmatch(check, i)]
        if len(matches) > 1:
            files_to_show = []
            for file in matches:
                path = pathlib.Path(USB_PATH).joinpath(file)
                time = datetime.fromtimestamp(path.stat().st_ctime).strftime('%m/%d/%Y')
                files_to_show.append([file, time])
            self.message_tree = Message_box(data=files_to_show, ui_command=self.populate_treeveiw)

    def populate_treeveiw(self):
        global LIST_DESIGN
        global LIST_CFG
        global LIST_MCG
        global USB_PATH
        path = self.message_tree.file_selection()
        try:
            USB.current_path = str(pathlib.Path(USB_PATH).joinpath(path))
        except TypeError:
            pass
        LIST_DESIGN = USB.list_designs()
        LIST_CFG = USB.list_cfg()
        LIST_MCG = USB.list_mch()
        self.TAB_NAME()




























