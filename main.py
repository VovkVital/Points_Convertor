from UI import Interface
from Pandas import CSV
import asyncio
from USB import Usb_drive
import re

async def main():
    screen = Interface()
    pd = CSV()
    print(Usb_drive.USB_PATH)
    if re.fullmatch(r".+?MachIne Control Data", str(Usb_drive.USB_PATH), flags=re.IGNORECASE):
        await screen.multiple_files_usb()
    screen.mainloop()

if __name__ == "__main__":
    asyncio.run(main())



# box = Message_box(data=[["A",1], ["B",2]])















