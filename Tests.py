import re

string = "Backup_MHG 6022_20221117_152506"

string_2 = "D:\Machine Control Data\Backup_MHG 6022_20221117_152506"

s = r"(?i)Backup_(.+?)_.+"
s_2 = r"(?i).+MachIne Control Data.+Backup_MHG.+"

# find =re.fullmatch(string=string_2, pattern=s_2)
# print(bool(find))


def catch_mname(path):
    main_check = r"(?i).+MachIne Control Data.+Backup_MHG.+"
    name_check = s = r"(?i)Backup_(.+?)_.+"
    if re.fullmatch(string=path, pattern=main_check):
        machine_name = re.findall(string=path, pattern=name_check)[0]
        print(type(machine_name))

catch_mname(path=string_2)