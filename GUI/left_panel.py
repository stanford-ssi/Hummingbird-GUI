""" Stage + experiment + quick file control """
import tkinter as tk

class LeftPanel:
    frame: tk.Frame

    def __init__(self, parent):
        # Create frame
        self.frame = tk.Label(parent)

        # PT, TT, and LC measurements


    def render(self):
        self.frame.pack(side='left', fill='both')