from tkinter import ttk
import customtkinter


SELECTED_BLUE = "#008fd7"
NOT_SELECTED = "#44657e"
FONT_NOT_SELECTED = "gray60"
FONT_SELECTED = "gray94"
ROW_EVEN = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1]
# ________ Font ___________
FONT_HEADER = ("Roboto", 17, "bold")
FONT_TABLE = ("Roboto", 15, "bold")
FONT_LABEL_ERROR = ("Roboto", 18, "bold")
FONT = ("Roboto", 15, "bold")
# _________ Tab Names _______
TAB_NAME = ["Design Folders", "Config Files", "Machine Files"]

class MainTree(ttk.Treeview):
    def __init__(self, master, data, **kwargs):
        super().__init__(master=master, **kwargs)
        self.trstyle()
        self.tree(data=data, master=master, **kwargs)
        self.config(**kwargs)

    def trstyle(self):
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

    def tree(self, data, master, **kwargs):
        #             ------------------------------------------Scroll Bar ________________________________
        self.tree_scroll = customtkinter.CTkScrollbar(master=master, command=self.yview)
        self.tree_scroll.grid(row=0, column=1, sticky="ens")
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
        self.grid(row=0,  column=0, columnspan=4, sticky="news" )
        self.configure(yscrollcommand=self.tree_scroll.set)
        self.config(**kwargs)
        count = 0
        row_count = 1
        try:
            for record in data:
                if count % 2 == 0:
                    self.insert(parent="", index="end", text=row_count, iid=count,
                                           values=(record[0], record[1]), tags=("odd",))
                else:
                    self.insert(parent="", index="end", text=row_count, iid=count,
                                           values=(record[0], record[1]), tags=("even",))
                count += 1
                row_count += 1
        except TypeError:
            LIST_DESIGN = []




