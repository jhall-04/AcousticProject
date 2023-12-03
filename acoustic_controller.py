from acoustic_statistics import Statistics
from pydub import AudioSegment
import pathlib

# --comment to be removed
# replace the direct file call with the tkinter import once completed
raw_audio = "Florida_Polytechnic_University_5.wav"


# --comment to be removed
# needed to convert to wav for the purposes of having a file to read for statistics so I went ahead and finished this
# part of the cleanup code while I was at it


def check_format(audio_file):
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
print(results.get_length(audio_to_analyze))



