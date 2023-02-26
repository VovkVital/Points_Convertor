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

    def save_btn_event(self, design, usb_path, event_save):
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
                                                                    self.call_back_save_btn_event(path=path,
                                                                    event_save=event_save)])
                else:
                    try:
                        with open("Add_design.json", "r") as file:
                            data = json.load(file)
                        Add_design.DESIGN_PATH = design_path = path
                        data["Design Path"] = str(design_path)

                        with open("Add_design.json", "w") as file:
                            json.dump(data, file, indent=4)
                        event_save()

                    except FileNotFoundError:
                        try:
                            with open("Add_design.json", "w") as file:
                                Add_design.DESIGN_PATH = design_path = path
                                upload_file = {"Design Path": str(design_path), "SVD_Path": "None", "SVL_Path": "None",
                                               "CFG_Path": "None"}
                                json.dump(upload_file, file, indent=4)
                                event_save()
                        except Exception:
                            Error_message(message="Something went wrong ):\n please try it again")
            else:
                Error_message(message="Enter and save design name first", time=2000)
        else:
            Error_message(message="Incorrect name !!!")

    def add_file(self, event_svd):
        file_type = [("Machine Files", (".svd", ".svl", ".cfg")), ("All Files", "*.*")]
        if pathlib.Path(SELECT_FILE_PATH).exists():
            if selected_file := filedialog.askopenfilenames(initialdir=SELECT_FILE_PATH, filetypes=file_type):
                self.file_validation(selected_file=selected_file, event_btn=event_svd)
            else:
                Error_message(message="File was not selected")
        else:
            desktop_path = pathlib.Path("~\\Desktop").expanduser()
            if selected_file := filedialog.askopenfilenames(initialdir=desktop_path, filetypes=file_type):
                self.file_validation(selected_file=selected_file, event_btn=event_svd)
            else:
                Error_message(message="File was not selected")



    def add_cfg(self, usb_path, event_btn):
        file_type = [("Config Files", ".cfg"), ("All Files", "*.*")]
        usb_path = pathlib.Path(usb_path)
        if usb_path.exists():
            if selected_file := filedialog.askopenfilenames(initialdir=usb_path, filetypes=file_type):
                self.file_validation(selected_file=selected_file, event_btn=event_btn)
            else:
                Error_message(message="File was not selected")
        else:
            desktop_path = pathlib.Path("~\\Desktop").expanduser()
            if selected_file := filedialog.askopenfilenames(initialdir=desktop_path, filetypes=file_type):
                self.file_validation(selected_file=selected_file, event_btn=event_btn)
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
            shutil.copy(src=data["SVL_Path"], dst=str(directory))
        if data["CFG_Path"] != "None":
            shutil.copy(src=data["CFG_Path"], dst=str(directory))

        try:
            with open("Add_design.json", "r") as file:
                data = json.load(file)
            data["SVD_Path"] = "None"
            data["SVL_Path"] = "None"
            data["CFG_Path"] = "None"

            with open("Add_design.json", "w") as file:
                json.dump(data, file, indent=4)
        except Exception:
            Error_message(message="Something went wrong ):\n please try it again")



    def file_validation(self, selected_file, event_btn):
        match = r"(?i).+?\.(cfg|svd|svl)"
        svd_count = 0
        svl_count = 0
        cfg_count = 0
        event_btn = event_btn
        try:
            with open("Add_design.json", "r") as file:
                data = json.load(file)
            for file in selected_file:
                if re.fullmatch(pattern=match, string=file):
                    if file.endswith(".svd"):
                        if svd_count == 0:
                            data["SVD_Path"] = Add_design.SVD_PATH = file
                            svd_count += 1
                        else:
                            Error_message("Two or more .svd files\n were selected\n select only one")
                    elif file.endswith(".svl"):
                        if svl_count == 0:
                            data["SVL_Path"] = Add_design.SVL_PATH = file
                            svl_count += 1
                        else:
                            Error_message("Two or more .svl files\n were selected\n select only one")
                    if file.endswith(".cfg"):
                        if cfg_count == 0:
                            data["CFG_Path"] = Add_design.CFG_PATH = file
                            cfg_count += 1
                        else:
                            Error_message("Two or more .cfg files\n were selected\n select only one")
                else:
                    Error_message(message="File was not selected")

            if svd_count > 0 or svl_count > 0 or cfg_count > 0:
                try:
                    with open("Add_design.json", "w") as file:
                        json.dump(data, file, indent=4)
                    if event_btn is not None:
                        event_btn()
                except Exception as e:
                    print(e)
                    # Error_message(message="Something went wrong\n Design name does not exist")
                    # return
        except FileNotFoundError:
            Error_message(message="Something went wrong\n Design name does not exist")
            return


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

    def call_back_save_btn_event(self, path, event_save):
        if pathlib.Path(path).exists():
            timer = threading.Timer(1.0, self.call_back_save_btn_event(path=path, event_save=event_save))
            timer.start()
        else:
            self.save_btn_event(usb_path=self.usb_path, design=self.design_name, event_save=event_save)






