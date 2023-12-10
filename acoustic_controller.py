from acoustic_model import Model
from pydub import AudioSegment
import pathlib
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


raw_audio = "Clap.wav"


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_plot_in_tkinter(self):
        canvas_widget = self.model.plot_waveform(self.view, self.model.file_path)
        # Add the Matplotlib canvas to the Tkinter window
        canvas_widget.grid(row=4, column=1, sticky='w')
    
    def load_data(self):
        file = pathlib.Path(self.model.load()).name
        self.view.name_label['text'] = f'Name: {file}'
        self.view.time_label['text'] = f'Time: {self.model.get_length(raw_audio)}'
        self.display_plot_in_tkinter()

# --comment to be removed
# placeholder code for testing modeling/data analysis code:
'''
s = Model()
s.get_length(raw_audio)
s.get_rd60_display("mid")
s.get_rd60_display("low")
s.get_rd60_display("high")
'''
