# How-to Guide: Using Wavelet Transforms to Analyze Signal Data with pynapple

This tutorial will guide you through the process of performing continuous wavelet transforms using pynapple to capture changes in signal data over time. We will be working with the functionalities provided within the pynapple library to analyze Local Field Potential (LFP) data.

## Prerequisites

Before you start, ensure you have the necessary libraries installed. You can install pynapple along with other required libraries using pip:

```bash
pip install matplotlib requests tqdm seaborn pynapple
```

## Step-by-Step Instructions

### 1. Import Required Libraries

Start by importing the necessary libraries for your analysis.

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pynapple as nap
import requests
import tqdm
import math
```

### 2. Download Example Data

For demonstration purposes, download a sample dataset that contains LFP data. This data can be obtained from a provided URL.

```python
path = "example_data.nwb"  # Replace with actual data path
if path not in os.listdir("."):
    r = requests.get(f"https://osf.io/2dfvp/download", stream=True)
    block_size = 1024 * 1024
    with open(path, "wb") as f:
        for data in tqdm.tqdm(r.iter_content(block_size), unit="MB", unit_scale=True,
                               total=math.ceil(int(r.headers.get("content-length", 0)) // block_size)):
            f.write(data)
```

### 3. Load the Data

Load the data into your script using pynapple. This step allows you to access different components of the data such as the LFP signals.

```python
data = nap.load_file(path)  # Load the NWB file
eeg = data["eeg"]  # Extract the LFP data
```

### 4. Define the Time Interval for Analysis

Select a specific time interval of interest from the loaded data. This interval will be used for the wavelet transformation.

```python
run_interval = nap.IntervalSet(start_time, end_time)  # define your interval of interest
eeg_example = eeg.restrict(run_interval)[:, 0]  # Restrict LFP data to the selected interval
```

### 5. Perform the Wavelet Transform

Define the frequency range for your wavelet transform. Then compute the wavelet transform on the LFP data.

```python
frequencies = np.geomspace(3, 250, 100)  # Define the frequency range for analysis
mwt = nap.compute_wavelet_transform(eeg_example, fs=1250, freqs=frequencies)  # Compute wavelet transform
```

### 6. Visualize the Wavelet Decomposition

After performing the wavelet transform, visualize the results using a spectrogram.

```python
# Define plotting function
def plot_timefrequency(freqs, powers, ax=None):
    im = ax.imshow(np.abs(powers), aspect="auto")
    ax.invert_yaxis()
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Frequency (Hz)")
    ax.get_xaxis().set_visible(False)
    ax.set(yticks=np.arange(len(freqs))[::2], yticklabels=np.rint(freqs[::2]))
    ax.grid(False)
    return im

# Creating the plot
fig, ax = plt.subplots(figsize=(10, 6))
plot_timefrequency(frequencies, np.transpose(np.abs(mwt)), ax=ax)
plt.title("Wavelet Decomposition")
plt.colorbar(label='Amplitude')
plt.show()
```

### 7. Analyzing and Interpreting Results

The resulting plot will help you analyze how different frequency components change over time. Look for patterns or oscillations corresponding to specific frequencies that may indicate states of interest (e.g., theta rhythm during REM sleep).

### Conclusion

You have successfully performed a continuous wavelet transform on signal data using pynapple and visualized the results. This method is useful for understanding how signals evolve over time and can be applied to various types of data in neuroscience and other fields.

For further exploration and specific details, refer to the [pynapple documentation](https://pynapple-org.github.io/pynapple/).