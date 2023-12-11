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
        canvas_widget = self.model.plot_waveform(self.view)
        # Add the Matplotlib canvas to the Tkinter window
        canvas_widget.grid(row=4, column=1, sticky='w')

    def display_rt_in_tkinter(self, root, freq_range):
        time, controller_widget = self.model.get_rd60_display(root, freq_range)
        self.view.reverb_label['text'] = f'Reverb: {time} seconds'
        controller_widget.grid(row=4, column=4, columnspan=4, sticky='w')
    
    def load_data(self):
        file = pathlib.Path(self.model.load()).name
        if file != '':
            self.view.name_label['text'] = f'Name: {file}'
            self.view.time_label['text'] = f'Time: {self.model.get_length(raw_audio)}'
            self.view.frequency_label['text'] = f'Frequency: {self.model.get_frequency()}'
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
