# How-to Guide: Handling Memory Maps During Analysis

This guide outlines how to effectively use numpy and zarr memory maps with pynapple for scalable data processing, allowing you to work with large datasets that may not fit in memory.

## Introduction

Pynapple provides functionalities to work with memory-mapped files, which allow for efficient reading and manipulation of large datasets without loading the entire dataset into memory directly. This is particularly useful when dealing with large time series data such as electrophysiological recordings.

### Types of Memory Maps
- **Numpy Memory Map**: NumPy provides the `np.memmap` functionality to create an array that reads data from a binary file without loading it into memory.
- **Zarr Array**: Zarr is a format for chunked, compressed, N-dimensional arrays that supports memory mapping and allows for efficient storage of large array data.

## Using Numpy Memory Map with Pynapple

### Step 1: Create a Memory Map
You can create a numpy memory map by defining the path to your data and initializing it with `np.memmap`.

```python
import numpy as np

eeg_path = "path_to_your_data.eeg"  # Path to your binary file
n_channels = 16
frequency = 1250  # Sampling rate in Hz
f = open(eeg_path, 'rb')

# Calculate number of samples
startoffile = f.seek(0, 0)
endoffile = f.seek(0, 2)
f.close()
bytes_size = 2  # Size of each data point (e.g., for int16)
n_samples = int((endoffile - startoffile) / n_channels / bytes_size)

# Create numpy memory map
fp = np.memmap(eeg_path, dtype=np.int16, mode='r', shape=(n_samples, n_channels))
```

### Step 2: Create a Pynapple Object
To integrate with pynapple, you can create a `TsdFrame` while keeping the data as a memory map.

```python
import pynapple as nap

# Create time array
timestep = np.arange(0, n_samples) / frequency

# Instantiate a pynapple TsdFrame
eeg = nap.TsdFrame(t=timestep, d=fp)

print(eeg)  # Check the TsdFrame object
```

### Step 3: Accessing Data
When accessing the data, you will just read from the memory map, stopping any need to load the entire dataset into RAM.

```python
# Check the type of eeg.values to confirm it is still a memory map
print(type(eeg.values))  # Should indicate that it is an array in memory-mapped mode
```

## Using Zarr with Pynapple

### Step 1: Create a Zarr Array
To use zarr, you'll first need to create a zarr dataset. It can be initialized as a Zarr array in your code.

```python
import zarr

# Create a zarr array
data = zarr.zeros((10000, 5), chunks=(1000, 5), dtype='i4')
timestep = np.arange(len(data))
```

### Step 2: Create a Pynapple Object
Similar to numpy memory maps, you can utilize zarr arrays directly in pynapple.

```python
# Instantiate a TsdFrame with zarr data
tsdframe = nap.TsdFrame(t=timestep, d=data)

# Check the type of TsdFrame
print(type(tsdframe.d))  # Should be a zarr array
```

### Step 3: Avoid Loading into Memory
If you want to maintain the zarr array without converting it to a numpy array, use the `load_array=False` argument.

```python
tsdframe = nap.TsdFrame(t=timestep, d=data, load_array=False)

# Confirm data type
print(type(tsdframe.d))  # Should indicate it is still a zarr array
```

### Step 4: Perform Analysis
Once your data is loaded as a memory map or zarr array, you can perform any analysis provided by pynapple without having all the data in memory.

```python
# Apply any pynapple functions directly to the memory-mapped or zarr TsdFrame
epoch = nap.IntervalSet(start=0, end=10)  # Define intervals as needed
tsdframe.restrict(epoch)  # Restrict based on defined intervals
```

## Conclusion
By effectively using numpy and zarr memory maps with pynapple, you can analyze large-scale datasets without overloading your system memory. These methods allow efficient data handling and processing necessary for scientific data analysis, especially in neuroscience applications.