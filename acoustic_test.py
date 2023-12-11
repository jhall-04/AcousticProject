from acoustic_model import Model
from acoustic_view import View
from acoustic_controller import Controller
from pydub import AudioSegment
import tkinter as tk


class App(tk. Tk):
    def __init__(self):
        super().__init__()

        self.title('Acoustic')
        self.geometry('1300x400')

        # create a model
        model = Model()



        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()