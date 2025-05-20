import tkinter as tk 

class MeasureWidget:
    frame: tk.Frame
    partname: str
    units: str

    def __init__(self, parent, partname, units, default_entry = 0.0):
        self.frame = tk.Label(parent) #makes frame
        self.partname = partname
        self.units = units

        self.partname_box = tk.Label(self.frame, text = self.partname, font = ("Comic Sans MS", 20))
        self.measurement_box = tk.Label(self.frame, text = str(default_entry), font = ("Comic Sans MS", 20))
        self.units_box = tk.Label(self.frame, text = self.units, font = ("Comic Sans MS", 20))

    def render(self):
        # locations of the part name, measurements, and units 
        self.partname_box.pack(side = 'left', padx = 30, expand=True)
        self.measurement_box.pack(side = 'left', padx = 30, expand=True)
        self.units_box.pack(side = 'left', padx = 30, expand=True)
        self.frame.pack(fill = 'x', side = 'top')



