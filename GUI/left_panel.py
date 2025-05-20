""" Stage + experiment + quick file control """
import tkinter as tk
from measure_widget import MeasureWidget

class LeftPanel:
    frame: tk.Frame

    def __init__(self, parent):
        # Create frame
        self.frame = tk.Label(parent, borderwidth=5, relief='solid')

        # top frame
        self.topframe = tk.Frame(self.frame)
        self.title = tk.Label(self.topframe, text = '⏱️ Measurements 🌡️', font=('Comic Sans MS', 26))

        # PT, TT, and LC measurements
        self.pt1 = MeasureWidget(self.frame, 'PT1', '[Pa]')
        self.pt2 = MeasureWidget(self.frame, 'PT2', '[Pa]')
        self.pt3 = MeasureWidget(self.frame, 'PT3', '[Pa]')
        self.pt4 = MeasureWidget(self.frame, 'PT4', '[Pa]')
        self.pt5 = MeasureWidget(self.frame, 'PT5', '[Pa]')
        self.pt6 = MeasureWidget(self.frame, 'PT6', '[Pa]')
        self.pt7 = MeasureWidget(self.frame, 'PT7', '[Pa]')
        self.pt8 = MeasureWidget(self.frame, 'PT8', '[Pa]')
        self.pt9 = MeasureWidget(self.frame, 'PT9', '[Pa]')
        self.tt1 = MeasureWidget(self.frame, 'TT1', '[*C]')
        self.tt2 = MeasureWidget(self.frame, 'TT2', '[*C]')
        self.tt3 = MeasureWidget(self.frame, 'TT3', '[*C]')
        self.tt4 = MeasureWidget(self.frame, 'TT4', '[*C]')
        self.tt5 = MeasureWidget(self.frame, 'TT5', '[*C]')
        self.lc1 = MeasureWidget(self.frame, 'LC1', '[g]')
        self.lc2 = MeasureWidget(self.frame, 'LC2', '[g]')
        self.lc3 = MeasureWidget(self.frame, 'LC3', '[g]')

    def render(self):
        self.title.pack(fill = 'x')
        self.topframe.pack(fill = 'x')
        self.pt1.render()
        self.pt2.render()
        self.pt3.render()
        self.pt4.render()
        self.pt5.render()
        self.pt6.render()
        self.pt7.render()
        self.pt8.render()
        self.pt9.render()
        self.tt1.render()
        self.tt2.render()
        self.tt3.render()
        self.tt4.render()
        self.tt5.render()
        self.lc1.render()
        self.lc2.render()
        self.lc3.render()
        self.frame.pack(side='left', fill='both', expand=True)

