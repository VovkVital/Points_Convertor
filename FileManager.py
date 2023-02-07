import shutil

class FileManager():
    def __init__(self):
        pass
    def move(self, src, dst):
        if not dst.exists():
            folders = ["Designs", "Machine Files", "Config Files"]
            for folder in range(0, len(folders)):
                dst.joinpath(folders[folder]).mkdir(parents=True, exist_ok=True)

        if src.is_dir():
            shutil.move(src, dst.joinpath("Designs"))
            self.click_design()
            self.label_design_files_m2.configure(text=f"Design Files: -- {len(LIST_DESIGN)}")

        if src.is_file():
            files = glob(os.path.join(str(src.parent), "*.cfg"))
            for match in range(0, len(files)):
                if str(src) == files[match]:
                    shutil.move(src, dst.joinpath("Config Files"))
                    self.click_cfg()
                    self.label_config_files_m2.configure(text=f"Config Files: -- {len(LIST_CFG)}")

        if src.is_file():
            files = glob(os.path.join(str(src.parent), "*.MCH"))
            for match in range(0, len(files)):
                if str(src) == files[match]:
                    shutil.move(src, dst.joinpath("Machine Files"))
                    self.click_mch()
                    self.label_machine_files_m2.configure(text=f"Config Files: -- {len(LIST_MCG)}")

