import socket
import tkinter as tk
import tkinter.ttk as ttk


PI_IP = '192.168.0.108'  # Updated Raspberry Pi's IP address
PORT = 65432

def send_command(cmd, pin):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((PI_IP, PORT))
        s.sendall(f"{cmd},{pin}".encode())
        response = s.recv(1024)
        print('Received', response.decode())

def button_press(event, pin):
    send_command('ON', pin)

def button_release(event, pin):
    send_command('OFF', pin)

def toggle_pin(state, pin):
    cmd = 'ON' if state else 'OFF'
    send_command(cmd, pin)

# Create GUI
root = tk.Tk()
root.title("GPIO Control")

# Define GPIOs and their labels
sliders = [(17, "PV2N"), (18, "Unassigned"), (27, "Unassigned")]
buttons = [(22, "Big Boy Left"), (23, "Big Boy Right")]

# Add sliders
for pin, label in sliders:
    frame = tk.Frame(root)
    frame.pack(pady=5)

    tk.Label(frame, text=label).pack(side=tk.LEFT)
    slider = tk.Scale(frame, from_=0, to=1, orient=tk.HORIZONTAL, command=lambda val, p=pin: toggle_pin(int(val), p))
    slider.pack(side=tk.LEFT)

# Add buttons
for pin, label in buttons:
    frame = tk.Frame(root)
    frame.pack(pady=5)

    tk.Label(frame, text=label).pack(side=tk.LEFT)
    btn = tk.Button(frame, text=label)
    btn.pack(side=tk.LEFT)
    btn.bind('<ButtonPress-1>', lambda event, p=pin: button_press(event, p))
    btn.bind('<ButtonRelease-1>', lambda event, p=pin: button_release(event, p))

root.mainloop()