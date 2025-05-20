""" Main section of UI """
import tkinter as tk
from left_panel import LeftPanel
from right_panel import RightPanel

class Body:
    frame: tk.Frame

    def __init__(self, parent):
        # Create frame
        self.frame = tk.Frame(parent)

        # Left panel 
        self.left_panel = LeftPanel(self.frame, self.store)

        # Right panel 
        self.right_panel = RightPanel(self.frame, self.store)

    def render(self):
        self.left_panel.render()
        self.right_panel.render()
        self.frame.pack(fill='both', expand=True)
