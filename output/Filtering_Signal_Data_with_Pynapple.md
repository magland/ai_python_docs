# How-to Guide: Filtering Signal Data with Pynapple

In this tutorial, you will learn how to apply various filters (bandpass, lowpass, highpass, bandstop) to analyze signal frequencies using the Pynapple library.

## Prerequisites

Make sure you have Pynapple installed. You can install it along with the required libraries using the following command:
```bash
pip install matplotlib requests tqdm seaborn
```

## Step-by-Step Guide

### 1. Import Necessary Libraries

Start by importing the required libraries:
```python
import numpy as np
import matplotlib.pyplot as plt
import pynapple as nap
```

### 2. Generate a Sample Signal

Create a sample signal with multiple frequencies, which will demonstrate the filtering capabilities of Pynapple.
```python
fs = 1000  # Sampling frequency
t = np.linspace(0, 2, fs * 2)
f2 = np.cos(t * 2 * np.pi * 2)    # 2 Hz signal
f10 = np.cos(t * 2 * np.pi * 10)  # 10 Hz signal
f50 = np.cos(t * 2 * np.pi * 50)  # 50 Hz signal

# Combine to form the signal with noise
signal = f2 + f10 + f50 + np.random.normal(0, 0.5, len(t))
```

### 3. Plot the Original Signal

Visualize the original signal to understand what it looks like before applying any filters.
```python
plt.figure(figsize=(15, 5))
plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.title("Original Signal")
plt.show()
```

### 4. Apply Different Filters

You can apply different types of filters as demonstrated below:

#### Bandpass Filter
To filter the signal between two frequency bands (e.g., 8 to 12 Hz):
```python
bandpass_filtered_signal = nap.apply_bandpass_filter(signal, cutoff=(8, 12), fs=fs, mode='butter')
```

#### Lowpass Filter
To filter out high frequencies and keep the low frequencies below a specified cut-off (e.g., below 10 Hz):
```python
lowpass_filtered_signal = nap.apply_lowpass_filter(signal, cutoff=10, fs=fs, mode='butter')
```

#### Highpass Filter
To filter out low frequencies and keep the high frequencies above a specified cut-off (e.g., above 10 Hz):
```python
highpass_filtered_signal = nap.apply_highpass_filter(signal, cutoff=10, fs=fs, mode='butter')
```

#### Bandstop Filter
To remove a specific frequency band (e.g., around 50 Hz):
```python
bandstop_filtered_signal = nap.apply_bandstop_filter(signal, cutoff=(45, 55), fs=fs, mode='butter')
```

### 5. Plot the Filtered Signals

Visualize the filtered signals to see the effects of the different filters.
```python
plt.figure(figsize=(15, 10))

# Bandpass Filtered Signal
plt.subplot(4, 1, 1)
plt.plot(t, bandpass_filtered_signal)
plt.title("Bandpass Filtered Signal (8-12 Hz)")
plt.xlabel("Time (s)")

# Lowpass Filtered Signal
plt.subplot(4, 1, 2)
plt.plot(t, lowpass_filtered_signal)
plt.title("Lowpass Filtered Signal (cutoff 10 Hz)")
plt.xlabel("Time (s)")

# Highpass Filtered Signal
plt.subplot(4, 1, 3)
plt.plot(t, highpass_filtered_signal)
plt.title("Highpass Filtered Signal (cutoff 10 Hz)")
plt.xlabel("Time (s)")

# Bandstop Filtered Signal
plt.subplot(4, 1, 4)
plt.plot(t, bandstop_filtered_signal)
plt.title("Bandstop Filtered Signal (45-55 Hz removed)")
plt.xlabel("Time (s)")

plt.tight_layout()
plt.show()
```

### Conclusion

You have successfully learned how to apply various filters to signal data using Pynapple. By filtering your signals effectively, you can analyze specific frequency components and enhance your understanding of the underlying data.