# live microscope feed & data vis
import tkinter as tk
from control_widget import ControlWidget

class RightPanel:
    frame: tk.Frame

    def __init__(self, parent):
        # Create frame
        self.frame = tk.Label(parent, borderwidth=5, relief='solid')

        # top frame
        self.topframe = tk.Frame(self.frame)
        self.title = tk.Label(self.topframe, text = '🎛️ Controls 🎛️', font=('Comic Sans MS', 26))

        # PV and SV controls
        self.pv1 = ControlWidget(self.frame, 'PV1')
        self.pv2 = ControlWidget(self.frame, 'PV2')
        self.pv3 = ControlWidget(self.frame, 'PV3')
        self.pv4 = ControlWidget(self.frame, 'PV4')
        self.sv1 = ControlWidget(self.frame, 'SV1')
        self.sv2 = ControlWidget(self.frame, 'SV2')
        self.sv3 = ControlWidget(self.frame, 'SV3')
        self.sv4 = ControlWidget(self.frame, 'SV4')

        # E-stop button
        self.estop_button = tk.Button(self.frame, foreground='red', text='✋ EMERGENCY STOP ✋', font=('Comic Sans MS', 26), command=None)

    def render(self):
        self.title.pack(fill = 'x')
        self.topframe.pack(fill = 'x')
        self.pv1.render()
        self.pv2.render()
        self.pv3.render()
        self.pv4.render()
        self.sv1.render()
        self.sv2.render()
        self.sv3.render()
        self.sv4.render()
        self.estop_button.pack(fill='x', expand=True)
        self.frame.pack(side='left', fill='both', expand=True)