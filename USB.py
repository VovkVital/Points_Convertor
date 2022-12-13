import win32file
import os
from glob import glob



class usb_drive:
    def __init__(self):
        self.detect_usb()



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
                    # print(f"List{drive_list}")
                    for right_usb in drive_list:
                        directory_check = os.path.join(right_usb, "Machine Control Data", )
                        check_path = glob(f"{directory_check}\\Backup_*")
                        path = ""
                        # needs to be fixed
                        for path in check_path :
                            path = (check_path[0])
                        if os.path.exists(path) == True:
                            self.correct_usb.append(right_usb)
                            print(self.correct_usb)
                            return self.correct_usb





test = usb_drive()