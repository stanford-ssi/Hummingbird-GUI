""" Top header """
import tkinter as tk

class Header:
    frame: tk.Frame

    def __init__(self, parent):
        # Create frame
        self.frame = tk.Frame(parent)

        # Tabs label
        self.title = tk.Label(self.frame, text='⛲⛲⛲⛲⛲ Fountain Hopper ⛲⛲⛲⛲⛲', font=('Comic Sans MS',32))
        self.subtitle = tk.Label(self.frame, text='🐦🐦🐦 Hummingbird GUI 🐦🐦🐦', font=('Comic Sans MS',28))

    def render(self):
        self.title.pack()
        self.subtitle.pack()
        self.frame.pack()
