# example_interface.py
"""Interface Demo"""
import tkinter as tk

class InterfaceApp:
    """Define an interface defaults"""
    def __init__(self, parent):
        self.parent = parent
        self.used_rows = set()
        self.used_columns = set()
        self.setup_window()
        self.create_widgets()
        self.configure_used_grid()

    def setup_window(self):
        """Setup a new window"""
        # Main Window Variables
        interface_geometry = "400x400"
        interface_title = "Processor Interface"
        interface_geometry_max = {'width': 600, 'height': 600}
        interface_geometry_min = {'width': 300, 'height': 300}

        self.parent.title(interface_title)
        self.parent.geometry(interface_geometry)
        self.parent.wm_minsize(**interface_geometry_min)
        self.parent.wm_maxsize(**interface_geometry_max)

    def create_widgets(self):
        """Add Widgets to frame"""
        # Define the initial LabelFrames and apply the grid settings
        self.add_labelframe("frame1", row=0, column=0)
        self.add_labelframe("frame2", row=1, column=0)

    def add_labelframe(self, text, row, column):
        """Define custom labelframe"""
        labelframe = tk.LabelFrame(self.parent, text=text, width=10, height=10)
        self.configure_labelframe_grid(labelframe, row, column)

    def configure_labelframe_grid(self, labelframe, row, column):
        """Define custom labelframe"""
        labelframe.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
        self.used_rows.add(row)
        self.used_columns.add(column)
        self.configure_used_grid()

    def configure_used_grid(self):
        """configure grid of all used rows and columns"""
        # Configure the grid behavior for only the used rows and columns
        for row in self.used_rows:
            self.parent.grid_rowconfigure(row, weight=1, minsize=10)
        for column in self.used_columns:
            self.parent.grid_columnconfigure(column, weight=1, minsize=10)

    def get_used_rows_and_columns(self):
        """get all used rows and columns"""
        return self.used_rows, self.used_columns

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    root.mainloop()

# End-of-file (EOF)
