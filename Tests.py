from Warnings import Exception_message
from UsbError import Message_box

import tkinter

screen = tkinter.Tk()
error = Exception_message(message="Select Design", time=2)


screen.mainloop()