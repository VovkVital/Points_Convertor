import re

string = "Backup_MHG 6022_20221117_152506"

string_2 = "D:\Machine Control Data\Backup_MHG 6022_20221117_152506"

s = r"(?i)Backup_(.+?)_.+"
s_2 = r"(?i).+Backup_MHG.+"

find =re.fullmatch(string=string_2, pattern=s_2)
print(bool(find))