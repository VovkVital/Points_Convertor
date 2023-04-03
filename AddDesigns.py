import pathlib
from Warnings import Error_message, Exception_message, Design_exists
import json
import threading
from tkinter import filedialog
import re
import shutil
import logging


PATH_SITEWORK_DIR = r"C:\Trimble Synchronizer Data\PC\Trimble SCS900 Data"



class Add_design():
    SVD_PATH = "None"
    SVL_PATH = "None"
    CFG_PATH = "None"
    DESIGN_PATH = "None"
    def __init__(self):
        self.design_name = ""
        self.usb_path = ""
        super().__init__()
        self.logger = logging.getLogger("App_."+__name__)

    def save_btn_event(self, design, usb_path, event_save):
        pattern = r"((?i)[a-z0-9 \._-]*$)"
        self.logger.debug(f"Values: Design name {design} || {usb_path}")
        if re.fullmatch(pattern=pattern, string=str(design)):
            design_name = str(design).strip()
            USB_PATH = usb_path
            if USB_PATH != "":
                pass
                if design_name != "" and design_name[0] != " " and design_name[0] != "." and design_name[0] != "_" \
                        and design_name[0] != "-":
                    path = pathlib.Path(USB_PATH).joinpath(str(design_name))
                    self.design_name = design_name
                    self.usb_path = str(usb_path)
                    if path.exists() and path.is_dir():
                        message = f"The design name : {design_name}\n\nis already exist on the USB\n\n " \
                                  "Do you want to remove it first ?"
                        Design_exists(message=message, command=lambda: [self.remove_file(usb_path=path),
                                                                        self.call_back_save_btn_event(path=path,
                                                                        event_save=event_save)])

                    else:
                        try:
                            with open("Add_design.json", "r") as file:
                                data = json.load(file)
                            Add_design.DESIGN_PATH = design_path = path
                            data["Design Path"] = str(design_path)
                            data["SVD_Path"] = "None"
                            data["SVL_Path"] = "None"
                            data["CFG_Path"] = "None"

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
                                Error_message(message="Something went wrong ):\nplease try it again")
                                return
                else:
                    Error_message(message="Save design name first", time=2000)
                    return

            else:
                Error_message(message="USB not connected")
                return

        else:
            Error_message(message="Invalid name !!!\n\n(No symbols like %!^& etc.)")
            return

    def add_file(self, event_svd):
        file_type = [("Machine Files", (".svd", ".svl", ".cfg")), ("All Files", "*.*")]
        if pathlib.Path(PATH_SITEWORK_DIR).exists():
            if selected_file := filedialog.askopenfilenames(initialdir=PATH_SITEWORK_DIR, filetypes=file_type):
                self.file_validation(selected_file=selected_file, event_btn=event_svd)
            else:
                Error_message(message="Files not selected")
        else:
            desktop_path = pathlib.Path("~\\Desktop").expanduser()
            if selected_file := filedialog.askopenfilenames(initialdir=desktop_path, filetypes=file_type):
                self.file_validation(selected_file=selected_file, event_btn=event_svd)
            else:
                Error_message(message="Files not selected")



    def add_cfg(self, usb_path, event_btn):
        file_type = [("Config Files", ".cfg"), ("All Files", "*.*")]
        usb_path = pathlib.Path(usb_path)
        if usb_path.exists():
            if selected_file := filedialog.askopenfilenames(initialdir=usb_path, filetypes=file_type):
                self.file_validation(selected_file=selected_file, event_btn=event_btn)
            else:
                Error_message(message="File not selected")
        else:
            desktop_path = pathlib.Path("~\\Desktop").expanduser()
            if selected_file := filedialog.askopenfilenames(initialdir=desktop_path, filetypes=file_type):
                self.file_validation(selected_file=selected_file, event_btn=event_btn)
            else:
                Error_message(message="File not selected")

    def create_design(self):
        task = threading.Thread(target=self.move_files)
        task.daemon = True
        task.start()



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
                            Error_message("Two or more .svd files selected\n\nselect one .svd and one .svl")
                            data["SVD_Path"] = "None"
                            data["SVL_Path"] = "None"
                            svd_count = 0
                            svl_count = 0
                            cfg_count = 0
                            break
                    elif file.endswith(".svl"):
                        if svl_count == 0:
                            data["SVL_Path"] = Add_design.SVL_PATH = file
                            svl_count += 1
                        else:
                            Error_message("Two or more .svl files selected\n\nselect one .svd and one .svl")
                            data["SVD_Path"] = "None"
                            data["SVL_Path"] = "None"
                            svd_count = 0
                            svl_count = 0
                            cfg_count = 0
                            break
                    if file.endswith(".cfg"):
                        if cfg_count == 0:
                            data["CFG_Path"] = Add_design.CFG_PATH = file
                            cfg_count += 1
                        else:
                            Error_message("Two or more .cfg files selected\n\nselect one .cfg file")
                            data["CFG_Path"] = "None"
                            cfg_count = 0
                            break
                else:
                    Error_message(message="No files were selected")

            if svd_count > 0 or svl_count > 0 or cfg_count > 0:
                try:
                    with open("Add_design.json", "w") as file:
                        json.dump(data, file, indent=4)
                    if event_btn is not None:
                        event_btn()
                except Exception:
                    Error_message(message="Something went wrong\nDesign name does not exist")
                    return
        except FileNotFoundError:
            Error_message(message="Something went wrong\nDesign name does not exist")
            return


    def remove_file (self, usb_path):
        src = usb_path = usb_path
        dst = pathlib.WindowsPath("~\\Desktop\\USB Deleted Files").expanduser()
        if not dst.exists():
            folders = ["Designs", "Machine Files", "Config Files"]
            for folder in range(0, len(folders)):
                dst.joinpath(folders[folder]).mkdir(parents=True, exist_ok=True)
        dst_folder = pathlib.WindowsPath("~\\Desktop\\USB Deleted Files\\Designs").joinpath(usb_path.name).expanduser()
        if src.is_dir():
            if dst_folder.exists():
                shutil.rmtree(dst_folder)
                shutil.move(src=src, dst=dst_folder)
            else:
                shutil.move(src=src, dst=dst_folder)
        else:
            Error_message(message="Change design name\n and try it again")

    def call_back_save_btn_event(self, path, event_save):
        if pathlib.Path(path).exists():
            timer = threading.Timer(1.0, self.call_back_save_btn_event(path=path, event_save=event_save))
            timer.start()
        else:
            self.save_btn_event(usb_path=self.usb_path, design=self.design_name, event_save=event_save)


    def move_files(self):
        with open("Add_design.json", "r") as file:
            data = json.load(file)
        directory = pathlib.Path(data["Design Path"])
        try:
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

                Error_message(message="Design is created", time=3000)
            except Exception:
                Error_message(message="Something went wrong ):\nplease try it again")
                return
        except FileNotFoundError:
            pass





