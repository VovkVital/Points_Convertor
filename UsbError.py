import tkinter
from tkinter import ttk
import customtkinter
from Widgets import Button, Label

# _______ Colors _________
SELECTED_BLUE = "#008fd7"
NOT_SELECTED = "#44657e"
FONT_NOT_SELECTED = "gray60"
FONT_SELECTED = "gray94"
ROW_EVEN = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1]
# ________ Font ___________
FONT_HEADER = ("Roboto", 16, "bold")
FONT_TABLE = ("Roboto", 14, "bold")
FONT_LABEL_ERROR = ("Roboto", 18, "bold")
# _________ Tab Names _______
TAB_NAME = ["Design Folders", "Config Files", "Machine Files"]

TAB_BUTTON_WIDTH = 120
TAB_BUTTON_HEIGHT = 40

MESSAGE = "Two or more files are present on the USB. Select one!"



class Message_box(tkinter.ttk.Treeview):

    def __init__(self, data, ui_command, **kwargs):
        self.frame()
        self.flash = Button.flash
        super(). __init__(master=self.tree_frame)
        self.data = data
        self.Treestyle()
        self.one_frame()
        self.buttons(ui_command=ui_command)
        self.return_value = 0



    def frame(self):
        self.box = customtkinter.CTkToplevel()
        width = self.box.winfo_screenwidth()
        height = self.box.winfo_screenheight()
        self.box.geometry("+%d+%d" % ((width / 2) - 200, (height / 2) - 100))
        self.box.minsize(width=550, height=250)
        self.box.maxsize(width=550, height=250)
        self.box.title("Data Error")
        self.box.rowconfigure(0, weight=1, minsize=60)
        self.box.rowconfigure(1, weight=2)
        self.box.rowconfigure(2, minsize=10)
        self.box.rowconfigure(3, weight=1, minsize=80)
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
                                 borderwidth=0, font=FONT_TABLE, rowheight=38)
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
        self.column("Date", anchor="w", width=40, minwidth=38)
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

    def buttons(self, ui_command):

        self.button_select = Button(master=self.box, text="Select", sticky=None, row=3, column=0,
                                    command=lambda: [ui_command()])
        self.button_select.configure(width=TAB_BUTTON_WIDTH, height=TAB_BUTTON_HEIGHT)

        self.button_close = Button(master=self.box, text="Close", sticky=None, row=3, column=1, command=self.close_frame)
        label = Label(master=self.box, text="Select folder to manage !", row=0, column=0)
        label.grid(columnspan=2)
        label.configure(text_color=SELECTED_BLUE, font=FONT_LABEL_ERROR)


    def file_selection(self):
        try:
            selected_item = self.item(self.focus())["values"][0]
            self.after(800, lambda: self.box.destroy())
            return selected_item
        except IndexError:
            pass
    def close_frame(self):
        self.after(800, lambda: self.box.destroy())














