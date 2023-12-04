from acoustic_view import Statistics
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
    def fileConversion(file_path):
        wav_audio = AudioSegment.from_file("audio.wav", format="wav")
        raw_audio = AudioSegment.from_file("audio.wav", format="raw",
                                        frame_rate=44100, channels=2, sample_width=2)

        wav_audio.export("audio1.mp3", format="mp3")
        raw_audio.export("audio2.mp3", format="mp3")

    def check_format(self, audio_file):
        # gets the file type before converting if not a wav
        file_extension = pathlib.Path(audio_file).suffix
        if file_extension != ".wav":
            audio_converted = AudioSegment.from_file(audio_file)
            audio_converted.export("Florida_Polytechnic_University_5.wav", format="wav")
            audio_file = "Florida_Polytechnic_University_5.wav"
        return audio_file

# temporary "main"
# switches out the old audio clip for the new working one.


audio_to_analyze = check_format(raw_audio)

# test for acoustic statistics
results = Statistics(audio_to_analyze)
results.get_length(audio_to_analyze)
results.get_highest_resonance(audio_to_analyze)



