from acoustic_model import Model
from acoustic_view import Statistics, View
from pydub import AudioSegment
import pathlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# --comment to be removed
# replace the direct file call with the tkinter import once completed
raw_audio = "Florida_Polytechnic_University_5.wav"


# --comment to be removed
# needed to convert to wav for the purposes of having a file to read for statistics so I went ahead and finished this
# part of the cleanup code while I was at it


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_plot_in_tkinter(self, root, fig):
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()

        # Add the Matplotlib canvas to the Tkinter window
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)



        root.mainloop()
    
    def load_data(self):
        self.model.load()
        self.view.name_label.text = self.model.file_path
    

