import audioread
import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import AudioFileClip as aClip
from scipy.io import wavfile

# temporary placeholder, replace with call for import from controller instead of hardcoded directory
sample_rate, data = wavfile.read("Florida_Polytechnic_University_5.wav")
spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, \
NFFT=1024, cmap=plt.get_cmap('autumn_r'))
cbar = plt.colorbar(im)

# used for rdt60 plotting


def find_target_frequency(freqs):
    # selects a frequency under 1kHZ
    for x in freqs:
        if x > 1000:
            break
    return x


def frequency_check():
    # find the frequency to check
    #
    global target_frequency
    target_frequency = find_target_frequency(freqs)
    index_of_frequency = np.where(freqs == target_frequency)[0][0]
    # gets the sounds data at this freq
    data_for_frequency = spectrum[index_of_frequency]
    # looks at change in single for a value in dB
    # // runtime error currently caused by there being no sound at the beginning of the file, fix in cleaning
    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun


class Statistics:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def get_length(self, audio_file):
        with audioread.audio_open(audio_file) as f:
            # placeholder until gui is introduced
            print ("The full duration of the file audio clip is: ", f.duration, "seconds")

    def get_rd60_display(self):
        data_in_db = frequency_check()
        plt.figure("Decibels over time")

        plt.plot(t, data_in_db, linewidth=1,  color='red')

        plt.xlabel('Time (s)')

        plt.ylabel('Power(dB)')

        # find index of max value
        index_of_max = np.argmax(data_in_db)
        value_of_max = data_in_db[index_of_max]
        plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

        # slice array from max value
        sliced_array = data_in_db[index_of_max:]
        value_of_max_less_5 = value_of_max - 5

        # find nearest value of < 5dB
        def find_nearest_value(array, value):
            array = np.asarray(array)
            idx = (np.abs(array - value)).argmin()
            return array[idx]

        value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
        index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
        plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

        # slice array from a max-5dB
        value_of_max_less_25 = value_of_max - 25
        value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
        index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
        plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')

        rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]
        rt60 = 3 * rt20

        plt.grid()
        plt.show()

        print(f'The RT60 reverb time at freq {int(target_frequency)}Hz is {round(abs(rt60), 2)} seconds')


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


