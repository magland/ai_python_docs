Certainly! Below is a step-by-step guide on how to apply various filters (bandpass, lowpass, highpass, bandstop) using the pynapple package to analyze signal frequencies.

---

# How to Guide: Filtering Signal Data with Pynapple

## Introduction

This guide will walk you through applying different types of filters to your signal data using the pynapple library. Whether you want to focus on specific frequency bands or eliminate unwanted frequencies, pynapple provides robust filtering functions to effectively analyze signal frequencies.

## Step 1: Installation and Setup

First, ensure you have the pynapple library installed. You can install it via pip if you haven't already:

```bash
pip install pynapple
```

Additionally, you'll require matplotlib and numpy for plotting and numerical operations:

```bash
pip install matplotlib numpy
```

## Step 2: Import Required Libraries

Begin by importing the necessary libraries:

```python
import pynapple as nap
import numpy as np
import matplotlib.pyplot as plt
```

## Step 3: Generating or Loading Signal Data

You can either generate synthetic signal data or load your real data. Below, we generate a synthetic signal composed of multiple frequencies:

```python
fs = 1000  # Sampling frequency
t = np.linspace(0, 2, fs * 2)  # Time vector
# Generate a signal with 2 Hz, 10 Hz, and 50 Hz components
signal_data = np.cos(t * 2 * np.pi * 2) + np.cos(t * 2 * np.pi * 10) + np.cos(t * 2 * np.pi * 50)
```

## Step 4: Apply Filters

### Bandpass Filter

To isolate a frequency band (e.g., 8-12 Hz), use:

```python
filtered_signal_bandpass = nap.apply_bandpass_filter(signal_data, (8, 12), fs, mode='butter')
```

### Lowpass Filter

To allow frequencies below a certain threshold (e.g., < 10 Hz) to pass:

```python
filtered_signal_lowpass = nap.apply_lowpass_filter(signal_data, cutoff=10, fs=fs, mode='butter')
```

### Highpass Filter

To allow frequencies above a certain threshold (e.g., > 10 Hz) to pass:

```python
filtered_signal_highpass = nap.apply_highpass_filter(signal_data, cutoff=10, fs=fs, mode='butter')
```

### Bandstop Filter

To remove specific frequency bands (e.g., 45-55 Hz):

```python
filtered_signal_bandstop = nap.apply_bandstop_filter(signal_data, cutoff=(45, 55), fs=fs, mode='butter')
```

## Step 5: Plotting the Filtered Signals

Visualize the effects of filtering by plotting the original and filtered signals:

```python
plt.figure(figsize=(10, 8))

# Plot original signal
plt.subplot(511)
plt.plot(t, signal_data)
plt.title("Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot Bandpass filtered signal
plt.subplot(512)
plt.plot(t, filtered_signal_bandpass)
plt.title("Bandpass Filtered Signal (8-12 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot Lowpass filtered signal
plt.subplot(513)
plt.plot(t, filtered_signal_lowpass)
plt.title("Lowpass Filtered Signal (< 10 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot Highpass filtered signal
plt.subplot(514)
plt.plot(t, filtered_signal_highpass)
plt.title("Highpass Filtered Signal (> 10 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot Bandstop filtered signal
plt.subplot(515)
plt.plot(t, filtered_signal_bandstop)
plt.title("Bandstop Filtered Signal (45-55 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Adjust layout for better readability
plt.tight_layout()
plt.show()
```

## Conclusion

By following these steps, you can apply various filters to your signal data using pynapple and analyze specific frequency components. The example provided demonstrates each filter type and their effects on a synthetic signal.

Feel free to experiment with different frequency cutoffs and modes to see how they influence your data!

---

This guide provides a comprehensive overview of filtering signal data using pynapple, highlighting its flexibility and ease of use for frequency analysis.