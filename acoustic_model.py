from moviepy.editor import AudioFileClip as aClip

class Model:
    def __init__(self, file_path):
        self.file_path = file_path


    @property
    def file_path(self):
        return self._file_path
    
    @file_path.setter
    def file_path(self, value):
        try:
            audio = aClip(value)
            self._file_path = value
        except Exception:
            raise ValueError(f"This is not an audio file: {value}")