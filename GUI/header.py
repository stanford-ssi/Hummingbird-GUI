""" Top header """
import tkinter as tk

class Header:
    frame: tk.Frame

    def __init__(self, parent):
        # Create frame
        self.frame = tk.Frame(parent)

        # Tabs label
        self.title = tk.Label(self.frame, text='Capture', font=('Aria',26))

    def render(self):
        self.title.pack(fill='both', expand=True)
        self.frame.pack(fill='both', expand=True)
