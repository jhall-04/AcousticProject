# Creation of Summary statistics:
"""
1. Length of Audio Sample

2. RT60 Value: RT60 = 0.049 V/Σ S α

Σ = sabins (total room absorption at given frequency)

S = surface area of material (feet squared)

α = sound absorption coefficient at given frequency or the NRC

V = volume of the space (feet cubed)

a = sabins (total room absorption at given frequency)

3. Frequency mean/median/largest/lowest (for future graphing)
"""
# imports
import audioread

class Statistics:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def get_length(self, audio_file):
        with audioread.audio_open(audio_file) as f:
            print ("The full duration of the file audio clip is: ", f.duration, "seconds")
    def get_frequencies(self, audio_file):
        # get the highest frequency
        # get the medium/average frequency
        # get the lowest frequency
        print("test")