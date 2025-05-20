'''
sets up main window and widgets

'''
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import queue
import time

import comm  

class GroundStationGUI:
    POLL_INTERVAL_MS = 200

    def __init__(self, master):
        self.master = master
        master.title("Hummingbird Ground Station")
        master.geometry("600x500")

        # Thread-safe queue for incoming sensor messages
        self._queue = queue.Queue()

        self._build_estop_frame()
        self._build_valve_frame()
        self._build_sensor_frame()
        self._build_log_frame()

        # Start background reader
        threading.Thread(target=self._sensor_reader, daemon=True).start()
        master.after(self.POLL_INTERVAL_MS, self._poll_queue)

    def _build_estop_frame(self):
        frm = tk.Frame(self.master, pady=10)
        frm.pack(fill="x")
        btn = tk.Button(
            frm, text="EMERGENCY STOP", bg="red", fg="white",
            font=("Comic sans", 24, "bold"), height=2,
            command=self._on_estop
        )
        btn.pack(fill="x", padx=20)

    def _build_valve_frame(self):
        frm = tk.LabelFrame(self.master, text="Valve Controls", padx=10, pady=10)
        frm.pack(fill="x", padx=20, pady=5)

        for vid in range(1, 6):  # assuming valves 1–5
            sub = tk.Frame(frm)
            sub.pack(fill="x", pady=2)
            lbl = tk.Label(sub, text=f"Valve {vid}", width=8)
            lbl.pack(side="left")

            btn_open = tk.Button(
                sub, text="Open",
                command=lambda i=vid: self._on_valve(i, True)
            )
            btn_open.pack(side="left", padx=5)

            btn_close = tk.Button(
                sub, text="Close",
                command=lambda i=vid: self._on_valve(i, False)
            )
            btn_close.pack(side="left", padx=5)

    def _build_sensor_frame(self):
        frm = tk.LabelFrame(self.master, text="Live Sensor Readings", padx=10, pady=10)
        frm.pack(fill="both", expand=True, padx=20, pady=5)

        self.sensor_text = scrolledtext.ScrolledText(frm, height=8, state="disabled")
        self.sensor_text.pack(fill="both", expand=True)

    def _build_log_frame(self):
        frm = tk.LabelFrame(self.master, text="TX/RX Log", padx=10, pady=10)
        frm.pack(fill="both", expand=True, padx=20, pady=5)

        self.log_text = scrolledtext.ScrolledText(frm, height=6, state="disabled")
        self.log_text.pack(fill="both", expand=True)

    # ─── Callbacks ────────────────────────────────────────────────────────────────

    def _on_estop(self):
        try:
            comm.send_estop()
            self._log("Sent EMERGENCY STOP")
        except Exception as e:
            messagebox.showerror("E-Stop Error", str(e))

    def _on_valve(self, valve_id, open_):
        cmd = "OPEN" if open_ else "CLOSE"
        try:
            comm.send_valve_command(valve_id, open_)
            self._log(f"Sent {cmd} Valve {valve_id}")
        except Exception as e:
            messagebox.showerror("Valve Error", str(e))

    # ─── Background reader ───────────────────────────────────────────────────────

    def _sensor_reader(self):
        """ Continuously read packets and push into queue. """
        while True:
            try:
                pkt = comm.read_sensor_packet()  # blocking or timed read
                self._queue.put(pkt)
            except Exception as e:
                self._queue.put(f"ERROR reading packet: {e}")
            time.sleep(0.01)

    def _poll_queue(self):
        """ Pull from queue and update display. """
        while not self._queue.empty():
            line = self._queue.get()
            self._append(self.sensor_text, line)
        self.master.after(self.POLL_INTERVAL_MS, self._poll_queue)

    # ─── Helpers ─────────────────────────────────────────────────────────────────

    def _append(self, widget, text):
        widget.configure(state="normal")
        widget.insert("end", f"{text}\n")
        widget.see("end")
        widget.configure(state="disabled")

    def _log(self, message):
        self._append(self.log_text, message)


if __name__ == "__main__":
    root = tk.Tk()
    app = GroundStationGUI(root)
    root.mainloop()




