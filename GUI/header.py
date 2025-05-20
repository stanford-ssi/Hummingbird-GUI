""" Top header """
import tkinter as tk

class Header:
    frame: tk.Frame

    def __init__(self, parent):
        # Create frame
        self.frame = tk.Frame(parent)

        # Tabs label
        self.title = tk.Label(self.frame, text='Fountain Hopper - Hummingbird GUI', font=('Comic Sans',32))

    def render(self):
        self.title.pack(fill='both', expand=True)
        self.frame.pack(fill='both', expand=True)
