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

        # load button
        self.load_button = ttk.Button(self, text='Load', command=self.load_button_pressed)
        self.load_button.grid(row=8, column=1)

        self.high_button = ttk.Button(self, text='High', command=self.high_button_pressed)
        self.high_button.grid(row=8, column=4, padx=5, pady=5)

        self.mid_button = ttk.Button(self, text='Mid', command=self.mid_button_pressed)
        self.mid_button.grid(row=8, column=5, padx=5, pady=5)

        self.low_button = ttk.Button(self, text='Low', command=self.low_button_pressed)
        self.low_button.grid(row=8, column=6, padx=5, pady=5)

        self.all_button = ttk.Button(self, text='All', command=self.all_button_pressed)
        self.all_button.grid(row=8, column=7, padx=5, pady=5)



        # File name
        self.name_label = ttk.Label(self, text='Name: ', foreground='black')
        self.name_label.grid(row=1, column=1, sticky='w')

        self.time_label = ttk.Label(self, text='Time: ', foreground='black')
        self.time_label.grid(row=2, column=1, sticky='w')

        self.frequency_label = ttk.Label(self, text='Reverb: ', foreground='black')
        self.frequency_label.grid(row=3, column=1, sticky='w')

        self.placeholder_fig = Figure(figsize=(4, 2), dpi=100)
        self.ax = self.placeholder_fig.add_subplot(111)
        self.ax.axis('off')  # Turn off axis to create a blank space
        self.placeholder_fig.patch.set_visible(False)  # Hide the figure patch
        self.canvas = FigureCanvasTkAgg(self.placeholder_fig, self)
        self.canvas.get_tk_widget().grid(row=4, column=1, sticky='w')

        self.placeholder_fig1 = Figure(figsize=(3, 2), dpi=100)
        self.ax1 = self.placeholder_fig1.add_subplot(111)
        self.ax1.axis('off')  # Turn off axis to create a blank space
        self.placeholder_fig1.patch.set_visible(False)  # Hide the figure patch
        self.canvas1 = FigureCanvasTkAgg(self.placeholder_fig1, self)
        self.canvas1.get_tk_widget().grid(row=4, column=4, columnspan=4, padx=15)




        # set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def load_button_pressed(self):
        if self.controller:
            self.controller.load_data()

    def plot_button_pressed(self):
        if self.controller:
            '''
            canvas1 = FigureCanvasTkAgg(self.controller.model.get_rd60_display('high'), self.upper_frame)
            canvas1.draw()
            canvas1.get_tk_widget().grid(row=3, column=1, sticky='w')
            '''
            self.controller.display_plot_in_tkinter()

    def high_button_pressed(self):
        model = Model()
        self.frequency_label['text'] = f'Reverb: {model.get_rd60_display("high")}'

    def mid_button_pressed(self):
        model = Model()
        self.frequency_label['text'] = f'Reverb: {model.get_rd60_display("mid")}'


    def low_button_pressed(self):
        model = Model()
        self.frequency_label['text'] = f'Reverb: {model.get_rd60_display("low")}'


    def all_button_pressed(self):
        # placeholder
        pass





        