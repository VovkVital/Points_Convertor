import shutil
import pathlib

class File_mangment():
    def __init__(self):
        pass

    def delete_dsn(self, src, dst, usb_path, dst_parent_folder):
        try:
            USB_PATH = usb_path
            if dst.exists():
                shutil.rmtree(dst)
                shutil.move(src=src, dst=dst_parent_folder)
                if field_data :=pathlib.Path(USB_PATH).joinpath(".Field-Data").joinpath(src.name).exists():
                    shutil.rmtree(str(field_data))
            else:
                shutil.move(src, dst=dst_parent_folder)
                if field_data := pathlib.Path(USB_PATH).joinpath(".Field-Data").joinpath(src.name).exists():
                    shutil.rmtree(str(field_data))
        except FileNotFoundError:
            pass


    def delete_file(self, src, dst, dst_parent_folder):
        try:
            if dst.joinpath(dst_parent_folder).joinpath(pathlib.Path(src).name).exists():
                pathlib.Path(dst.joinpath(dst_parent_folder).joinpath(pathlib.Path(src).name)).unlink()
                shutil.move(src, dst.joinpath(dst_parent_folder))
            else:
                shutil.move(src, dst.joinpath(dst_parent_folder))
        except FileNotFoundError:
            pass
