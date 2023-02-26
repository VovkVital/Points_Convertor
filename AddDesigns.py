import pathlib
from Warnings import Error_message, Exception_message, Design_exists
import json
import threading
from tkinter import filedialog
import re
import shutil
from glob import glob
import os.path

SELECT_FILE_PATH = r"C:\Trimble Synchronizer Data\PC\Trimble SCS900 Data"



class Add_design():
    SVD_PATH = "None"
    SVL_PATH = "None"
    CFG_PATH = "None"
    DESIGN_PATH = "None"
    def __init__(self):
        self.design_name = ""
        self.usb_path = ""
        super().__init__()

    def save_btn_event(self, design, usb_path):
        pattern = r"((?i)[a-z0-9 _-]*$)"
        if re.fullmatch(pattern=pattern, string=str(design)):
            design_name = design
            USB_PATH = usb_path
            if design_name != "":
                path = pathlib.Path(USB_PATH).joinpath(design_name)
                self.design_name = design_name
                self.usb_path = str(usb_path)
                if path.exists() and path.is_dir():
                    message = "The design name is already exist\n\n on the connected USB\n\n " \
                              "Do you want to remove it, first ?"
                    Design_exists(message=message, command=lambda: [self.remove_file(usb_path=path),
                                                                    self.call_back_save_btn_event(path=path)])
                else:
                    try:
                        with open("Add_design.json", "w") as file:
                            Add_design.DESIGN_PATH = design_path = path
                            upload_file = {"Design Path": str(design_path), "SVD_Path": "None", "SVL_Path": "None",
                                           "CFG_Path": "None"}
                            json.dump(upload_file, file, indent=4)
                    except Exception as e:
                        Exception_message(message=e)
            else:
                Error_message(message="Enter and save design name first", time=2000)
        else:
            Error_message(message="Incorrect name !!!")

    def add_file(self):
        file_type = [("Machine Files", (".svd", ".svl", ".cfg")), ("All Files", "*.*")]
        if pathlib.Path(r"C:\Trimble Synchronizer Data\PC\Trimble SCS900 Data").exists():
            if selected_file := filedialog.askopenfilenames(initialdir=SELECT_FILE_PATH, filetypes=file_type):
                self.file_validation(selected_file=selected_file)
            else:
                Error_message(message="File was not selected")
        else:
            desktop_path = pathlib.Path("~\\Desktop").expanduser()
            if selected_file := filedialog.askopenfilenames(initialdir=desktop_path, filetypes=file_type):
                self.file_validation(selected_file=selected_file)
            else:
                Error_message(message="File was not selected")




    def create_design(self):
        with open("Add_design.json", "r") as file:
            data = json.load(file)
        directory = pathlib.Path(data["Design Path"])
        directory.mkdir()
        if data["SVD_Path"] != "None":
            shutil.copy(src=data["SVD_Path"], dst=str(directory))
        if data["SVL_Path"] != "None":
            print("svl")
            shutil.copy(src=data["SVL_Path"], dst=str(directory))
            print("copied")
        if data["CFG_Path"] != "None":
            print(data["CFG_Path"])
            shutil.copy(src=data["CFG_Path"], dst=str(directory))






    def file_validation(self, selected_file):
        match = r"(?i).+?\.(cfg|svd|svl)"
        svd_count = 0
        svl_count = 0
        cfg_count = 0
        for file in selected_file:
            if re.fullmatch(pattern=match, string=file):
                if file.endswith(".svd"):
                    if svd_count == 0:
                        Add_design.SVD_PATH = file
                        svd_count += 1
                    else:
                        Error_message("Two or more .svd files\n were selected\n select only one")
                elif file.endswith(".svl"):
                    if svl_count == 0:
                        Add_design.SVL_PATH = file
                    else:
                        Error_message("Two or more .svl files\n were selected\n select only one")
                elif file.endswith(".cfg"):
                    if cfg_count == 0:
                        Add_design.CFG_PATH = file
                        cfg_count += 1
                    else:
                        Error_message("Two or more .cfg files\n were selected\n select only one")
        if svd_count > 0 or svl_count > 0 or cfg_count > 0:
            try:
                with open("Add_design.json", "r") as file:
                    data = json.load(file)
                data["SVD_Path"] = Add_design.SVD_PATH
                data["SVL_Path"] = Add_design.SVL_PATH
                data["CFG_Path"] = Add_design.CFG_PATH

                with open("Add_design.json", "w") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                Error_message(message="Something went wrong\n"
                                      "Design name does not exist")
                return
        else:
            Error_message(message="File was not selected")

    def remove_file (self, usb_path):
        usb_path = usb_path
        src = pathlib.Path(usb_path)
        dst = pathlib.WindowsPath("~\\Desktop\\PC Deleted Files").expanduser()
        if src.is_dir():
            dst = dst.joinpath("Designs")
            if dst.exists():
                shutil.rmtree(str(dst))
                shutil.move(src=src, dst=dst)
            else:
                shutil.move(src=src, dst=dst)
        else:
            Error_message(message="Change design name\n and try it again")

    def call_back_save_btn_event(self, path):
        # print(bool(pathlib.Path(path).exists()))
        if pathlib.Path(path).exists():
            timer = threading.Timer(1.0, self.call_back_save_btn_event)
            timer.start()
        else:
            self.save_btn_event(usb_path=self.usb_path, design=self.design_name)






