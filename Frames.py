
class Frames():
    def __init__(self, master, value):
        self.window = master
        self._colum_count = 0
        self._row_count = 0
        self.columns = value["columns"]
        self.rows = value["rows"]

    @property
    def columns(self):
        return f"{self}"

    @columns.setter
    def columns(self, value):
        for data in value:
            self.window.columnconfigure(data[0], weight=data[1], minsize=data[2])
            self._colum_count += 1

    @property
    def rows(self):
        return f"{self}"

    @rows.setter
    def rows(self, value):
        for data in value:
            self.window.rowconfigure(data[0], weight=data[1], minsize=data[2])
            self._row_count += 1

    def __str__(self):
        return f"Number of columns: {self._colum_count}\nNumber of rows: {self._row_count}"
