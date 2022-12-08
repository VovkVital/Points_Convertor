import json
import tkinter.ttk
from tkinter import *
from PANDAS import CSV
from tkinter import filedialog, ttk
import customtkinter
import tkinter
from PIL import Image, ImageTk
import pandas as pd
import os
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# -------------- Fonts -----------------------------
FONT = ("Futura", 10, "bold")
FONT_CONVERSION = ("Roboto", 16)
FONT_BUTTON = ("Roboto", 16)
FONT_LABEL = ("Roboto", 16)
FONT_COPY_RIGHTS = ("Roboto", 6)
panda = CSV ()
SELECT_FILE_PATH = r"C:\Trimble Synchronizer Data\PC\Trimble SCS900 Data"
# - ----- Program's Titles, Names ----------
PROGRAM_NAME = "Points Convertor"
FRAME_PICK_YOUR_SYSTEM = "Choose your system"

# ---------------Buttons Size------------------------
MAIN_WIDTH=210
MAIN_HEIGHT=70
SECONDARY_WIDTH=150
SECONDARY_HEIGHT=50
TAB_BUTTON_WIDTH =120
TAB_BUTTON_HEIGHT=40
ENTRY_WIDTH=350
ENTRY_HEIGHT=50




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


# ------------------- Images ------------------------
image_add_folder = customtkinter.CTkImage(light_image=Image.open("./Images/add_folder_light.png"),
                                          size=(30, 30))
image_create_file = customtkinter.CTkImage(light_image=Image.open("./Images/create_file.png"),
                                           size=(45, 45))

image_teichert_logo = customtkinter.CTkImage(light_image=Image.open("./Images/teichert-logo.png"),
                                          size=(300, 300))
image_teichert_logo_blue = customtkinter.CTkImage(light_image=Image.open("./Images/teichert-Logo_blue_2.png"),
                                          size=(300, 300))







class Interface(customtkinter.CTk):
    # ---APP Size-----
    WIDTH = 1280
    HEIGHT = 800
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
        self.tab_2()
        self.frame_tab_2()
        self.control_tab_2()


    #------------------------ App Logo---------------------------

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
        self.frame_3_1.tab("Simple Point Conversion").grid_rowconfigure(5, minsize=460)
        self.frame_3_1.tab("Simple Point Conversion").grid_rowconfigure(6, minsize=5)



        #----------------------------Columns----------------------
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(0, minsize=5)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(1, weight=2)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(2, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(3, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_columnconfigure(4, minsize=5)

        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(0, minsize=5)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(1, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(2, minsize=5)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(3, weight=5)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(4, weight=1)
        self.frame_3_1.tab("Restore box Conversion").grid_rowconfigure(5, minsize=1)

    def frame_message_box(self):
        self.frame_3_3 = customtkinter.CTkFrame(master=self.frame_3_1.tab("Simple Point Conversion"), corner_radius=25)
        self.frame_3_3.grid(row=5, column=0,columnspan=5, rowspan=3 , sticky="news")
        self.frame_3_3.grid_rowconfigure(0, minsize=5)
        self.frame_3_3.grid_rowconfigure(1, weight=1)
        self.frame_3_3.grid_rowconfigure(2, minsize=5)
        self.frame_3_3.grid_columnconfigure(0, minsize=5)
        self.frame_3_3.grid_columnconfigure(1, weight=1)
        self.frame_3_3.grid_columnconfigure(2, minsize=5)


    def frame_tab_2 (self):
        self.frame_tab_2 = customtkinter.CTkTabview(master=self.frame_3_1.tab("Restore box Conversion"), corner_radius=25,
                                                    segmented_button_selected_color=SELECTED_BLUE)
        self.frame_tab_2.add("Designs Folders")
        self.frame_tab_2.add("Config Files")
        self.frame_tab_2.add("Machine Files")

        self.frame_tab_2.grid(row=3, column=1, sticky="news", columnspan=4, rowspan=125)

        self.frame_tab_2.tab("Designs Folders").grid_columnconfigure(0, minsize=5)
        self.frame_tab_2.tab("Designs Folders").grid_columnconfigure(1, weight=3)
        self.frame_tab_2.tab("Designs Folders").grid_columnconfigure(2, minsize=5)
        self.frame_tab_2.tab("Designs Folders").grid_columnconfigure(3, weight=1)
        self.frame_tab_2.tab("Designs Folders").grid_columnconfigure(4, minsize=5)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(0, minsize=5)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(1, weight=1)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(2, minsize=5)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(3, weight=1)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(4, minsize=5)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(5, weight=1)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(6, minsize=5)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(7, weight=1)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(8, minsize=5)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(9, weight=1)
        self.frame_tab_2.tab("Designs Folders").grid_rowconfigure(10, minsize=5)

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






    def control_tab_2 (self):
        tab_name=["Designs Folders", "Machine Files", "Config Files" ]
        for name in tab_name:
            self.button_tab_2_keep = customtkinter.CTkButton(master=self.frame_tab_2.tab(name), text="Keep", font=FONT_BUTTON,
                                                            width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)
            self.button_tab_2_keep.grid(row=1, column=3, sticky="e")

            self.button_tab_2_delete = customtkinter.CTkButton(master=self.frame_tab_2.tab(name), text="Delete",
                                                             font=FONT_BUTTON,
                                                             width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)
            self.button_tab_2_delete.grid(row=3, column=3, sticky="e")

            self.button_tab_2_add = customtkinter.CTkButton(master=self.frame_tab_2.tab(name), text="ADD",
                                                             font=FONT_BUTTON,
                                                             width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)
            self.button_tab_2_add.grid(row=5, column=3, sticky="e")

            self.button_tab_2_create = customtkinter.CTkButton(master=self.frame_tab_2.tab(name),
                                                               text="Create",
                                                               font=FONT_BUTTON,
                                                               width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)
            self.button_tab_2_create.grid(row=7, column=3, sticky="se")

            self.message_box_tab_2_all = customtkinter.CTkFrame(master=self.frame_tab_2.tab(name), height=150)
            self.message_box_tab_2_all.grid(row=10, column=0, columnspan=4, sticky="ew" )

            self.tree_tab_2 = tkinter.ttk.Treeview(master=self.frame_tab_2.tab(name))

    #         --------- Define Columns ______-------
            self.tree_tab_2["columns"] = ("#", "Name", "Date")
            self.tree_tab_2.column("#0", width=10, minwidth=25)
            self.tree_tab_2.column("#", anchor=W, width=50, minwidth=25)
            self.tree_tab_2.column("Name", anchor=CENTER, width=50, minwidth=25)
            self.tree_tab_2.column("Date", anchor=E, width=50, minwidth=25)
    #      --------------- Create Headings --------------------------
            self.tree_tab_2.heading("#0", text="#0", anchor=W)
            self.tree_tab_2.heading("#", text="#", anchor=W)
            self.tree_tab_2.heading("Name", text="Name", anchor=CENTER)
            self.tree_tab_2.heading("Date", text="Date", anchor=W)
            self.tree_tab_2.grid(row=1, rowspan=7, column=1, columnspan=2, sticky="news")




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
        self.button_machine_save = customtkinter.CTkButton(master=self.frame_3_1.tab("Simple Point Conversion"),text="Save",
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
        self.button_rover_file = customtkinter.CTkButton(master=self.frame_3_1.tab("Simple Point Conversion"), text="Select         ", image=image_add_folder,
                                                         compound= "right", font=FONT_BUTTON,
                                                         fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
                                                         command=lambda:[self.event_button_select(),
                                                                         self.message_file_selected()],
                                                         corner_radius=15, width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT)
        self.button_rover_file.grid(row=2, column=4)



        self.label_select_file = customtkinter.CTkLabel(master=self.frame_3_1.tab("Simple Point Conversion"), text="Select Point File on the Rover",
                                                        font=FONT_LABEL)
        self.label_select_file.grid(row=2, column=1)

        self.button_create = customtkinter.CTkButton(master=self.frame_3_1.tab("Simple Point Conversion"), text="Create File",
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

    def tab_2(self):
        # -------------------------------------Buttons Tab2 -----------------------------------------------------------
        self.button_machine_save_tab2 = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"),
                                                                text="Save",
                                                                command=lambda: [self.event_button_save(),
                                                                                 self.message_saved_name()],
                                                                fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
                                                                width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT,
                                                                corner_radius=15, font=FONT_BUTTON)
        self.button_machine_save_tab2.grid(row=1, column=2, sticky="w")

        self.button_rover_file_tab2 = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"),
                                                              text="Select         ", image=image_add_folder,
                                                              compound="right", font=FONT_BUTTON,
                                                              fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
                                                              command=lambda: [self.event_button_select(),
                                                                               self.message_file_selected()],
                                                              corner_radius=15, width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT)
        self.button_rover_file_tab2.grid(row=1, column=4)

        # self.button_create_tab2 = customtkinter.CTkButton(master=self.frame_3_1.tab("Restore box Conversion"),
        #                                                   text="Create File",
        #                                                   image=image_create_file, compound="right",
        #                                                   corner_radius=15,
        #                                                   fg_color=NOT_SELECTED, text_color=FONT_NOT_SELECTED,
        #                                                   command=lambda: [panda.create_file(),
        #                                                                    self.message_file_created(),
        #                                                                    self.event_button_create()],
        #                                                   width=SECONDARY_WIDTH, height=SECONDARY_HEIGHT, font=FONT_BUTTON)
        # self.button_create_tab2.grid(row=3, column=4)

        # --------------------------------------------------- Entry Tab2--------------------------------------------
        self.entry_machine_name_tab2 = customtkinter.CTkEntry(master=self.frame_3_1.tab("Restore box Conversion"),
                                                              corner_radius=15, width=250, height=ENTRY_HEIGHT)
        self.entry_machine_name_tab2.grid(column=1, row=1, sticky="w")
        self.entry_machine_name_tab2.insert(0, panda.get_machine_name())




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
        select = filedialog.askopenfilename(initialdir=SELECT_FILE_PATH)
        try:
            with open ("TempFile.json", "w") as file:
                upload_file = {"Selected File":select}
                json.dump(upload_file, file, indent =4)


        except:
            print("Except ativated file explorer  ")

        return select




