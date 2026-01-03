Python DSP FIR Filtering

Project Overview
This project demonstrates digital signal processing (DSP) techniques using Python, focusing on the design and application of high-order FIR bandpass filters. The implementation uses SciPy to isolate specific frequency components from a sampled signal and visualize the results in the time domain.

The project loads signal data from a MATLAB `.mat` file, applies zero-phase FIR filtering, and compares unfiltered and filtered signals.

Objectives
Design FIR bandpass filters using the window method
Isolate specific frequency bands from a signal
Apply zero-phase filtering using `filtfilt`
Visualize filtered and unfiltered signals in the time domain
Demonstrate practical DSP concepts using Python

Key Concepts Used
FIR (Finite Impulse Response) Filters  
Bandpass Filter Design  
Window Method (`firwin`)  
Zero-Phase Filtering (`filtfilt`)  
Signal Normalization  
Time-Domain Signal Visualization  

Technologies & Libraries
Python  
NumPy  
SciPy  
Matplotlib  
MATLAB `.mat` file support


Input Signal
Sampling Frequency: **120 kHz**
Signal loaded from a MATLAB `.mat` file
Signal is scaled before processing

Filtering Details
Two FIR bandpass filters are designed:

| Filter | Center Frequency | Bandwidth |
|------|-----------------|-----------|
| Filter 1 | 60 kHz | ±10 kHz |
| Filter 2 | 100 kHz | ±10 kHz |

Filter Order: 501
Filtering Method: Zero-phase (forward-backward filtering)

Output Visualization
The script generates plots for the first 10 seconds of the signal:
1. Original (unfiltered) signal  
2. Filtered signal around 60 kHz
3. Filtered signal around 100 kHz

These plots clearly show the effect of frequency-selective filtering.

How to Run
1. Clone the repository:
```bash
git clone https://github.com/your-username/python-dsp-fir-filtering.git
