import json
import pandas as pd
import os
from Warnings import Exception_message
import logging


PATH_SITEWORK_DIR = "C:\Trimble Synchronizer Data\PC\Trimble SCS900 Data"
SAVE_FILE_PATH = os.path.expanduser("~/Desktop/Points GCS 900")
S_FOLDER_NAME = "Point Folder GCS 900"



class CSV:
    def __init__(self):
        self.csv_version = "TEXT"
        self.logger = logging.getLogger("App_." + __name__)
    def get_machine_name (self):
        try:
            with open("Settings.json", "r") as file:
                machine_name = json.load(file)
                return machine_name["Machine Name"]
        except BaseException as error:
            Exception_message(message=error)




    def create_file(self, *args):
        try:
            with open ("TempFile.json", "r") as file:
                loaded_file = json.load(file)
            rover = pd.read_csv(loaded_file["Selected File" ])
            cleaned_rover = rover[["Point Name", "Northing", "Easting", "Elevation", "Point Code", "Date", ]].copy()
            cleaned_rover["UTM Zone"] = "None"
            cleaned_rover["Date"] = pd.to_datetime(cleaned_rover['Date'])
            final_rover = cleaned_rover.rename(
                columns={"Point Name": "PointID", "Northing": "Northing(FT)", "Easting": "Easting(FT)",
                         "Elevation": "Elevation(FT)", "Date": "Time-UTC (YYYY/MM/DD HH:MM)"}).copy()
            home_dir = SAVE_FILE_PATH
            if len(args) > 0:
                path = args[0]
                machine_name = self.get_machine_name()
                csv = final_rover.to_csv(fr"{path}\Points_{machine_name}_001.csv", index=False,)
            else:
                if not os.path.isdir(home_dir):
                    os.makedirs(home_dir)
                machine_name = self.get_machine_name()
                csv = final_rover.to_csv(fr"{SAVE_FILE_PATH}\Points_{machine_name}_001.csv", index=False)

        except (KeyError, json.decoder.JSONDecodeError, FileNotFoundError, PermissionError) as error:
            Exception_message(error)
            self.logger.exception(error)
            print(error)

        finally:
            with open("TempFile.json", "w") as file:
                place_holder = {}
                json.dump(place_holder, file)


