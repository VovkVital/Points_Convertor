import pathlib
import re
import win32file
import os
from glob import glob
from datetime import datetime



class Usb_drive:
    usb_folders_design = []
    usb_file_cfg = []
    usb_file_mch = []
    USB_PATH = ""
    CORRECT_USB = []
    AVAILABLE_USB = set()

    def __init__(self):
        self.detect_usb()
        self.list_designs()
        self.list_cfg()
        self.list_mch()
        self.new = 0
        self.path_switch = 0




    def detect_usb(self):
        drive_list = []
        drivebits=win32file.GetLogicalDrives()
        for d in range(1,26):
            mask=1 << d
            if drivebits & mask:
                # here if the drive is at least there
                drname='%c:\\' % chr(ord('A')+d)
                t=win32file.GetDriveType(drname)
                if t == win32file.DRIVE_REMOVABLE:
                    drive_list.append(drname)
                    self.AVAILABLE_USB.add(drname)
                    for right_usb in drive_list:
                        if pathlib.Path(os.path.join(right_usb, "Machine Control Data")).exists():
                            Usb_drive.USB_PATH = self.directory_check = os.path.join(right_usb, "Machine Control Data")
                            check_path = self.multiple_files(os.listdir(self.directory_check))
                            if check_path != None:
                                self.CORRECT_USB.append(right_usb)
                                Usb_drive.USB_PATH = self.current_path = pathlib.Path(self.directory_check).joinpath(check_path)
                                self.path_switch = 1
                                return self.current_path


    def list_designs(self):
        list_designs = []
        try:
            for design_f in os.listdir(self.current_path):
                folder_path = pathlib.Path(self.current_path).joinpath(design_f)
                if folder_path.is_dir():
                    pattern = r"(?i)\..+|GeoData"
                    match = re.fullmatch(pattern=pattern, string=design_f)
                    if not bool(match):
                        folder_path = pathlib.Path(self.current_path).joinpath(design_f)
                        time = datetime.fromtimestamp(os.path.getmtime(folder_path)).strftime('%m/%d/%Y')
                        list_designs.append([design_f, time])
            return list_designs
        except AttributeError as error:
            # Exception_message(message=error)
            pass
    def list_cfg(self):
        try:
            check_path_cfg = glob(f"{self.current_path}\\*.cfg")
            list_cfg = []
            for cfg in range(0, (len(check_path_cfg))):
                time = datetime.fromtimestamp(os.path.getmtime(check_path_cfg[cfg])).strftime('%m/%d/%Y')
                file = os.path.basename(check_path_cfg[cfg])
                list_cfg.append([file, time])
            return list_cfg
        except AttributeError as error:
            # Exception_message(message=error)
            pass

    def list_mch(self):
        try:
            list_mch = []
            check_path_mch = glob(f"{self.current_path}\\*.MCH")
            for mch in range(0, (len(check_path_mch))):
                time = datetime.fromtimestamp(os.path.getmtime(check_path_mch[mch])).strftime('%m/%d/%Y')
                file = os.path.basename(check_path_mch[mch])
                list_mch.append([file, time])
            return list_mch
        except BaseException as error:
            # Exception_message(message=error)
            pass
    def multiple_files(self, path):
        file_list = self.select_file(path)
        if len(file_list) == 1 or len(file_list) == 0:
            return file_list[0]
        else:
            return None

    def select_file(self, path):
        check = r"(?i)Backup.+|All"
        return [i for i in path if re.fullmatch(check, i)]
    def assign_path(self):
        self.current_path = Usb_drive.USB_PATH


