import audioread
import numpy as np
import matplotlib.pyplot as plt
import wave
from moviepy.editor import AudioFileClip as aClip
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy.io import wavfile
from pydub import AudioSegment
import pathlib
import os
from tkinter import filedialog as fd

# temporary placeholder, replace with call for import from controller instead of hardcoded filepath
sample_rate, data = wavfile.read("Florida_Polytechnic_University_5.wav")

# code for plotting the spectrogram of the .wav file
plt.figure("Spectrogram")

plt.xlabel('Time (s)')

plt.ylabel('Frequency(Hz)')
spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('viridis'))
cbar = plt.colorbar(im)

cbar.set_label('Intensity (dB)')


# used for rdt60 plotting:
def find_target_frequency(freqs, freq_range):
    # selects a frequency under 1kHZ, midrange
    if freq_range == "high":
        for x in freqs:
            if 10000 > x > 5000:
                break
    elif freq_range == "low":
        for x in freqs:
            if 250000000 > x > 60000000:
                break
    else:
        for x in freqs:
            if x > 1000:
                break

    return x

# 10000 > x > 5000: high
# 250000000 > x > 60000000: low

def frequency_check(freq_range):
    # find the frequency to check
    global target_frequency
    target_frequency = find_target_frequency(freqs, freq_range)
    # gets index of the freq in the array
    index_of_frequency = np.where(freqs == target_frequency)[0][0]
    # gets the sounds data at this freq
    data_for_frequency = spectrum[index_of_frequency]
    # natural log is used to get the "more natural" audio output
    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun


class Model:
    def __init__(self):
        self.file_path = ''

    @property
    def file_path(self):
        return self._file_path
    
    @file_path.setter
    def file_path(self, value):
        if value == '':
            self._file_path = ''
        elif not os.path.exists(value):
            raise ValueError(f"Path {value} not found")
        try:
            self.check_format(value)
            self._file_path = 'Clap.wav'
        except Exception:
            raise ValueError(f"This is not an audio file: {value}")

    def check_format(self, audio_file):
    # gets the file type before converting if not a wav
        file_extension = pathlib.Path(audio_file).suffix.lower()
        print(file_extension[1:])
        if file_extension == ".mp3":
            audio_converted = AudioSegment.from_file(audio_file)
            audio_converted.set_channels(1)
            audio_converted.export("Clap.wav", format="wav")
            self._file_path = "Clap.wav"
        elif file_extension == ".wav":
            audio = AudioSegment.from_file(audio_file)
            audio.set_channels(1)
            audio.export("Clap.wav", format="wav")
            self._file_path = "Clap.wav"
        return self.file_path
    
    def load(self):
        filetypes = (
            ('All files', '*.*'),
            ('Text files', '*.txt*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        self.file_path = filename
        return filename

    def get_length(self, audio_file):
        with audioread.audio_open(audio_file) as f:
            # placeholder print statement, replace with call to display to gui
            return round(f.duration, 2)

    def get_rd60_display(self, freq_range):
        data_in_db = frequency_check(freq_range)

        fig1, ax1 = plt.subplots()
        ax1.plot(t, data_in_db, linewidth=1.5, color='#1EC197')
        ax1.set_title("Decibles over time")
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Power (dB)')

        # find index of max value of the frequency
        index_of_max = np.argmax(data_in_db)
        value_of_max = data_in_db[index_of_max]

        ax1.plot(t[index_of_max], data_in_db[index_of_max], 'go', color='#1E99C1')

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

        ax1.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo', color='#1E47C1')

        # slice array from a max-5dB
        value_of_max_less_25 = value_of_max - 25
        value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
        index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)

        ax1.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro', color='#461EC1')

        rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]
        rt60 = 3 * rt20

        # placeholder print statement, replace with call to display to gui
        print(f'The RT60 reverb time at freq {int(target_frequency)}Hz is {round(abs(rt60), 2)} seconds')

        ax1.grid()
        return fig1, round(abs(rt60), 2)

    def plot_waveform(self, root, file_path):
        # Open the .wav file
        print(file_path)
        with wave.open(file_path, 'rb') as wav_file:
            # Read audio data
            sample_rate, signal = wavfile.read(file_path)

            # Create a Matplotlib figure
            fig = Figure(figsize=(4.8, 2), dpi=100)
            ax = fig.add_subplot(111)

            # Plot the waveform
            time = np.arange(0, len(signal)) / sample_rate
            ax.plot(time, signal, color='blue')
            ax.set_title('Waveform of {}'.format(file_path))
            ax.set_xlabel('Time (seconds)')
            ax.set_ylabel('Amplitude')
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas_widget = canvas.get_tk_widget()
            return canvas_widget
    def get_resonant_frequency(self):
        pass
