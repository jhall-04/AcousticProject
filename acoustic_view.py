from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.loaded = False

        # Load button prompts user to open an audio file
        self.load_button = ttk.Button(self, text='Load', command=self.load_button_pressed)
        self.load_button.grid(row=8, column=1)

        # displays the rt60 of the high frequency range
        self.high_button = ttk.Button(self, text='High', command=self.high_button_pressed)
        self.high_button.grid(row=8, column=4, padx=5, pady=5)

        # displays the rt60 of the mid frequency range
        self.mid_button = ttk.Button(self, text='Mid', command=self.mid_button_pressed)
        self.mid_button.grid(row=8, column=5, padx=5, pady=5)

        # displays the rt60 of the low frequency range
        self.low_button = ttk.Button(self, text='Low', command=self.low_button_pressed)
        self.low_button.grid(row=8, column=6, padx=5, pady=5)

        # displays the rt60 of all frequency ranges
        self.all_button = ttk.Button(self, text='All', command=self.all_button_pressed)
        self.all_button.grid(row=8, column=7, padx=5, pady=5)

        # displays the spectogram of the audio file
        self.spect_button = ttk.Button(self, text='Spect', command=self.spect_button_pressed)
        self.spect_button.grid(row=8, column=8, padx=5, pady=5)




        # File name
        self.name_label = ttk.Label(self, text='Name: ', foreground='black')
        self.name_label.grid(row=1, column=1, sticky='w')

        # Audio length
        self.time_label = ttk.Label(self, text='Time: ', foreground='black')
        self.time_label.grid(row=2, column=1, sticky='w')

        # Resonant frequency
        self.frequency_label = ttk.Label(self, text='Frequency: ', foreground='black')
        self.frequency_label.grid(row=3, column=1, sticky='w')

        # RT60 value
        self.reverb_label = ttk.Label(self, text='Reverb: ', foreground='black')
        self.reverb_label.grid(row=3, column=4, columnspan=4, sticky='w')

        # Holds space until graphs generated
        self.placeholder_fig = Figure(figsize=(4.8, 2), dpi=100)
        self.ax = self.placeholder_fig.add_subplot(111)
        self.ax.axis('off')
        self.placeholder_fig.patch.set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.placeholder_fig, self)
        self.canvas.get_tk_widget().grid(row=4, column=1, sticky='w')

        self.placeholder_fig1 = Figure(figsize=(4.8, 2), dpi=100)
        self.ax1 = self.placeholder_fig1.add_subplot(111)
        self.ax1.axis('off')
        self.placeholder_fig1.patch.set_visible(False)
        self.canvas1 = FigureCanvasTkAgg(self.placeholder_fig1, self)
        self.canvas1.get_tk_widget().grid(row=4, column=4, columnspan=5)

        # set the controller
        self.controller = None

    # connects view with controller
    def set_controller(self, controller):
        self.controller = controller

    # implements load button functionality
    def load_button_pressed(self):
        if self.controller:
            self.controller.load_data()

    # implements high button functionality
    def high_button_pressed(self):
        if self.controller and self.loaded:
            self.controller.display_rt_in_tkinter("high")

    # implements mid button functionality
    def mid_button_pressed(self):
        if self.controller and self.loaded:
            self.controller.display_rt_in_tkinter("mid")

    # implements low button functionality
    def low_button_pressed(self):
        if self.controller and self.loaded:
            self.controller.display_rt_in_tkinter("low")

    # implements all button functionality
    def all_button_pressed(self):
        if self.controller and self.loaded:
            self.controller.display_all_rt_in_tkinter()

    # implements spectogram button functionality
    def spect_button_pressed(self):
        if self.controller and self.loaded:
            self.controller.display_spectogram_in_tkinter()
