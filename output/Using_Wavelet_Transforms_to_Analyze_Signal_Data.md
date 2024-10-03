# Using Wavelet Transforms to Analyze Signal Data

This guide provides a tutorial on performing continuous wavelet transforms to capture changes in signal data over time using the `pynapple` library. We will explore how to generate a wavelet transform using `pynapple`, visualize the results, and interpret the outcomes. This can be particularly useful when analyzing neural signals, which often change and develop over time.

## Step-by-Step Tutorial

### 1. Install Required Libraries

Ensure you have the required libraries installed. You will need `pynapple`, `matplotlib`, `numpy`, and `seaborn`. You can install them using pip:

```sh
pip install pynapple matplotlib numpy seaborn
```

### 2. Import Libraries

Import the necessary libraries in your script or Jupyter notebook:

```python
import pynapple as nap
import matplotlib.pyplot as plt
import numpy as np
import seaborn
```

### 3. Load or Generate Data

You can load your signal data. For this tutorial, let's generate a dummy signal with a 2Hz component and an increasing frequency component:

```python
Fs = 2000  # Sampling frequency
t = np.linspace(0, 5, Fs * 5)

# Generate components
two_hz_phase = t * 2 * np.pi * 2
two_hz_component = np.sin(two_hz_phase)
increasing_freq_component = np.sin(t * (5 + t) * np.pi * 2)

# Combine components with noise
signal_data = nap.Tsd(
    d=two_hz_component + increasing_freq_component + np.random.normal(0, 0.1, len(t)),
    t=t,
)
```

### 4. Generate Morlet Wavelet Filter Bank

Define the frequencies you want for the wavelet transform and generate the filter bank:

```python
freqs = np.linspace(1, 25, num=25)
filter_bank = nap.generate_morlet_filterbank(freqs, Fs, gaussian_width=1.5, window_length=1.0)
```

### 5. Perform Continuous Wavelet Transform

Use the `compute_wavelet_transform` function to perform the wavelet transform on the signal data:

```python
mwt = nap.compute_wavelet_transform(signal_data, fs=Fs, freqs=freqs)
```

### 6. Visualize the Results

Plot the wavelet transform to visualize how the signal's frequency components vary over time:

```python
def plot_timefrequency(freqs, powers, ax=None):
    im = ax.imshow(np.abs(powers), aspect="auto")
    ax.invert_yaxis()
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Frequency (Hz)")
    ax.get_xaxis().set_visible(False)
    ax.set(yticks=np.arange(len(freqs))[::2], yticklabels=freqs[::2])
    ax.grid(False)
    return im

# Create plot
fig, ax = plt.subplots(1, constrained_layout=True, figsize=(10, 6))
plot_timefrequency(freqs, np.transpose(mwt[:, :].values), ax=ax)
plt.title("Wavelet Transform Scalogram")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.show()
```

### 7. Interpret the Wavelet Transform

The wavelet transform provides a time-frequency analysis of the signal. You can observe changes in frequency content over time. Notice prominent frequencies and their duration.

### 8. Further Analysis

You may extract specific components, such as low or high-frequency oscillations, and reconstruct them from the wavelet transform. Analyze the modulation of specific frequencies over time or compute the signal's phase and amplitude at these frequencies.

### Conclusion

Wavelet transforms are powerful for analyzing non-stationary signals and capturing temporal changes in frequency content. This tutorial demonstrates using `pynapple` to perform continuous wavelet transforms, which are particularly useful for neuroscientific data and other bio-signals.

Feel free to explore additional parameters and customize the analysis to fit your specific needs!