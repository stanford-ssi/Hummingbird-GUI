""" Stage + experiment + quick file control """
import tkinter as tk
from measure_widget import MeasureWidget

class LeftPanel:
    frame: tk.Frame

    def __init__(self, parent):
        # Create frame
        self.frame = tk.Label(parent, background='blue')

        # top frame
        self.topframe = tk.Frame(self.frame)
        self.title = tk.Label(self.topframe, text = 'Measurements', font=('Comic Sans MS', 26))

        # PT, TT, and LC measurements
        self.pt1 = MeasureWidget(self.frame, 'PT1', '[Pa]')

    def render(self):
        self.title.pack(fill = 'x')
        self.topframe.pack(fill = 'x')
        self.pt1.render()
        self.frame.pack(side='left', fill='both', expand=True)

