# imports
import matplotlib.pyplot as plt

from acoustic_model import Model
from acoustic_controller import Controller
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.loaded = False

        # load button
        self.load_button = ttk.Button(self, text='Load', command=self.load_button_pressed)
        self.load_button.grid(row=8, column=1)

        self.high_button = ttk.Button(self, text='High', command=self.high_button_pressed)
        self.high_button.grid(row=8, column=4, padx=5, pady=5)

        self.mid_button = ttk.Button(self, text='Mid', command=self.mid_button_pressed)
        self.mid_button.grid(row=8, column=5, padx=5, pady=5)

        self.low_button = ttk.Button(self, text='Low', command=self.low_button_pressed)
        # since clicking the buttons one after the other forms the "all" graph, there isn't a need for a specific
        # button, at least for mvp
        self.low_button.grid(row=8, column=6, padx=5, pady=5)

        self.all_button = ttk.Button(self, text='All', command=self.all_button_pressed)
        self.all_button.grid(row=8, column=7, padx=5, pady=5)

        self.spect_button = ttk.Button(self, text='Spect', command=self.spect_button_pressed)
        self.spect_button.grid(row=8, column=8, padx=5, pady=5)




        # File name
        self.name_label = ttk.Label(self, text='Name: ', foreground='black')
        self.name_label.grid(row=1, column=1, sticky='w')

        self.time_label = ttk.Label(self, text='Time: ', foreground='black')
        self.time_label.grid(row=2, column=1, sticky='w')

        self.frequency_label = ttk.Label(self, text='Frequency: ', foreground='black')
        self.frequency_label.grid(row=3, column=1, sticky='w')

        self.reverb_label = ttk.Label(self, text='Reverb: ', foreground='black')
        self.reverb_label.grid(row=3, column=4, columnspan=4, sticky='w')

        self.placeholder_fig = Figure(figsize=(4.8, 2), dpi=100)
        self.ax = self.placeholder_fig.add_subplot(111)
        self.ax.axis('off')  # Turn off axis to create a blank space
        self.placeholder_fig.patch.set_visible(False)  # Hide the figure patch
        self.canvas = FigureCanvasTkAgg(self.placeholder_fig, self)
        self.canvas.get_tk_widget().grid(row=4, column=1, sticky='w')

        self.placeholder_fig1 = Figure(figsize=(4.8, 2), dpi=100)
        self.ax1 = self.placeholder_fig1.add_subplot(111)
        self.ax1.axis('off')  # Turn off axis to create a blank space
        self.placeholder_fig1.patch.set_visible(False)  # Hide the figure patch
        self.canvas1 = FigureCanvasTkAgg(self.placeholder_fig1, self)
        self.canvas1.get_tk_widget().grid(row=4, column=4, columnspan=5)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def load_button_pressed(self):
        if self.controller:
            self.controller.load_data()
            self.loaded = True

    def plot_button_pressed(self):
        if self.controller and self.loaded:
            '''
            canvas1 = FigureCanvasTkAgg(self.controller.model.get_rd60_display('high'), self.upper_frame)
            canvas1.draw()
            canvas1.get_tk_widget().grid(row=3, column=1, sticky='w')
            '''
            self.controller.display_plot_in_tkinter()

    def high_button_pressed(self):
        if self.controller and self.loaded:
            self.controller.display_rt_in_tkinter(self, "high")

    def mid_button_pressed(self):
        if self.controller and self.loaded:
            self.controller.display_rt_in_tkinter(self, "mid")

    def low_button_pressed(self):
        if self.controller and self.loaded:
            self.controller.display_rt_in_tkinter(self, "low")

    def all_button_pressed(self):
        if self.controller and self.loaded:
            self.reverb_label['text'] = f'Reverb: {round((self.controller.model.get_rd60_display("high") + self.controller.model.get_rd60_display("mid") + self.controller.model.get_rd60_display("low"))/3, 2)} seconds'

    def spect_button_pressed(self):
        if self.controller and self.loaded:
            pass





        