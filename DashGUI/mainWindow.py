'''
Creates a dashboard for Hummingbird using Tkinter 
'''
import tkinter as tk 
import tkinter.ttk as ttk

class MainWindow(tk.Tk):

    #initialize the main window 
    def __init__(self):
        super().__init__() # self is now the standard "root"
        self.withdraw() 

        # Set fullscreen
        self.fullscreen = False
        self.attributes('-fullscreen', False)
        self.state('normal') # start maximized, not full screen

        # create the the overall container frame (mainframe), then pack the frame into the main window
        self.mainframe = ttk.Frame(self)
        self.mainframe.pack(fill=tk.BOTH, expand=1)

        # Set overall style and create any default styles for Tk Objects #
        self.tk.call('source', 'lib/black.tcl')
        self.style = ttk.Style()
        self.style.theme_use('black')
        fs = 7
        self.style.configure('TableHeader.TLabel', font = ('TkDefaultFont', fs,'bold'), foreground = 'white', background = "#323232",anchor = 'center')
        self.style.configure('TableHeader.TButton', font = ('TkDefaultFont', fs,'bold'), foreground = 'white', background = "#323232",anchor = 'center')
        self.style.configure('TableEntry.TLabel', font = ('TkDefaultFont', fs,'bold'), background = "#000000",anchor = 'center')
        self.style.configure('OpenClose.TButton',background='black',foreground='white', highlightthickness='40',font=('TkDefaultFont', fs, 'bold'),anchor='center')
        self.style.map('OpenClose.TButton',foreground=[('alternate', 'black'),('!alternate', 'white')],
                                        background=[('!pressed','alternate', 'white'),('!pressed','!alternate', 'black'),('pressed','alternate', '#DDDDDD'),('pressed','!alternate', '#222222')], 
                                        relief=[('pressed', 'groove'),('!pressed','alternate','raised'),('!pressed', '!alternate','sunken')])
        self.style.configure('Fire.TButton',background='red',foreground='white', highlightthickness='20',font=('TkDefaultFont', fs, 'bold'))
        self.style.map('Fire.TButton',foreground=[('alternate', 'white'),('!alternate', '!disabled','white'),('!alternate', 'disabled','#888888')],
                                        background=[('!pressed','alternate', 'black'),('!pressed','!disabled','!alternate', '#a83232'),('!pressed','disabled','!alternate', '#222222'),('pressed','alternate', '#222222'),('pressed','!alternate', '#aa1111')], 
                                        relief=[('pressed', 'groove'),('!pressed','alternate','sunken'),('!pressed', '!alternate','!disabled','raised'),('!pressed', '!alternate','disabled','sunken')])

        # Bind close event to stop animation updating if the window is closed
        self.bind("<Destroy>", lambda event: self.kill())

        # Pack the frame with constituent components
        self.config(menu = self.menubar)
        num_cols = 4
        num_rows = 5
        panepad = 15
        self.channelpane.grid( row=0, column=0, columnspan=1, sticky='nsew', pady=(0,panepad))
        self.solenoidpane.grid( row=1, column=0, columnspan=1, sticky='nsew', pady=(0,panepad))
        self.squibpane.grid( row=2, column=0, columnspan=1, sticky='nsew', pady=(0,0))
        self.graphpanes.grid( row=0, column=1, rowspan=num_rows-2, columnspan=2, sticky='nsew')
        self.buttonpane.grid( row=0, column=num_cols-1, rowspan=num_rows-2, columnspan=1, sticky='nsew')
        self.printbar.grid( row=3, column=0, rowspan=1, columnspan=num_cols//2, sticky='nsew')
        self.cmdpane.grid( row=4, column=0, rowspan=1, columnspan=num_cols//2, sticky='nsew')
        self.recordpane.grid( row=3, column=num_cols//2, rowspan=2, columnspan=num_cols//2, sticky='nsew')
        
        # set the rows/columns to expand equally to fill space as the window is resized
        for i in range(num_cols):
            self.mainframe.columnconfigure(i, weight = 1 )
        for i in range(num_rows-2):
            self.mainframe.rowconfigure(i, weight = 1 ) # exclude the top row

        # Set fullscreen
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)
        self.bind("<<Update>>", self.update)
        self.bind("<<UPDATE_CH>>", self.update_channels)
        self.bind("<<REDRAW>>", self.redraw)


    #closes the window
    def kill(self, event=None):
        self.destroy()

    #switches between fullscreen and non fullscreen
    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.attributes("-fullscreen", self.fullscreen)

    #end full screen
    def end_full_screen(self, event=None):
        self.fullscreen = False
        self.attributes("-fullscreen", False)