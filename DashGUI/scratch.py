import socket
import threading
import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Configure your Pi connection
PI_IP = '192.168.0.108'
PORT = 65432
POLL_INTERVAL = 1000  # ms between sensor updates

class SensorDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hummingbird Sensor Dashboard")
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        container = ttk.Frame(self, padding=10)
        container.pack(fill=tk.BOTH, expand=True)

        # dicts for sparkline state
        self.spark_axes = {}   # maps sensor key -> (ax, canvas)
        self.spark_data = {}   # maps sensor key -> list of last readings

        # Build panels (we’ll only show Pressure as an example)
        self.create_pressure_panel(container)
        # ... create other panels ...

        self.after(POLL_INTERVAL, self.update_sensors)

    def create_pressure_panel(self, parent):
        frame = ttk.Labelframe(parent, text="PTs (Pressure 1-10)")
        frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.pt_labels = {}
        for i in range(1, 11):
            sub = ttk.Frame(frame)
            sub.grid(row=(i-1)//5, column=(i-1)%5, padx=2, pady=2)

            # 1) Numeric label
            lbl = ttk.Label(sub, text=f"PT{i}: -- psi", width=12)
            lbl.pack(side=tk.TOP)
            self.pt_labels[i] = lbl

            # 2) Sparkline canvas
            fig, ax = plt.subplots(figsize=(1.5, 0.3))
            ax.axis('off')
            canvas = FigureCanvasTkAgg(fig, master=sub)
            canvas.get_tk_widget().pack(side=tk.BOTTOM)
            self.spark_axes[f"PT{i}"] = (ax, canvas)
            self.spark_data[f"PT{i}"] = []

    def update_sensors(self):
        # Pressure + sparkline update
        for i, lbl in self.pt_labels.items():
            key = f"PT{i}"
            resp = send_command('READ', 'PT', i)
            try:
                val = float(resp)
            except ValueError:
                val = 0.0

            # update numeric text
            lbl.config(text=f"PT{i}: {val:.1f} psi")

            # append to history, keep last 60
            data = self.spark_data[key]
            data.append(val)
            self.spark_data[key] = data[-60:]

            # redraw sparkline
            ax, canvas = self.spark_axes[key]
            ax.clear()
            ax.plot(self.spark_data[key])
            ax.axis('off')
            canvas.draw()

        # ... repeat similar blocks for TC and LC sparklines if you add them ...``
        self.after(POLL_INTERVAL, self.update_sensors)


if __name__ == '__main__':
    app = SensorDashboard()
    app.mainloop()