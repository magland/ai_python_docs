# High Performance Filtering Techniques: Comparing Butterworth and Windowed-Sinc Filters

In this guide, we'll explore how to use Pynapple to compare Butterworth and Windowed-sinc filters in terms of performance and precision, especially when applied to large datasets. This is critical when working with time series data where efficient and precise filtering is required.

## Overview

The Pynapple filtering module provides two main methods for frequency manipulation:
- **Butterworth Filter**: A type of recursive filter known for its smooth frequency response.
- **Windowed-Sinc Filter**: A non-recursive filter using a windowed-sinc function, offering precise control over the transition bandwidth.

## Steps to Compare Filters

### 1. Preparation

Before you begin, ensure you have Pynapple and other necessary libraries installed. You can do this via:

```bash
pip install pynapple matplotlib numpy
```

### 2. Generate Sample Data

You can start by generating a multi-frequency signal to test the filtering methods:

```python
import numpy as np
import pynapple as nap
import matplotlib.pyplot as plt

fs = 1000  # Sampling frequency
t = np.linspace(0, 2, fs * 2)
f2 = np.cos(t * 2 * np.pi * 2)
f10 = np.cos(t * 2 * np.pi * 10)
f50 = np.cos(t * 2 * np.pi * 50)
sig = nap.Tsd(t=t, d=f2 + f10 + f50 + np.random.normal(0, 0.5, len(t)))
```

### 3. Apply Filters

#### Butterworth Filter

Apply a Butterworth filter with a defined passband:

```python
sig_butter = nap.apply_bandpass_filter(sig, (8, 12), fs, mode='butter')
```

#### Windowed-Sinc Filter

Similarly, apply a Windowed-sinc filter:

```python
sig_sinc = nap.apply_bandpass_filter(sig, (8, 12), fs, mode='sinc', transition_bandwidth=0.003)
```

### 4. Plot Results

Visualize the results to compare the precision of both filters:

```python
fig = plt.figure(figsize=(10, 5))
plt.subplot(211)
plt.plot(t, f10, '-', color='gray', label="10 Hz component")
plt.xlim(0, 1)
plt.legend()
plt.subplot(212)
plt.plot(sig_butter, label="Butterworth")
plt.plot(sig_sinc, '--', label="Windowed-sinc")
plt.legend()
plt.xlabel("Time (s)")
plt.xlim(0, 1)
plt.show()
```

### 5. Performance Assessment

To assess the performance, especially for large datasets, you can profile the time taken by each filtering method:

#### Define a Function for Benchmarking

```python
from time import perf_counter

def get_mean_perf(tsd, mode, n=10):
    times = []
    for _ in range(n):
        start = perf_counter()
        filtered = nap.apply_lowpass_filter(tsd, 0.25 * fs, mode=mode)
        end = perf_counter()
        times.append(end - start)
    return np.mean(times), np.std(times)
```

#### Run Benchmark

Test with increasing sizes of data points and report the performance:

```python
sizes = [1000, 20000, 50000, 100000]
butter_times = [get_mean_perf(nap.Tsd(t=np.linspace(0, size/fs, size), d=np.random.rand(size)), 'butter') for size in sizes]
sinc_times = [get_mean_perf(nap.Tsd(t=np.linspace(0, size/fs, size), d=np.random.rand(size)), 'sinc') for size in sizes]

print("Butterworth times:", butter_times)
print("Windowed-sinc times:", sinc_times)
```

### 6. Analyze Results

From the above benchmarks, you can analyze:
- **Precision**: Compare plots to see which filter more accurately retains the desired frequency components.
- **Performance**: Time taken for each filtering process at various data sizes to assess computational efficiency.

By following this guide, you'll be able to perform an informed comparison between the Butterworth and Windowed-sinc filters, allowing you to select the best technique based on your performance and precision requirements for large datasets.