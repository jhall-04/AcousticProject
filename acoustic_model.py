from moviepy.editor import AudioFileClip as aClip
from pydub import AudioSegment
import pathlib
import os
from tkinter import filedialog as fd

class Model:
    def __init__(self, file_path):
        self.file_path = file_path


    @property
    def file_path(self):
        return self._file_path
    
    @file_path.setter
    def file_path(self, value):
        if not os.path.exists(value):
            raise ValueError(f"Path {value} not found")
        try:
            audio = aClip(value)
            self._file_path = value
        except Exception:
            raise ValueError(f"This is not an audio file: {value}")
    

    def check_format(self, audio_file):
    # gets the file type before converting if not a wav
        file_extension = pathlib.Path(audio_file).suffix
        if file_extension != ".wav":
            audio_converted = AudioSegment.from_file(audio_file)
            audio_converted.export("Clap.wav", format="wav")
            audio_file = "Clap.wav"
            self.file_path = audio_file
    def mono_audio(self):
        audio = AudioSegment.from_wav(self.file_path)
        audio.set_channels(1)
        audio.export("Clap.wav", format="wav")
    
    def load(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        self.file_path = filename
    


model = Model("Florida_Polytechnic_University_5.m4a")
model.check_format(model.file_path)
model.file_path = "Clap.wav"
print(model.file_path)