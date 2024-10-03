# Efficiently Saving and Loading Pynapple Objects

## Introduction
Pynapple provides efficient methods for saving and loading objects using NPZ and NWB formats. This guide demonstrates best practices for persisting your data while maintaining compatibility and easy accessibility.

## Saving Pynapple Objects

### 1. Saving to NPZ Format
The NPZ format is a convenient way to save all properties of a pynapple object, including the time support and all associated metadata.

```python
# Example of saving a Tsd object to NPZ format
import numpy as np
import pynapple as nap

# Create a sample Tsd object
tsd = nap.Tsd(t=np.arange(100), d=np.random.rand(100))

# Specify the file path for saving
npz_file_path = "my_data.npz"

# Save the Tsd object
nap.save(npz_file_path, tsd, description="This is my Tsd data")
```

### 2. Saving to NWB Format
The NWB format is structured and allows for rich metadata. It is ideal for storing large datasets derived from experiments. 

```python
# Example of saving to NWB format
from pynwb import NWBFile

# Create an NWBFile object
nwbfile = NWBFile(session_description="My experiment", identifier="001", session_start_time="2023-10-01T00:00:00")

# Add data to the NWB file
nwbfile.add_acquisition(tsd)

# Specify the file path for saving
nwb_file_path = "my_data.nwb"

# Save the data to the NWB format
with NWBHDF5IO(nwb_file_path, mode='w') as io:
    io.write(nwbfile)
```

## Loading Pynapple Objects

### 1. Loading from NPZ Format
To load data saved in NPZ format, you can use the following approach:

```python
# Loading an NPZ file
loaded_data = nap.load(npz_file_path)

# Access the Tsd object from the loaded data
tsd_loaded = loaded_data['my_data']  # Use the key you provided when saving

print(tsd_loaded)
```

### 2. Loading from NWB Format
Loading from an NWB file involves creating an instance of NWBHDF5IO. 

```python
# Loading from NWB format
from pynwb import NWBHDF5IO

# Specify the path to the NWB file
nwb_file_path = "my_data.nwb"

# Open the NWB file
with NWBHDF5IO(nwb_file_path, mode='r') as io:
    nwb_loaded = io.read()
    tsd_loaded = nwb_loaded['my_tsd_data']  # Access the stored data 

print(tsd_loaded)
```

## Best Practices
- **Use NPZ for Smaller Datasets**: NPZ is ideal for smaller, less complex datasets where metadata is not critical.
- **Use NWB for Structured Data**: NWB is preferred for larger datasets that require detailed metadata, ensuring data integrity and compatibility with various neuroscience tools.
- **Always Document Your Data**: Include descriptions and relevant metadata when saving using either format to ensure clarity when the data is accessed later.

## Conclusion
Efficiently saving and restoring pynapple objects using NPZ and NWB formats leverages the strengths of both methods. By following these best practices, you can ensure your data is accessible and well-structured for future analyses.