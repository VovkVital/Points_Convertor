import re

folder_1 = "Work q"
folder_2 = ".Work-related"


pattern = r"(?i)\..+"

print(bool(re.fullmatch(pattern=pattern, string=folder_2)))