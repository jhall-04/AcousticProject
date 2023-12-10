# Creation of Summary statistics:
"""
1. Length of Audio Sample

2. RT60 Value: RT60 = 0.049 V/Σ S α

Σ = sabins (total room absorption at given frequency)

S = surface area of material (feet squared)

α = sound absorption coefficient at given frequency or the NRC

V = volume of the space (feet cubed)

a = sabins (total room absorption at given frequency)

3. Frequency mean/median/largest/lowest (for future graphing)
"""
# imports
import audioread
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Statistics:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def get_length(self, audio_file):
        with audioread.audio_open(audio_file) as f:
            print ("The full duration of the file audio clip is: ", f.duration, "seconds")
    def get_frequencies(self, audio_file):
        # get the highest frequency
        # get the medium/average frequency
        # get the lowest frequency
        print("test")



class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # load button
        self.load_button = ttk.Button(self, text='Load', command=self.load_button_pressed)
        self.load_button.grid(row=8, column=1, sticky="nsew")

        # File name
        self.name_label = ttk.Label(self, text='Name: ', foreground='black')
        self.name_label.grid(row=1, column=1)

        self.name_label = ttk.Label(self, text='Time: ', foreground='black')
        self.name_label.grid(row=2, column=1)

        self.name_label = ttk.Label(self, text='Frequency: ', foreground='black')
        self.name_label.grid(row=3, column=1)

        # Open the image file using Pillow
        img = Image.open('img.png')
        img = ImageTk.PhotoImage(img)

        # Create a label to display the image
        self.waveform = tk.Label(self, image=img)
        self.waveform.grid(row=4, column=1)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def load_button_pressed(self):
        if self.controller:
            self.controller.load_data()
        