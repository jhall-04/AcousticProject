import pathlib


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.raw_audio = "Clap.wav"

    def display_plot_in_tkinter(self):
        canvas_widget = self.model.plot_waveform(self.view)
        # Add the Matplotlib canvas to the Tkinter window
        canvas_widget.grid(row=4, column=1, sticky='w')

    def display_rt_in_tkinter(self, freq_range):
        time, controller_widget = self.model.get_rd60_display(self.view, freq_range)
        self.view.reverb_label['text'] = f'Reverb: {time} seconds'
        self.view.canvas1 = controller_widget
        self.view.canvas1.grid(row=4, column=4, columnspan=5, sticky='w')

    def display_spectogram_in_tkinter(self):
        self.view.reverb_label['text'] = ''
        self.view.canvas1 = self.model.plot_spectogram(self.view)
        self.view.canvas1.grid(row=4, column=4, columnspan=5, sticky='w')
    
    def load_data(self):
        file = pathlib.Path(self.model.load()).name
        if file != '':
            self.view.name_label['text'] = f'Name: {file}'
            self.view.time_label['text'] = f'Time: {self.model.get_length(self.raw_audio)}'
            self.view.frequency_label['text'] = f'Frequency: {self.model.get_frequency()}'
            self.display_plot_in_tkinter()
            self.view.loaded = True

    def display_all_rt_in_tkinter(self):
        time_h, controller_widget_h = self.model.get__all_rd60_display(self.view)

        self.view.reverb_label['text'] = f'Difference: {time_h - 0.5} seconds'
        self.view.canvas1 = controller_widget_h
        self.view.canvas1.grid(row=4, column=4, columnspan=5, sticky='w')

