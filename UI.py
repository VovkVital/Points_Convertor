import glob
import json
import os.path
import pathlib
import time
import tkinter.ttk
from tkinter import *
from PANDAS import CSV
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

USB = Usb_drive()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# -------------- Fonts -----------------------------
FONT = ("Robot", 15, "bold")
FONT_CONVERSION = ("Roboto", 16)
FONT_BUTTON = ("Roboto", 16)
FONT_LABEL = ("Roboto", 16)
FONT_COPY_RIGHTS = ("Roboto", 6)
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
ENTRY_WIDTH = 300
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
image_add_folder = customtkinter.CTkImage(light_image=Image.open("./Images/add_folder_light.png"),
                                          size=(30, 30))
image_create_file = customtkinter.CTkImage(light_image=Image.open("./Images/create_file.png"),
                                           size=(30, 30))

image_teichert_logo = customtkinter.CTkImage(light_image=Image.open("./Images/teichert-logo.png"),
                                          size=(300, 300))
image_teichert_logo_blue = customtkinter.CTkImage(light_image=Image.open("./Images/teichert-Logo_blue_2.png"),
                                          size=(300, 300))



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


    def frame_col_3_1 (self):
        self.frame_3_1 = customtkinter.CTkTabview(master=self, corner_radius=25, height=900,
                                                  segmented_button_selected_color=SELECTED_BLUE)
        self.frame_3_1.add("Simple Point Conversion")
        self.frame_3_1.add("Restore box Conversion")
        self.frame_3_1.grid(row=1, column=3, rowspan=3, sticky ="sewn" )
        self.frame_3_1.tab("Simple Point Conversion").grid_columnconfigure(0, minsize=10)
        self.frame_3_1.tab("Simple Point Conversion").grid_columnconfigure(1, weight=2)
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
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(1, weight=2)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(2, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(3, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(4, minsize=5)

        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(0, minsize=5)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(1, minsize=60)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(2, minsize=5)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(3, weight=5)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(4, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(5, minsize=1)


    def frame_message_box(self):
        self.frame_3_3 = customtkinter.CTkFrame(master=self.frame_3_1.tab("Simple Point Conversion"), corner_radius=25)
        self.frame_3_3.grid(row=5, column=0,columnspan=5, rowspan=3, sticky="news")
        self.frame_3_3.grid_rowconfigure(0, minsize=5)
        self.frame_3_3.grid_rowconfigure(1, weight=1)
        self.frame_3_3.grid_rowconfigure(2, minsize=5)
        self.frame_3_3.grid_columnconfigure(0, minsize=5)
        self.frame_3_3.grid_columnconfigure(1, weight=1)
        self.frame_3_3.grid_columnconfigure(2, minsize=5)


    def frame_tab_2 (self):
        self.frame_tab_2 = customtkinter.CTkTabview(master=self.frame_3_1.tab("Restore box Conversion"), corner_radius=25,
                                                    segmented_button_selected_color=SELECTED_BLUE)
        self.frame_tab_2.add("Design Folders")
        self.frame_tab_2.add("Config Files")
        self.frame_tab_2.add("Machine Files")

        self.frame_tab_2.grid(row=3, column=0, sticky="news", columnspan=5, rowspan=125)

        self.frame_tab_2.tab("Design Folders").grid_columnconfigure(0, minsize=5)
        self.frame_tab_2.tab("Design Folders").grid_columnconfigure(1, weight=3)
        self.frame_tab_2.tab("Design Folders").grid_columnconfigure(2, minsize=5)
        self.frame_tab_2.tab("Design Folders").grid_columnconfigure(3, weight=1)
        self.frame_tab_2.tab("Design Folders").grid_columnconfigure(4, minsize=5)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(0, minsize=5)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(1, weight=1)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(2, minsize=5)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(3, weight=1)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(4, minsize=5)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(5, weight=1)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(6, minsize=5)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(7, weight=1)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(8, minsize=5)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(9, weight=1)
        self.frame_tab_2.tab("Design Folders").grid_rowconfigure(10, minsize=5)

        self.frame_tab_2.tab("Machine Files").grid_columnconfigure(0, minsize=5)
        self.frame_tab_2.tab("Machine Files").grid_columnconfigure(1, weight=3)
        self.frame_tab_2.tab("Machine Files").grid_columnconfigure(2, minsize=5)
        self.frame_tab_2.tab("Machine Files").grid_columnconfigure(3, weight=1)
        self.frame_tab_2.tab("Machine Files").grid_columnconfigure(4, minsize=5)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(0, minsize=5)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(1, weight=1)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(2, minsize=5)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(3, weight=1)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(4, minsize=5)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(5, weight=1)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(6, minsize=5)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(7, weight=1)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(8, minsize=5)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(9, weight=1)
        self.frame_tab_2.tab("Machine Files").grid_rowconfigure(10, minsize=5)

        self.frame_tab_2.tab("Config Files").grid_columnconfigure(0, minsize=5)
        self.frame_tab_2.tab("Config Files").grid_columnconfigure(1, weight=3)
        self.frame_tab_2.tab("Config Files").grid_columnconfigure(2, minsize=5)
        self.frame_tab_2.tab("Config Files").grid_columnconfigure(3, weight=1)
        self.frame_tab_2.tab("Config Files").grid_columnconfigure(4, minsize=5)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(0, minsize=5)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(1, weight=1)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(2, minsize=5)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(3, weight=1)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(4, minsize=5)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(5, weight=1)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(6, minsize=5)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(7, weight=1)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(8, minsize=5)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(9, weight=1)
        self.frame_tab_2.tab("Config Files").grid_rowconfigure(10, minsize=5)


    def create_buttons_tabs (self):
        global TAB_NAME
        tab_name_count = 0
        for tab in TAB_NAME:
            self.button_tab_2_keep = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"), text="Keep", font=FONT_BUTTON,
                                                            width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT,
                                                             command=self.but_tr_keep)
            self.button_tab_2_keep.grid(row=1, column=0, sticky="e")

            self.button_tab_2_delete = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"), text="Delete",
                                                             font=FONT_BUTTON,
                                                             width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT,
                                                               command=self.but_tr_delete)
            self.button_tab_2_delete.grid(row=1, column=1, sticky="e")

            self.button_tab_2_add = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"), text="ADD",
                                                            font=FONT_BUTTON,
                                                            width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT,
                                                            command=self.but_tr_add)
            self.button_tab_2_add.grid(row=1, column=2, sticky="e")
            if TAB_NAME[tab_name_count] == TAB_NAME[0]:
                self.button_tab_2_create_ds = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"),
                                                                   text="Create",
                                                                   font=FONT_BUTTON,
                                                                   width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT,
                                                                   state ="disabled", command=self.but_tr_cr)
                self.button_tab_2_create_ds.grid(row=1, column=3, sticky="se")
                tab_name_count += 1
            else:
                self.button_tab_2_create = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"),
                                                                   text="Create",
                                                                   font=FONT_BUTTON,
                                                                   width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT,
                                                                   state="disabled")
                self.button_tab_2_create.grid(row=1, column=3, sticky="se")
                tab_name_count += 1

            self.message_box_tab_2_all = customtkinter.CTkFrame(master=self.frame_tab_2.tab(tab), height=150)
            self.message_box_tab_2_all.grid(row=9, column=0, columnspan=5, sticky="ew")

            # ------------------------------------Tree view ---------------------------------------


    def TAB_NAME(self):
        global TAB_NAME
        for name in TAB_NAME:
            treestyle = ttk.Style()
            treestyle.theme_use('default')
            treestyle.configure("Treeview", background=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1],
                                foreground=customtkinter.ThemeManager.theme["CTkLabel"]["text_color"][1],
                                fieldbackground=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1],
                                borderwidth=0, font=FONT, rowheight=50)
            treestyle.configure("Treeview.Heading", font=("Roboto", 17),
                                background=(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1]),
                                foreground=FONT_NOT_SELECTED, borderwidth=0,
                                selected=SELECTED_BLUE)
            treestyle.map("Treeview.Heading", background=[('active', customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1])])
            treestyle.map('Treeview',
                          background=[("selected", SELECTED_BLUE)],
                          foreground=[('selected', FONT_SELECTED)])
            # style = ttk.Style()
            #
            # style.theme_use("default")
            #
            # style.configure("Treeview",
            #                 background="#2a2d2e",
            #                 foreground="white",
            #                 rowheight=50,
            #                 fieldbackground="#343638",
            #                 bordercolor="#343638",
            #                 borderwidth=0,
            #                 font = FONT,
            #                 text_color = FONT_SELECTED)
            # style.map('Treeview', background=[('selected', '#22559b')])
            #
            # style.configure("Treeview.Heading",
            #                 background="#565b5e",
            #                 foreground="white",
            #                 relief="flat")
            # style.map("Treeview.Heading",
            #           # font=("Roboto", 15),
            #           background=[('active', '#3484F0')])







            # tree_style = ttk.Style()
            # tree_style.theme_use("clam")
            # tree_style.configure("Treeview",
            #                      background="silver",
            #                      foreground="white",
            #                      rowheight=50,
            #                      fieldbackround="silver",
            #                      font=FONT,
            #                      text_color=FONT_SELECTED)
            #
            # tree_style.configure("Treeview.Heading", font=("Roboto", 15), background="grey")
            # tree_style.map("Treeview", background=[("selected", SELECTED_BLUE)])
            if name == TAB_NAME[0]:
                count = 0
                row_count = 1
                self.tree_tab_D = tkinter.ttk.Treeview(master=self.frame_tab_2.tab(name))
    #             ------------------------------------------Scroll Bar ________________________________
                self.tree_scroll = customtkinter.CTkScrollbar(master=self.frame_tab_2.tab(name), command=self.tree_tab_D.yview)
                self.tree_scroll.grid(row=1, rowspan=7, column=5, sticky="ns")
                self.tree_tab_D.tag_configure("odd", background="#212121")
                self.tree_tab_D.tag_configure("even", background= ROW_EVEN)
                #         --------- Define Columns ______-------
                self.tree_tab_D["columns"] = ("Name", "Date")
                self.tree_tab_D.column("#0", anchor=W, width=45, minwidth=45,  stretch=False)
                self.tree_tab_D.column("Name", anchor=W, width=350, minwidth=100)
                self.tree_tab_D.column("Date", anchor=W, width=40, minwidth=40)
                #      -    -------------- Create Headings --------------------------
                self.tree_tab_D.heading("#0", text="", anchor=W)
                self.tree_tab_D.heading("Name", text="Name", anchor=W)
                self.tree_tab_D.heading("Date", text="Date", anchor=W)
                self.tree_tab_D.grid(row=1, rowspan=7, column=0, columnspan=4, sticky="news",)
                self.tree_tab_D.configure(yscrollcommand=self.tree_scroll.set)

                # ----------------insert in Treeveiw --------------------------------
                for record in USB.list_designs():
                    if count % 2 == 0:
                        self.tree_tab_D.insert(parent="", index="end", text=row_count, iid=count,
                                               values=(record[0], record[1]), tags=("odd",))
                    else:
                        self.tree_tab_D.insert(parent="", index="end", text=row_count, iid=count,
                                               values=(record[0], record[1]), tags=("even",))
                    count += 1
                    row_count += 1



            if name == TAB_NAME[1]:
                count = 0
                row_count = 1
                self.tree_tab_C = tkinter.ttk.Treeview(master=self.frame_tab_2.tab(name))
                #             ------------------------------------------Scroll Bar ________________________________
                self.tree_scroll = customtkinter.CTkScrollbar(master=self.frame_tab_2.tab(name),
                                                              command=self.tree_tab_D.yview)
                self.tree_scroll.grid(row=1, rowspan=7, column=5, sticky="ns")

                self.tree_tab_C.tag_configure("odd", background="#212121")
                self.tree_tab_C.tag_configure("even", background=ROW_EVEN)
                #         --------- Define Columns ______-------
                self.tree_tab_C["columns"] = ("Name", "Date")
                self.tree_tab_C.column("#0", anchor=W, width=45, minwidth=45,  stretch=False)
                self.tree_tab_C.column("Name", anchor=W, width=350, minwidth=100)
                self.tree_tab_C.column("Date", anchor=W, width=40, minwidth=40)
                #      -    -------------- Create Headings --------------------------
                self.tree_tab_C.heading("#0", text="", anchor=W)
                self.tree_tab_C.heading("Name", text="Name", anchor=W)
                self.tree_tab_C.heading("Date", text="Date", anchor=W)
                self.tree_tab_C.grid(row=1, rowspan=7, column=0, columnspan=4, sticky="news")
                self.tree_tab_C.configure(yscrollcommand=self.tree_scroll.set)
                # ----------------insert in Treeveiw --------------------------------
                for record in USB.list_cfg():
                    if count % 2 == 0:
                        self.tree_tab_C.insert(parent="", index="end", text=row_count, iid=count,
                                               values=(record[0], record[1]), tags=("odd",))
                    else:
                        self.tree_tab_C.insert(parent="", index="end", text=row_count, iid=count,
                                               values=(record[0], record[1]), tags=("even",))
                    count += 1
                    row_count += 1

            if name == TAB_NAME[2]:
                count = 0
                row_count = 1
                self.tree_tab_M = tkinter.ttk.Treeview(master=self.frame_tab_2.tab(name))
                #             ------------------------------------------Scroll Bar ________________________________
                self.tree_scroll = customtkinter.CTkScrollbar(master=self.frame_tab_2.tab(name),
                                                              command=self.tree_tab_M.yview)
                self.tree_scroll.grid(row=1, rowspan=7, column=5, sticky="ns")
                self.tree_tab_M.tag_configure("odd", background="#212121")
                self.tree_tab_M.tag_configure("even", background=ROW_EVEN)
                self.tree_tab_M["columns"] = ("Name", "Date")
                self.tree_tab_M.column("#0", anchor=W, width=45, minwidth=45,  stretch=False)
                self.tree_tab_M.column("Name", anchor=W, width=350, minwidth=100)
                self.tree_tab_M.column("Date", anchor=W, width=40, minwidth=40)
                #      -    -------------- Create Headings --------------------------
                self.tree_tab_M.heading("#0", text="", anchor=W)
                self.tree_tab_M.heading("Name", text="Name", anchor=W)
                self.tree_tab_M.heading("Date", text="Date", anchor=W)
                self.tree_tab_M.grid(row=1, rowspan=7, column=0, columnspan=4, sticky="news")
                self.tree_tab_M.configure(yscrollcommand=self.tree_scroll.set)
                # ----------------insert in Treeveiw --------------------------------
                for record in USB.list_mch():
                    if count % 2 == 0:
                        self.tree_tab_M.insert(parent="", index="end", text=row_count, iid=count,
                                               values=(record[0], record[1]), tags=("odd",))
                    else:
                        self.tree_tab_M.insert(parent="", index="end", text=row_count, iid=count,
                                               values=(record[0], record[1]), tags=("even",))
                    count += 1
                    row_count += 1


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
        self.button_gcs_900_choice = customtkinter.CTkButton(master=self.frame_1_1, text="GCS 900", corner_radius=10,
                                                             font=FONT_BUTTON, width=MAIN_WIDTH, height=MAIN_HEIGHT,
                                                             fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
                                                             command=lambda: [self.event_button_system_gcs(),
                                                                              self.message_gcs_900()]
                                                             )
        self.button_gcs_900_choice.grid(row=1, column=1)

        self.button_earth_work_choice = customtkinter.CTkButton(master=self.frame_1_1, text="Earthwork",
                                                                corner_radius=10,
                                                                font=FONT_BUTTON, width=MAIN_WIDTH, height=MAIN_HEIGHT,
                                                                fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
                                                                command=lambda: [self.event_button_system_earth(),
                                                                                 self.message_earthwork()]
                                                                )
        self.button_earth_work_choice.grid(row=3, column=1)

        #     ------------------------------------ Teichert-Logo -----------------------------------------
        self.image_teichert_logo = customtkinter.CTkLabel(master=self, text="", image=image_teichert_logo_blue)
        self.image_teichert_logo.grid(row=1, column=1)

    def tab_1(self):
    # ---------------------------------------------------Machine Name -----------------------------------
        self.button_machine_save = customtkinter.CTkButton(master=self.frame_3_1.tab("Simple Point Conversion"),text="Save  ",
                                                           command=lambda:[self.event_button_save(),
                                                                           self.message_saved_name()],
                                                           fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
                                                           width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT,
                                                           corner_radius=15, font=FONT_BUTTON)
        self.button_machine_save.grid(row=1, column=4)

        self.entry_machine_name = customtkinter.CTkEntry(master=self.frame_3_1.tab("Simple Point Conversion"),
                                                         corner_radius=15, width=ENTRY_WIDTH, height=ENTRY_HEIGHT )
        self.entry_machine_name.grid(column=1, row=1)
        self.entry_machine_name.insert(0, panda.get_machine_name())


    #     #  ----------------------------------- Select_Create_Frame ------------------------------------
    #
        self.button_rover_file = customtkinter.CTkButton(master=self.frame_3_1.tab("Simple Point Conversion"), text="Select  ", image=image_add_folder,
                                                         compound= "right", font=FONT_BUTTON,
                                                         fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
                                                         command=lambda:[self.event_button_select(),
                                                                         self.message_file_selected()],
                                                         corner_radius=15, width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT)
        self.button_rover_file.grid(row=2, column=4)

        self.label_select_file = customtkinter.CTkLabel(master=self.frame_3_1.tab("Simple Point Conversion"), text="Select Point File on the Rover",
                                                        font=FONT_LABEL)
        self.label_select_file.grid(row=2, column=1)


        self.button_create = customtkinter.CTkButton(master=self.frame_3_1.tab("Simple Point Conversion"), text="Create  ",
                                                     image=image_create_file, compound="right", corner_radius=15,
                                                     fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
                                                     command=lambda:[panda.create_file(), self.message_file_created(),
                                                                     self.event_button_create()],
                                                     width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT, font=FONT_BUTTON)
        self.button_create.grid(row=3, column=4)


    # #    --------------------------------------Message-Box -----------------------------------------------------------
        self.label_message_box = customtkinter.CTkLabel(master=self.frame_3_3, text="Message Box", font=FONT_LABEL)
        self.label_message_box.grid(row=1, column=1)

        self.label_copy_rights = customtkinter.CTkLabel(master=self, text="@VITALII_VOVK", font=FONT_COPY_RIGHTS)
        self.label_copy_rights.grid(row=4, column=0, sticky="news")

    # def tab_2(self):
        # -------------------------------------Buttons Tab2 -----------------------------------------------------------
        # self.button_machine_save_tab2 = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"),
        #                                                         text="Save  ",
        #                                                         command=lambda: [self.event_button_save(),
        #                                                                          self.message_saved_name()],
        #                                                         fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
        #                                                         width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT,
        #                                                         corner_radius=15, font=FONT_BUTTON)
        # self.button_machine_save_tab2.grid(row=1, column=2, sticky="w")
        #
        # self.button_rover_file_tab2 = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"),
        #                                                       text="Select  ", image=image_add_folder,
        #                                                       compound="right", font=FONT_BUTTON,
        #                                                       fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
        #                                                       command=lambda: [self.event_button_select(),
        #                                                                        self.message_file_selected()],
        #                                                       corner_radius=15, width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT)
        # self.button_rover_file_tab2.grid(row=1, column=4)
        #
        # # self.button_create_tab2 = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"),
        # #                                                   text="Create File",
        # #                                                   image=image_create_file, compound="right",
        # #                                                   corner_radius=15,
        # #                                                   fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
        # #                                                   command=lambda: [panda.create_file(),
        # #                                                                    self.message_file_created(),
        # #                                                                    self.event_button_create()],
        # #                                                   width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT, font=FONT_BUTTON)
        # # self.button_create_tab2.grid(row=3, column=4)
        #
        # # --------------------------------------------------- Entry Tab2--------------------------------------------
        # self.entry_machine_name_tab2 = customtkinter.CTkEntry(master=self.frame_3_1.tab("Restore box Conversion"),
        #                                                       corner_radius=15, width=ENTRY_2_WIDTH, height=ENTRY_2_HEIGHT)
        # self.entry_machine_name_tab2.grid(column=1, row=1, sticky="w")
        # self.entry_machine_name_tab2.insert(0, panda.get_machine_name())

    def message_file_created (self):
        new_text ="Point File was created\n" \
                  "Desktop - Points GCS 900 "
        self.label_message_box.configure(text=new_text)

    def message_file_selected (self):
        new_text = "Point File was selected\n" \
                  "Project - ??????????   \n" \
                  "Workorder - ??????     \n"
        self.label_message_box.configure(text=new_text)

    def message_saved_name (self):
        machine_name = panda.get_machine_name()
        new_text =f"Machine name saved as\n {machine_name}"

        self.label_message_box.configure(text=new_text)
    def message_gcs_900 (self):
        new_text ="GCS900 - Selected"
        self.label_message_box.configure(text=new_text)

    def message_earthwork (self):
        new_text ="Earthwork - Selected"
        self.label_message_box.configure(text=new_text)

    def event_button_system_gcs(self):
        self.button_gcs_900_choice.configure(fg_color=SELECTED_BLUE, text_color=FONT_SELECTED)
        self.button_earth_work_choice.configure(fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED)

    def event_button_create(self):
        self.button_create.configure(fg_color=SELECTED_BLUE, text_color=FONT_SELECTED)

    def event_button_system_earth(self):
        self.button_earth_work_choice.configure(fg_color=SELECTED_BLUE, text_color=FONT_SELECTED)
        self.button_gcs_900_choice.configure(fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED)

    def event_button_save(self):
        self.button_machine_save.configure(fg_color=SELECTED_BLUE, text_color=FONT_SELECTED)
        machine_name = self.entry_machine_name.get()
        try:
            with open("Settings.json", "w") as file:
                upload_date = {"Machine Name": machine_name}
                print(upload_date)
                json.dump(upload_date, file, indent=4)
        except:
            pass

    def event_button_select(self):
        self.button_rover_file.configure(fg_color=SELECTED_BLUE, text_color=FONT_SELECTED)
        self.button_tab_2_create_ds.configure(state="normal")
        select = filedialog.askopenfilename(initialdir=SELECT_FILE_PATH)
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
            if TAB_NAME[tab] == selected_tab:
                index = 0
                selected_item = trees[tab].item(trees[tab].selection()[0])
                src = pathlib.Path(USB_PATH).joinpath(selected_item["values"][0])
                dst = pathlib.WindowsPath("~\\Desktop\\PC Deleted Files").expanduser()
                if not dst.exists():
                    folders = ["Designs", "Machine Files", "Config Files"]
                    for folder in range(0, len(folders)):
                        dst.joinpath(folders[folder]).mkdir(parents=True, exist_ok=True)

                if src.is_dir():
                    shutil.move(src, dst.joinpath("Designs"))
                    self.click_design()

                if src.is_file():
                    files = glob(os.path.join(str(src.parent), "*.cfg"))
                    for match in range(0, len(files)):
                        if str(src) == files[match]:
                            shutil.move(src, dst.joinpath("Config Files"))
                            self.click_cfg()

                if src.is_file():
                    files = glob(os.path.join(str(src.parent), "*.MCH"))
                    for match in range(0, len(files)):
                        if str(src) == files[match]:
                            shutil.move(src, dst.joinpath("Machine Files"))
                            self.click_mch()

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
                for math_file in range(0, len(list_glob)):
                    if str(selected_file) == list_glob[math_file]:
                        shutil.copy(selected_file, str(USB_PATH))
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


























