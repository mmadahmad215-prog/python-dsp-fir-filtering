import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, filtfilt

# Sampling frequency
fs = 120000  # Sampling frequency in Hz (120 kHz)

# Load the data
mat_data = sio.loadmat('C:\\Users\\Amadd\\Desktop\\DSP Theory\\ecgsig.mat')  # Load the data
y = mat_data['val'][0] / 2000  # Scale the data and select the first row if it's a 2D array

# Define the frequency ranges for the bandpass filters
f_center1 = 60e3  # Center frequency in Hz for the first filter (60 kHz)
f_center2 = 100e3  # Center frequency in Hz for the second filter (100 kHz)
bw = 10e3  # Bandwidth in Hz

# Normalize the frequencies
f_low1 = (f_center1 - bw) / fs  # Lower cutoff frequency for the first filter
f_high1 = (f_center1 + bw) / fs  # Upper cutoff frequency for the first filter
f_low2 = (f_center2 - bw) / fs  # Lower cutoff frequency for the second filter
f_high2 = (f_center2 + bw) / fs  # Upper cutoff frequency for the second filter

# Design FIR bandpass filters using firwin with higher order
filter_order = 501  # Increased filter order
filter1 = firwin(filter_order, [f_low1, f_high1], pass_zero=False)
filter2 = firwin(filter_order, [f_low2, f_high2], pass_zero=False)

# Apply the filters to the signal using filtfilt
filtered_signal1 = filtfilt(filter1, 1, y)
filtered_signal2 = filtfilt(filter2, 1, y)

# Calculate the maximum number of samples we can plot for 10 seconds
max_samples_10s = min(int(10 * fs), len(y))

# Create a time vector for plotting (10 seconds)
time_vector_10s = np.arange(max_samples_10s) / fs

# Plot the unfiltered signal (first 10 seconds)
plt.subplot(3, 1, 1)
plt.plot(time_vector_10s, y[:max_samples_10s])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Unfiltered Signal (First 10 Seconds)')

# Plot the filtered signals with increased clarity (first 10 seconds)
plt.subplot(3, 1, 2)
plt.plot(time_vector_10s, filtered_signal1[:max_samples_10s], 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Filtered Signals - 60 kHz ± 10 kHz (First 10 Seconds)')

plt.subplot(3, 1, 3)
plt.plot(time_vector_10s, filtered_signal2[:max_samples_10s], 'g')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Filtered Signals - 100 kHz ± 10 kHz (First 10 Seconds)')

plt.tight_layout()
plt.show()


