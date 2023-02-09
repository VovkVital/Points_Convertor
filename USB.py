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

    def __init__(self):
        self.detect_usb()
        self.list_designs()
        self.list_cfg()
        self.list_mch()
        self.new = 0
        self.path_switch = 0


    def detect_usb(self):
        self.correct_usb = []
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
                    for right_usb in drive_list:
                        if pathlib.Path(os.path.join(right_usb, "Machine Control Data")).exists():
                            Usb_drive.USB_PATH = self.directory_check = os.path.join(right_usb, "Machine Control Data")
                            check_path = self.multiple_files(os.listdir(self.directory_check))
                            if check_path != None:
                                self.correct_usb.append(right_usb)
                                Usb_drive.USB_PATH = self.current_path = pathlib.Path(self.directory_check).joinpath(check_path)
                                self.path_switch = 1
                                return self.current_path


    def list_designs(self):
        list_designs = []
        try:
            for design_f in os.listdir(self.current_path):
                check_path_svd = glob(f"{self.current_path}\\{design_f}\\*.svd")
                check_path_svl = glob(f"{self.current_path}\\{design_f}\\*.svl")
                if check_path_svd or check_path_svl:
                    path_svd = check_path_svd[0]
                    # path_svl = check_path_svl[0]
                    time = datetime.fromtimestamp(os.path.getmtime(path_svd)).strftime('%m/%d/%Y')
                    list_designs.append([design_f, time])
            return list_designs
        except AttributeError:
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
        except AttributeError:
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
        except:
            pass
    def multiple_files(self, path):
        file_list = self.select_file(path)
        if len(file_list) == 1 or len(file_list) == 0:
            return file_list[0]
        else:
            return None

    def select_file(self, path):
        check = r"Backup.+|[aA][lL][lL]"
        return [i for i in path if re.fullmatch(check, i)]





        # try:
        #     for design_f in os.listdir(self.current_path):
        #         check_path_svd = glob(f"{self.current_path}\\{design_f}\\*.svd")
        #         check_path_svl = glob(f"{self.current_path}\\{design_f}\\*.svl")
        #         if check_path_svd or check_path_svl:
        #             path_svd = check_path_svd[0]
        #             # path_svl = check_path_svl[0]
        #             time = datetime.fromtimestamp(os.path.getmtime(path_svd)).strftime('%m/%d/%Y')
        #             list_designs.append([design_f, time])
        #     return list_designs
        # except AttributeError:
        #     pass
        #


