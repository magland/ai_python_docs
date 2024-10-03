# Handling Memory Maps During Analysis

This guide provides detailed instructions on how to effectively use numpy and zarr memory maps with Pynapple for scalable data processing. Memory maps enable efficient data access and manipulation without loading the entire dataset into memory, which is especially beneficial for large datasets.

## Prerequisites
Ensure you have the following packages installed:
- numpy
- zarr
- pynapple

```bash
pip install numpy zarr pynapple
```

## Using Numpy Memory Map with Pynapple

### Step 1: Create a Numpy Memory Map

A memory map in Numpy allows you to read and write data on disk as if they were numpy arrays.

```python
import numpy as np

# Define the path to your binary file
eeg_path = "your_dataset.eeg"

# Define data characteristics
frequency = 1250  # Hz
n_channels = 16

# Calculate the number of samples
f = open(eeg_path, 'rb')
startoffile = f.seek(0, 0)
endoffile = f.seek(0, 2)
f.close()
bytes_size = 2
n_samples = int((endoffile - startoffile) / n_channels / bytes_size)

# Create a memory map
fp = np.memmap(eeg_path, dtype=np.int16, mode='r', shape=(n_samples, n_channels))
timestep = np.arange(0, n_samples) / frequency
```

### Step 2: Integrate with Pynapple

Transform the numpy memmap into a Pynapple object for further analysis.

```python
import pynapple as nap

# Create a TsdFrame in Pynapple
eeg = nap.TsdFrame(t=timestep, d=fp)

# You can now use Pynapple functions for analysis while maintaining memory efficiency
print(eeg)
```

### Step 3: Processing and Analysis

You can apply Pynapple processing functions without loading the entire dataset into memory.

```python
# Example: Restricting data to a specific epoch
ep = nap.IntervalSet(0, 10)
eeg_restricted = eeg.restrict(ep)

# Example: Applying filters or other operations
filtered_eeg = nap.apply_bandpass_filter(eeg_restricted, (10, 20), frequency)
```

## Using Zarr Memory Map with Pynapple

### Step 1: Create a Zarr Array

Zarr provides a chunked, compressed, N-dimensional array with a richer feature set compared to numpy’s basic memory map.

```python
import zarr

# Create a Zarr array
zarr_data = zarr.zeros((10000, 5), chunks=(1000, 5), dtype='i4')
timestep = np.arange(len(zarr_data))
```

### Step 2: Integrate with Pynapple

When using a Zarr array, indicate that you don't want to load the array directly into memory.

```python
# Create a TsdFrame in Pynapple without loading the full array
tsdframe = nap.TsdFrame(t=timestep, d=zarr_data, load_array=False)

# Data remains as a Zarr array
print(type(tsdframe.d))
```

### Step 3: Processing and Analysis

Continue to process your data using Pynapple, taking advantage of Zarr's efficient I/O.

```python
# Restricting data and performing calculations without full data load
ep = nap.IntervalSet(start=0, end=1000)
tsdframe_restricted = tsdframe.restrict(ep)

print(tsdframe_restricted)
```

## Conclusion

By using numpy and zarr memory maps with Pynapple, you can manage large datasets efficiently without overwhelming memory resources. Memory maps are a powerful feature for anyone looking to scale their data processing tasks with Pynapple.