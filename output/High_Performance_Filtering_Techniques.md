# High Performance Filtering Techniques: Comparing Butterworth and Windowed-Sinc Filters

In this guide, we will compare the performance and precision of two common filtering techniques: the Butterworth filter and the Windowed-sinc filter. These techniques are vital for manipulating frequency characteristics in large datasets.

## Overview

This guide will demonstrate:

1. How to generate a test signal.
2. How to apply Butterworth and Windowed-sinc filters to the signal.
3. How to benchmark the performance of each filter type.
4. How to visualize and interpret the output.

## Step-by-Step Instructions

### 1. Import Necessary Libraries

Make sure to include the required libraries before starting the filtering.

```python
import numpy as np
import pynapple as nap
import matplotlib.pyplot as plt
from time import perf_counter
```

### 2. Generate Sample Data

Create a sample signal with known frequency components. This allows us to visualize how well each filtering method retains or removes certain frequencies.

```python
fs = 1000  # Sampling frequency
t = np.linspace(0, 2, fs * 2)
f2 = np.cos(t * 2 * np.pi * 2)  # 2 Hz component
f10 = np.cos(t * 2 * np.pi * 10)  # 10 Hz component
f50 = np.cos(t * 2 * np.pi * 50)  # 50 Hz component

# Combine components to create a signal
sig = f2 + f10 + f50 + np.random.normal(0, 0.5, len(t))
```

### 3. Apply Filters

We will apply both Butterworth and Windowed-sinc filters to the same signal, thereby comparing their outputs.

```python
# Bandpass filter using Butterworth
filtered_butter = nap.apply_bandpass_filter(sig, (8, 12), fs, mode='butter')

# Bandpass filter using Windowed-sinc
filtered_sinc = nap.apply_bandpass_filter(sig, (8, 12), fs, mode='sinc', transition_bandwidth=0.003)
```

### 4. Plotting Comparison of Filters

Visualize the original and filtered signals to inspect the performance:

```python
plt.figure(figsize=(15, 5))
plt.subplot(211)
plt.plot(t, sig, label="Original Signal")
plt.plot(t, filtered_butter, label="Butterworth Filtered", linewidth=2)
plt.title("Butterworth Filter")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(212)
plt.plot(t, sig, label="Original Signal")
plt.plot(t, filtered_sinc, label="Windowed-Sinc Filtered", linestyle='--', linewidth=2)
plt.title("Windowed-Sinc Filter")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
```

### 5. Benchmarking Performance

To evaluate the performance of both filters, you can define functions that measure the execution time for a number of trials.

```python
def get_mean_perf(signal, mode, n=10):
    tmp = np.zeros(n)
    for i in range(n):
        t1 = perf_counter()
        _ = nap.apply_lowpass_filter(signal, 0.25 * signal.rate, mode=mode)
        t2 = perf_counter()
        tmp[i] = t2 - t1
    return [np.mean(tmp), np.std(tmp)]

# Performance benchmarking for both filters
times_butter = get_mean_perf(sig, mode='butter')
times_sinc = get_mean_perf(sig, mode='sinc')

print(f"Butterworth Average Time: {times_butter[0]} ± {times_butter[1]}")
print(f"Windowed-Sinc Average Time: {times_sinc[0]} ± {times_sinc[1]}")
```

### Conclusion

Through this guide, you've learned how to implement high-performance filtering techniques using Butterworth and Windowed-sinc filters. By testing frequency retention, precision, and performance on large datasets, you can make informed decisions about which filtering approach to use in your analyses.