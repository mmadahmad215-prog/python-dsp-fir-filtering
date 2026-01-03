import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Define the sampling frequency of the ECG data
fs = 500  # Assuming 500 Hz for 5000 samples in 10 seconds

# Load the ECG data
mat_data = sio.loadmat('C:\\Users\\Amadd\\Desktop\\DSP Theory\\ecgsig.mat')
y = mat_data['val'][0] / 2000  # Scale the data

# Extract a 10-second segment (5000 samples)
dataLength = len(y)
if dataLength >= 5000:
    y_segment = y[:5000]
else:
    raise ValueError('The loaded data does not contain enough samples.')

# Generate Baseline Wander Noise (Low-frequency sinusoid)
t = np.arange(5000) / fs
baseline_wander = 0.5 * np.sin(2 * np.pi * 0.2 * t)  # 0.2 Hz sinusoidal noise

# Generate Power Line Noise (50 Hz sinusoid)
power_line_noise = 0.1 * np.sin(2 * np.pi * 50 * t)  # 50 Hz sinusoidal noise

# Add noises to the original ECG signal
noisy_ecg = y_segment + baseline_wander + power_line_noise

# Define the zeros and poles
zeros = [1, np.exp(0.2 * np.pi * 1j), np.exp(-0.2 * np.pi * 1j), 0.02 * np.pi * 1j, -0.02 * np.pi * 1j, -1]
poles = [0, 0, 0, 0, 0, 0]

# Calculate the transfer function coefficients
b = np.poly(zeros)
a = np.poly(poles)

# Apply the designed filter to the noisy ECG data
filtered_ecg = lfilter(b, a, noisy_ecg)

# Plot the original, noisy, and filtered signals
plt.figure()

plt.subplot(3, 1, 1)
plt.plot(np.arange(5000) / fs, y_segment)
plt.title('Original ECG Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(np.arange(5000) / fs, noisy_ecg)
plt.title('Noisy ECG Signal (with Baseline Wander and Power Line Noise)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(np.arange(5000) / fs, filtered_ecg)
plt.title('Filtered ECG Signal (after applying designed filter)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
