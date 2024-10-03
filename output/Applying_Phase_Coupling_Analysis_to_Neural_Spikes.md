# How-to Guide: Applying Phase Coupling Analysis to Neural Spikes

This guide outlines the steps for analyzing the relationship between neural spikes and oscillatory phase using Pynapple. The process involves band-pass filtering the neural signal, calculating the phase using Hilbert transforms, and then examining the phase preferences of spikes.

## Prerequisites

Ensure you have the following libraries installed:
```bash
pip install pynapple numpy matplotlib seaborn scipy
```

## Step-by-Step Process

### 1. **Download and Load the Data**
Begin by downloading your dataset, which typically contains both neural spikes (e.g., from a cortex or hippocampus) and an oscillatory signal (e.g., Local Field Potential, LFP).

```python
import pynapple as nap
import requests

# Download the data
path = "your_data_file.nwb"
if path not in os.listdir("."):
    r = requests.get(f"https://osf.io/your_download_link/download", stream=True)
    with open(path, 'wb') as f:
        f.write(r.content)

# Load the data
data = nap.load_file(path)
```

### 2. **Extract the Neural Spikes and Oscillatory Signal**
Identify the neural spike data and the oscillatory signal you want to analyze (e.g., LFP).

```python
# Extract neural spikes (assume it's in the 'units' key)
spikes = data["units"]

# Extract the oscillatory signal (assume it's in the 'eeg' key)
oscillatory_signal = data["eeg"]
```

### 3. **Filter the Oscillatory Signal**
Apply a band-pass filter to isolate the frequency range of interest (e.g., theta band: 6-10 Hz). 

```python
# Define sampling frequency
sampling_frequency = 1250  # Example frequency

# Band-pass filter the oscillatory signal
filtered_signal = nap.apply_bandpass_filter(oscillatory_signal, cutoff=(6, 10), fs=sampling_frequency)
```

### 4. **Compute the Phase Using Hilbert Transform**
Use the Hilbert transform to obtain the instantaneous phase of the filtered oscillatory signal.

```python
from scipy import signal

# Compute the Hilbert transform to extract the phase
instantaneous_phase = np.angle(signal.hilbert(filtered_signal))
```

### 5. **Compute Phase Preferences for Each Spike**
Use the phase values to analyze how spikes relate to the oscillatory phase. For this, apply a tuning curve analysis on the phase values.

```python
# Compute tuning curves to relate spike times to phase values
phase_modulation = nap.compute_1d_tuning_curves(group=spikes, feature=instantaneous_phase, nb_bins=61, minmax=(-np.pi, np.pi))
```

### 6. **Visualize the Phase Preferences**
Plot the tuning curves to visualize the relationship between spike timings and the oscillatory phase. This will help in identifying phase preferences.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
for i in range(len(phase_modulation.columns)):
    plt.plot(phase_modulation[i], label=f"Neuron {i + 1}")
plt.xlabel("Phase (rad)")
plt.ylabel("Firing Rate (Hz)")
plt.title("Phase Tuning Curves for Neural Spikes")
plt.legend()
plt.show()
```

### 7. **Interpret the Results**
Examine the plots to identify phase locking or preferences among neural spikes. A peak in the firing rate at a specific phase indicates that the spikes are preferentially occurring at that phase of the oscillation.

## Conclusion
By following this guide, you should have successfully applied phase coupling analysis to your neural spikes using filtering and Hilbert transforms. Adjust the filtering parameters based on your specific research needs and the oscillatory frequencies of interest.

For further details on specific functions and their parameters, consult the Pynapple documentation.