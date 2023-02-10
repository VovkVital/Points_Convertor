from tkinter import *
from tkinter import filedialog
import pandas as pd
import os
import customtkinter
SELECT_FILE_PATH = "C:\Trimble Synchronizer Data\PC\Trimble SCS900 Data"
SAVE_FILE_PATH = r"C:\Users\vovkv\Desktop\Point File GCS"
S_FOLDER_NAME = "Point File GCS 900"
FONT = ("Futura", 10, "bold")
MACHINE_NAME = ""
# --------------------------------------------Functions-----------------------------------------------------------------
def explorer ():
    select = filedialog.askopenfilename(initialdir= SELECT_FILE_PATH)
    return select


def create_file ():
    rover = pd.read_csv("iron.csv")
    rover.head(5)
    cleaned_rover = rover[["Point Name", "Northing", "Easting", "Elevation", "Point Code", "Date", ]].copy()

    cleaned_rover["UTM Zone"] = "None"
    final_rover = cleaned_rover.rename(
        columns={"Point Name": "PointID", "Northing": "Northing(FT)", "Easting": "Easting(FT)",
                 "Elevation": "Elevation(FT)", "Date": "Time-UTC (YYYY/MM/DD HH:MM:SS)"}).copy()
    home_dir = SELECT_FILE_PATH
    if not os.path.isdir(home_dir):
        os.makedirs(home_dir)
        final_rover.to_csv(f"{home_dir}\Points")
        print("Home directory %s was created." % home_dir)


# ------------------------------------------Screen-----------------------------------------------------------------

screen = Tk()
screen.title("GCS 900 Point Convertor")
screen.title(" Fly to US ")
screen.config(padx=00, pady=50, )
canvas = Canvas(width=600, height=800, highlightthickness=0, )
canvas.grid(row=1, column=0, columnspan=2)


#-------------------------------------------Entry------------------------------------------------------------------

machine_name = Entry(width=40, highlightthickness=0, font=FONT)
machine_name.grid(column=0, row=0)



#-------------------------------------------Buttons----------------------------------------------------------------
machine_select_button = Button(text="Select", highlightthickness=0, font=FONT,
                                  bg="white", width=20, padx=1, pady=2, )
machine_select_button.grid(row=0, column=1)

rover_button = Button(text="Point File from Rover", highlightthickness=0, font=FONT,
                                  bg="white", width=20, padx=1, pady=2, command=explorer)
rover_button.grid(column=0,row=1)

process_button = Button(text="Create Point File", highlightthickness=0, font=("Futura", 10, "bold"),
                                  bg="white", width=20, padx=1, pady=2, command=create_file)
process_button.grid(column=0,row=2)











screen.mainloop()
