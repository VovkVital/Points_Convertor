from UI import Interface
from Pandas import CSV
from USB import Usb_drive
import re



def main():
    screen = Interface()
    # Expands to the full screen
    # screen.state("zoomed")
    pd = CSV()
    if re.fullmatch(r".+?Machine Control Data", str(Usb_drive.USB_PATH), flags=re.IGNORECASE):
        screen.multiple_files_usb()
    screen.mainloop()

if __name__ == "__main__":
    main()



















