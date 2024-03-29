from UI import Interface
from Pandas import CSV
from USB import Usb_drive
import re
import win32event
import win32api
import sys
from winerror import ERROR_ALREADY_EXISTS
from Logging import MyLogger
import tkinter as tk

#  Terminates all the task after the main windows is closed
def on_window_close():
    # Close all tasks here
    sys.exit()


def main():
    try:
        logger = MyLogger("App_")
        logger.app_start("App_initialization")
        # checks if application is already open
        mutex = 'File Manager.exe'
        mutex_check = win32event.CreateMutex(None, False, 'File Manager.exe')
        if win32api.GetLastError() == ERROR_ALREADY_EXISTS:
            mutex = None
            sys.exit(0)
        else:
            screen = Interface()
            # Expands to the full screen
            screen.state("zoomed")
            pd = CSV()
            if re.fullmatch(r".+?Machine Control Data", str(Usb_drive.USB_PATH), flags=re.IGNORECASE):
                screen.multiple_files_usb()
            # Register a callback function to be called when the window is closed
            screen.protocol("WM_DELETE_WINDOW", on_window_close)
            screen.mainloop()

    except BaseException as err:
        if bool(logger):
            logger.app_crash("App_Crashed")
            logger.exception(f"The App Crashed because of {err}")
            sys.exit(1)
        else:
            logger = MyLogger("App_")
            logger.app_crash("App_Crashed")
            logger.exception(f"The App Crashed because of {err}")
            sys.exit(2)


if __name__ == "__main__":
    main()

















