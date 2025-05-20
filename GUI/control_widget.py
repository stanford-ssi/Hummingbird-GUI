import tkinter as tk 

class ControlWidget:
    frame: tk.Frame
    partname: str
    units: str

    def __init__(self, parent, partname, current_state = 'OFF'):
        self.frame = tk.Label(parent) #makes frame
        self.partname = partname

        self.partname_box = tk.Label(self.frame, text = self.partname, font = ("Comic Sans MS", 20))
        self.state_box = tk.Label(self.frame, text = current_state, font=("Comic Sans MS", 20))
        self.on_button = tk.Button(self.frame, foreground='green', text='ON', font=('Comic Sans MS',16), command=None)
        self.off_button = tk.Button(self.frame, foreground='blue', text='OFF', font=('Comic Sans MS',16), command=None)


    def render(self):
        self.partname_box.pack(side = 'left', padx = 30, expand=True)
        self.state_box.pack(side = 'left', padx = 30, expand=True)
        self.on_button.pack(side = 'left', padx = 30, expand=True)
        self.off_button.pack(side = 'left', padx = 30, expand=True)
        self.frame.pack(fill = 'x', side = 'top')



