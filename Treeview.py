import tkinter
from tkinter import ttk
import customtkinter
from Buttons import Button, Label
# _______ Colors _________
SELECTED_BLUE = "#008fd7"
NOT_SELECTED = "#44657e"
FONT_NOT_SELECTED = "gray60"
FONT_SELECTED = "gray94"
ROW_EVEN = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1]
# ________ Font ___________
FONT_HEADER = ("Robot", 18, "bold")
FONT_TABLE = ("Roboto", 16)
FONT_LABEL_ERROR = ("Roboto", 18, "bold")
# _________ Tab Names _______
TAB_NAME=["Design Folders", "Config Files", "Machine Files"]



class Treeview(tkinter.ttk.Treeview):
    def __init__(self, master, data, **kwargs):
        self.frame()
        self.flash=Button.flash
        super(). __init__(master=self.tree_frame)
        self.data = data
        self.master=master
        self.Treestyle()
        self.one_frame()


        if kwargs["message_box"] == True:
            self.buttons()
        # if kwargs["multiframe"] == True:
        #     if kwargs["frames"][0] == "Design Folders":
        #         self.multiframe(data[0])
        #     if kwargs["frames"][1] == "Config Files":
        #         self.multiframe(data[1])
        #     if kwargs["frames"][2] == "Machine Files":
        #         self.multiframe(data[2])
        # else:
        #     self.one_frame()
    def frame(self):
        self.box = customtkinter.CTkToplevel()
        self.box.geometry("500x250")
        self.box.minsize(width=500, height=250)
        self.box.title("Data Error")
        self.box.rowconfigure(0, weight=1, minsize=60)
        self.box.rowconfigure(1, weight=2)
        self.box.rowconfigure(2, minsize=10)
        self.box.rowconfigure(3, weight=1, minsize=40)
        self.box.rowconfigure(4, minsize=15)
        self.box.columnconfigure(0, weight=1)
        self.box.columnconfigure(1, weight=1)
        self.tree_frame = customtkinter.CTkFrame(master=self.box)
        self.tree_frame.grid(row=1, column=0, columnspan=2, sticky="news")
        self.tree_frame.rowconfigure(0, weight=1)
        self.tree_frame.columnconfigure(0, weight=1)





    def Treestyle(self):
        self.treestyle = ttk.Style()
        self.treestyle.theme_use('default')
        self.treestyle.configure("Treeview", background=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1],
                                 foreground=customtkinter.ThemeManager.theme["CTkLabel"]["text_color"][1],
                                 fieldbackground=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1],
                                 borderwidth=0, font=FONT_TABLE, rowheight=50)
        self.treestyle.configure("Treeview.Heading", font=FONT_HEADER,
                                 background=(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1]),
                                 foreground=FONT_NOT_SELECTED, borderwidth=0,
                                 selected=SELECTED_BLUE)
        self.treestyle.map("Treeview.Heading",
                      background=[('active', customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1])])
        self.treestyle.map('Treeview',
                      background=[("selected", SELECTED_BLUE)],
                      foreground=[('selected', FONT_SELECTED)])

    def one_frame (self, **kwargs):
        count = 0
        row_count = 1

        self.tree_scroll = customtkinter.CTkScrollbar(master=self.tree_frame, command=self.yview)
        self.tree_scroll.grid(row=0, column=0, sticky="ens")
        self.tag_configure("odd", background="#212121")
        self.tag_configure("even", background=ROW_EVEN)
        #         --------- Define Columns ______-------
        self["columns"] = ("Name", "Date")
        self.column("#0", anchor="w", width=55, minwidth=55, stretch=False)
        self.column("Name", anchor="w", width=350, minwidth=100)
        self.column("Date", anchor="w", width=40, minwidth=40)
        #      -    -------------- Create Headings --------------------------
        self.heading("#0", text="", anchor="w")
        self.heading("Name", text="Name", anchor="w")
        self.heading("Date", text="Date", anchor="w")
        self.grid(row=0, column=0, columnspan=2, sticky="news", )
        self.configure(yscrollcommand=self.tree_scroll.set)
        self.config(**kwargs)

        # ----------------insert in Treeveiw --------------------------------

        try:
            for record in self.data:
                if count % 2 == 0:
                    self.insert(parent="", index="end", text=row_count, iid=count,
                                values=(record[0], record[1]), tags=("odd",))
                else:
                    self.insert(parent="", index="end", text=row_count, iid=count,
                                values=(record[0], record[1]), tags=("even",))
                count += 1
                row_count += 1
        except TypeError:
                pass

    def buttons(self):

        Button(master=self.box, text="Select", sticky=None, row=3, column=0, command=None)
        Button(master=self.box, text="Cancel", sticky=None, row=3, column=1, command=None)
        label = Label(master=self.box, text="Two or more files are present on the USB. Select one!", row=0, column=0)
        label.grid(columnspan=2)
        label.configure(text_color=SELECTED_BLUE, font=FONT_LABEL_ERROR)


    def oppa(self):
        print("Oppa")
        # label = customtkinter.CTkLabel(master=self.box, text="Two or more files on USB. Select one")
        # label.grid(row=0, column=0, columnspan=2)

    # def multiframe(self, data, **kwargs):
    #     if kwargs["frames"]:
    #         for frame in range(0, kwargs["frames"]) :
    #                 count = 0
    #                 row_count = 1
    #                 self.tree_scroll = customtkinter.CTkScrollbar(master=kwargs["frames"][frame], command=self.yview)
    #                 self.tree_scroll.grid(row=0, column=1, sticky="ns")
    #                 self.tag_configure("odd", background="#212121")
    #                 self.tag_configure("even", background=ROW_EVEN)
    #                 #         --------- Define Columns ______-------
    #                 self["columns"] = ("Name", "Date")
    #                 self.column("#0", anchor="w", width=55, minwidth=55, stretch=False)
    #                 self.column("Name", anchor="w", width=350, minwidth=100)
    #                 self.column("Date", anchor="w", width=40, minwidth=40)
    #                 #      -    -------------- Create Headings --------------------------
    #                 self.heading("#0", text="", anchor="w")
    #                 self.heading("Name", text="Name", anchor="w")
    #                 self.heading("Date", text="Date", anchor="w")
    #                 self.grid(row=0, column=0, columnspan=4, sticky="news", )
    #                 self.configure(yscrollcommand=self.tree_scroll.set)
    #                 self.config(**kwargs)
    #
    #                 # ----------------insert in Treeveiw --------------------------------
    #
    #                 try:
    #                     for record in data:
    #                         if count % 2 == 0:
    #                             self.insert(parent="", index="end", text=row_count, iid=count,
    #                                                    values=(record[0], record[1]), tags=("odd",))
    #                         else:
    #                             self.insert(parent="", index="end", text=row_count, iid=count,
    #                                                    values=(record[0], record[1]), tags=("even",))
    #                         count += 1
    #                         row_count += 1
    #                 except TypeError:
    #                     LIST_DESIGN = []













