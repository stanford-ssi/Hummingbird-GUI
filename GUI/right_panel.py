# live microscope feed & data vis
import tkinter as tk

class RightPanel:
    frame: tk.Frame

    def __init__(self, parent):
        # Create frame
        self.frame = tk.Label(parent, background='red')

        # PV and SV controls

        # E-stop button

    def render(self):
        self.frame.pack(side='left', fill='both', expand=True)