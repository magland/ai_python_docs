# Wavelet Parametrization for Time-Frequency Analysis Guide

## Overview
This guide explains how to use wavelet analysis tools in the pynapple package, emphasizing the impact of various wavelet parameters on the temporal resolution and reconstruction fidelity of time-frequency analyses.

## Prerequisites
Ensure you have the pynapple package and its dependencies installed. You can install it along with the required libraries as follows:
```bash
pip install matplotlib seaborn requests tqdm
```

## Step-by-Step Instructions

### 1. Import Necessary Libraries
Begin by importing all the necessary libraries:
```python
import numpy as np
import pynapple as nap
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import os
import tqdm
```

### 2. Download Sample Data
For the purpose of this analysis, download an example dataset that contains LFP (local field potential) data. You can replace the URL with a valid data source if needed:
```python
path = "example_data.nwb"
if path not in os.listdir("."):
  r = requests.get("https://example.com/example_data.nwb", stream=True)
  block_size = 1024 * 1024
  with open(path, 'wb') as f:
    for data in tqdm.tqdm(r.iter_content(block_size), unit='MB', unit_scale=True,
                           total=math.ceil(int(r.headers.get('content-length', 0)) // block_size)):
      f.write(data)
```

### 3. Load the Data
Load the downloaded NWB file to import your LFP data:
```python
data = nap.load_file(path)
eeg = data["eeg"]  # Replace 'eeg' with the appropriate key for your LFP data
```

### 4. Define Frequency Set for Wavelet Transformation
To explore how parameters affect results, set a range of frequencies for the wavelet decomposition:
```python
freqs = np.linspace(1, 250, num=100)  # Adjust frequency range as appropriate
```

### 5. Compute Wavelet Transform
Perform the wavelet transform using the defined frequency set. Adjust the `gaussian_width` and `window_length` parameters to observe their effects:
```python
# Example with specific parameters
mwt = nap.compute_wavelet_transform(eeg, fs=1250, freqs=freqs, gaussian_width=1.5, window_length=1.0)
```

### 6. Visualize the Results
Plot the wavelet decomposition to visualize how the frequencies evolve over time:
```python
plt.figure(figsize=(10, 6))
plt.imshow(np.abs(mwt), aspect='auto', extent=[eeg.t.min(), eeg.t.max(), freqs.min(), freqs.max()])
plt.title("Wavelet Decomposition")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.colorbar(label="Magnitude")
plt.show()
```

### 7. Experiment with Different Parameters
Change the `gaussian_width` and `window_length` parameters and observe how they affect the wavelet transform:
- Decreasing `gaussian_width` generally increases the time resolution.
- Increasing `window_length` may offer better frequency resolution.
```python
# Example of changing parameters
mwt_new = nap.compute_wavelet_transform(eeg, fs=1250, freqs=freqs, gaussian_width=3.0, window_length=2.0)
```
Visualize the new results similarly to step 6.

### 8. Evaluate Reconstruction Fidelity
To assess how well your reconstruction matches the original signal, sum the wavelet results and compare against the original LFP signal:
```python
reconstructed_signal = np.sum(mwt, axis=1)
plt.figure()
plt.plot(eeg, label='Original Signal')
plt.plot(reconstructed_signal, label='Reconstructed Signal', alpha=0.7)
plt.legend()
plt.title("Signal Reconstruction Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
```

### 9. Analyze Transition Bands
Inspect how the parameter settings affect transition bandwidths and the resulting frequency response. For example, compute and plot the frequency response for different wavelets.

### Conclusion
By varying the wavelet parameters, you can significantly impact the analysis resolution and reconstruction fidelity in temporal analyses. Learning how to optimally set these parameters is crucial for accurately interpreting wavelet transform results in your research.

### References
Consult the pynapple documentation for further technical details and advanced usage: [Pynapple Documentation](https://pynapple-org.github.io/pynapple/)