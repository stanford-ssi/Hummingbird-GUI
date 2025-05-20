'''
sets up main window
'''

import tkinter as tk 
from header import Header  
from body import Body 

def main():
    # create main window 
    window = tk.Tk()
    window.title("Hummingbird GUI")
    window.geometry("1200x800")

    # create header(title)
    header = Header(window)
    header.render()

    # create body 
    body = Body(window)
    body.render()

    # left panel: reads measurements from PTs, TTs, load cells

    # right panel: controls solenoid and power valves + estop 

    # start event loop
    window.mainloop()

if __name__ == "__main__":
    main()