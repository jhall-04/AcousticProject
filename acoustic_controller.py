# Credit to the following library: https://github.com/jiaaro/pydub
from acoustic_statistics import Statistics
from pydub import AudioSegment
import pathlib

# replace the direct file call with the tkinter import once completed
raw_audio = "Florida_Polytechnic_University_5.m4a"

#wav_audio = AudioSegment.from_file("audio.wav", format="wav")
#raw_audio = AudioSegment.from_file("audio.wav", format="raw",
                                   #frame_rate=44100, channels=2, sample_width=2)

#wav_audio.export("audio1.mp3", format="mp3")
#raw_audio.export("audio2.mp3", format="mp3")

# --comment to be removed
# needed to convert to wav so I did some placeholder work for the clean up


def check_format(audio_file):
    # gets the file type before converting if not a wav
    file_extension = pathlib.Path(audio_file).suffix
    if file_extension != ".wav":
        print("There may be issues due to", file_extension, "not being in .wav format")
        # temporarily commented out, this needs ffmpeg to install which has caused signifigant issues, reconviene later
        # though honestly in looking at directions i am unsure if this calls for the file to be converted to .wav or
        # if its checking for any corruption that may have happened during the conversion
        #--------------------------------------------------------------------------
        # audio_converted = AudioSegment.from_file(audio_file, file_extension)
        # audio_converted.export("Test_Audio.wav", format="wav")

# test for cleaning test
check_format(raw_audio)

# test for acoustic statistics
results = Statistics(raw_audio).get_length(raw_audio)



