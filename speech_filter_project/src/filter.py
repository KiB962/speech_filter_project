import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, data = wavfile.read('speech_input.wav') #returns the sample rate and a numpy array of the amplitude values of the audio file
lowcut = 300 # Set the low cutoff frequency cutting off deep base 
highcut = 3400 # Set the high cutoff frequency cutting off high frequencies
order = 6# Set the order of the filter

sos = signal.butter(order, [lowcut, highcut], btype="bandpass", fs=fs, output='sos') # Create a second-order section filter

if data.dtype == np.int16:
    data = data.astype(np.float32) / np.max(np.abs(data))

filtered_data = signal.sosfiltfilt(sos, data)

# Normalize the output to int16 range again for saving
filtered_data = filtered_data / np.max(np.abs(filtered_data))  # scale to -1.0 to 1.0
filtered_int16 = np.int16(filtered_data * 32767)  # convert to int16

# Save the filtered audio to a new WAV file
wavfile.write('filtered_output.wav', fs, filtered_int16)

# Optional: Plot original and filtered waveforms for a quick check
import matplotlib.pyplot as plt

t = np.linspace(0, len(data) / fs, num=len(data))

# 1) Original waveform
plt.figure(figsize=(10, 4))
plt.plot(t, data, label="Original")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original Audio")
plt.grid(True)
plt.tight_layout()
plt.savefig('original_audio.png')
plt.close()

# 2) Filtered waveform
plt.figure(figsize=(10, 4))
plt.plot(t, filtered_data, label="Filtered", color='orange')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Filtered Audio")
plt.grid(True)
plt.tight_layout()
plt.savefig('filtered_audio.png')
plt.close()

# 3) Overlapping plot
plt.figure(figsize=(10, 4))
plt.plot(t, data, label="Original", alpha=0.5)
plt.plot(t, filtered_data, label="Filtered", alpha=0.8, color='orange')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original vs Filtered Audio")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('original_vs_filtered.png')
plt.close()

print("Saved three plots: 'original_audio.png', 'filtered_audio.png', and 'original_vs_filtered.png'.")