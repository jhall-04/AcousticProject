# imports
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# moved old code to model // putting it here was incorrect and my bad

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # load button
        self.load_button = ttk.Button(self, text='Load', command=self.load_button_pressed)
        self.load_button.grid(row=8, column=1, sticky="nsew")

        # File name
        self.name_label = ttk.Label(self, text='Name: ', foreground='black')
        self.name_label.grid(row=1, column=1, sticky='w')

        self.time_label = ttk.Label(self, text='Time: ', foreground='black')
        self.time_label.grid(row=2, column=1, sticky='w')

        self.frequency_label = ttk.Label(self, text='Frequency: ', foreground='black')
        self.frequency_label.grid(row=3, column=1, sticky='w')



        # set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def load_button_pressed(self):
        if self.controller:
            self.controller.load_data()
        