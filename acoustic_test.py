from acoustic_model import Model
from acoustic_view import View
from acoustic_controller import Controller
from pydub import AudioSegment
import tkinter as tk


class App(tk. Tk):
    def __init__(self):
        super().__init__()

        self.title('Acoustic')
        self.geometry('1000x500')

        # create a model
        audio_converted = AudioSegment.from_file(r'C:\Users\JJord\PycharmProjects\Acoustics\AcousticProject\Florida_Polytechnic_University_5.m4a')
        audio_converted.export("Clap.wav", format="wav")
        audio_file = "Clap.wav"
        self.file_path = audio_file
        model = Model('Florida_Polytechnic_University_5.m4a')

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        for i in range(9):
            view.grid_rowconfigure(i, weight=1)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()