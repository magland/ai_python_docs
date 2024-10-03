To create continuous spectral density estimates using the `pynapple` library, follow these steps to compute power spectral densities (PSD) across different epochs for thorough analysis of signal characteristics. This guide assumes you have time series data such as Local Field Potentials (LFP) or other types of continuous signals.

### Prerequisites

1. Ensure you have `pynapple` installed along with its dependencies such as `numpy`, `matplotlib`, and `seaborn`.
2. Import the necessary libraries:
   ```python
   import numpy as np
   import pynapple as nap
   import matplotlib.pyplot as plt
   ```

### Step-by-step Guide

1. **Load Your Data**
   - Load your time series data. This could be from a file or generated within your script.
   - For instance, load an NWB file or any compatible format:
     ```python
     data = nap.load_file('path_to_your_data.nwb')
     signal = data['eeg']  # Extract EEG or appropriate signal
     epochs = data['epochs']  # Load epochs, e.g., wake and sleep
     ```

2. **Define Epochs for Analysis**
   - Determine the epochs over which you want to analyze the spectral properties. 
   - You might have specific epochs like `wake`, `rest`, `run`, etc.
   - Use these epochs to restrict your analysis:
     ```python
     wake_ep = epochs['wake']
     rest_ep = epochs['rest']
     ```

3. **Compute PSD for Each Epoch**
   - Use `nap.compute_power_spectral_density` for large single epoch analysis.
   - Use `nap.compute_mean_power_spectral_density` for multiple epochs of equal length to avoid boundary artifacts.
   - Example of PSD calculation for a single large epoch:
     ```python
     fs = 1000  # Sampling frequency
     psd_wake = nap.compute_power_spectral_density(signal, fs=fs, ep=wake_ep, norm=True)
     psd_rest = nap.compute_power_spectral_density(signal, fs=fs, ep=rest_ep, norm=True)
     ```

4. **Visualize the Results**
   - Visualize the PSDs using Matplotlib.
   - Plot the PSD for each epoch to compare their spectral characteristics:
     ```python
     plt.figure(figsize=(10, 6))
     plt.plot(psd_wake.index, np.abs(psd_wake), label='Wake')
     plt.plot(psd_rest.index, np.abs(psd_rest), label='Rest')
     plt.xlabel('Frequency (Hz)')
     plt.ylabel('Amplitude')
     plt.legend()
     plt.title('Power Spectral Density')
     plt.show()
     ```

5. **Analyze the Spectral Characteristics**
   - Use PSD plots to examine dominant frequencies and their strengths across epochs.
   - Look for characteristic patterns such as theta waves during run epochs or ripple events during rest.

Using `pynapple`, you can efficiently compute and analyze continuous spectral density estimates across different epochs, providing insights into the spectral characteristics of your signals under varying conditions.