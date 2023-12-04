from acoustic_model import Model
from acoustic_view import Statistics, View
from pydub import AudioSegment
import pathlib

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

    def check_format(self, audio_file):
        # gets the file type before converting if not a wav
        file_extension = pathlib.Path(audio_file).suffix
        if file_extension != ".wav":
            audio_converted = AudioSegment.from_file(audio_file)
            audio_converted.export("Clap.wav", format="wav")
            audio_file = "Clap.wav"
        return audio_file
