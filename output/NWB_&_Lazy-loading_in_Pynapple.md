# How-To Guide: NWB & Lazy-loading in Pynapple

## Introduction
In this guide, you will learn how to efficiently load and work with Neurodata Without Borders (NWB) files using Pynapple's lazy-loading features. This allows you to work with large datasets without requiring all data to be loaded into memory at once.

## Required Libraries
Make sure you have the necessary packages installed. You can do this via pip:

```bash
pip install pynapple dandi fsspec h5py
```

## Step-by-Step Instructions

### Step 1: Import Libraries
Start by importing the required libraries for loading NWB files:

```python
from pynwb import NWBHDF5IO
from dandi.dandiapi import DandiAPIClient
import fsspec
from fsspec.implementations.cached import CachingFileSystem
import h5py
import pynapple as nap
```

### Step 2: Stream Data from DANDI
You can stream NWB data directly from the DANDI Archive without having to download the entire dataset first.

1. Specify the dataset ID and path to the NWB file:

```python
dandiset_id, filepath = ("000582", "sub-10073/sub-10073_ses-17010302_behavior+ecephys.nwb")
```

2. Use the Dandi API Client to get the asset and create a filesystem for streaming:

```python
with DandiAPIClient() as client:
    asset = client.get_dandiset(dandiset_id, "draft").get_asset_by_path(filepath)
    s3_url = asset.get_content_url(follow_redirects=1, strip_query=True)
```

3. Establish a caching filesystem to save downloaded data locally:

```python
fs = fsspec.filesystem("http")
fs = CachingFileSystem(fs=fs, cache_storage="nwb-cache")
```

### Step 3: Open the NWB File
Open the NWB file using `h5py` and `NWBFile` from Pynapple:

```python
file = h5py.File(fs.open(s3_url, "rb"))
io = NWBHDF5IO(file=file, load_namespaces=True)
```

### Step 4: Load NWB Data into Pynapple
Once the NWB file is opened, you can start streaming specific data into Pynapple:

```python
nwb = nap.NWBFile(io.read())
```

### Step 5: Access and Explore the Data
Once you have the NWB data loaded into Pynapple, you can access various datasets:

```python
spikes = nwb["units"]  # Access spike timings
epochs = nwb["epochs"]  # Access behavioral epochs
position = nwb["position"]  # Access position data
```

### Step 6: Perform Data Analysis
You can now perform various types of analyses without loading the entire dataset into memory. Use functions like `nap.compute_power_spectral_density` or `nap.compute_mean_power_spectral_density` while restricting your analysis to specific epochs:

```python
power = nap.compute_mean_power_spectral_density(eeg, ep=wake_ep, fs=FS, norm=True)
```

### Additional Notes:
- Keep in mind that while lazy loading is efficient for large datasets, careful code structuring is key to avoid out-of-memory errors.
- Using `lazy_loading=False` when initializing the `NWBClass` can help if you want to load the dataset entirely, but this might lead to performance issues when dealing with large files.

## Conclusion
You have successfully set up lazy-loading for NWB files in Pynapple, enabling efficient data analysis without overwhelming system memory. This approach is particularly useful for handling large experimental datasets in neuroscience.