# How to Stream Data from DANDI

This guide outlines the steps to stream data directly from the DANDI Archive into the pynapple package for real-time data analysis. By following these instructions, you will be able to efficiently access and process data without needing to download entire datasets.

## Step-by-Step Instructions

1. **Install Necessary Packages**
   Ensure you have the required packages installed. You can install them using pip:

   ```bash
   pip install matplotlib seaborn dandi fsspec pynwb h5py
   ```

2. **Import the Required Libraries**
   Start your Python script or Jupyter Notebook by importing the necessary libraries:

   ```python
   from pynwb import NWBHDF5IO
   from dandi.dandiapi import DandiAPIClient
   import fsspec
   from fsspec.implementations.cached import CachingFileSystem
   import h5py
   import pynapple as nap
   import matplotlib.pyplot as plt
   import seaborn as sns
   import numpy as np
   ```

3. **Define the DANDI Data Set**
   Specify the `dandiset_id` and the `filepath` to the data you want to stream. For example:

   ```python
   dandiset_id, filepath = (
       "000582",
       "sub-10073/sub-10073_ses-17010302_behavior+ecephys.nwb",
   )
   ```

4. **Connect to the DANDI Archive**
   Use `DandiAPIClient()` to connect to DANDI. This allows you to stream the data directly from the archive.

   ```python
   with DandiAPIClient() as client:
       asset = client.get_dandiset(dandiset_id, "draft").get_asset_by_path(filepath)
       s3_url = asset.get_content_url(follow_redirects=1, strip_query=True)
   ```

5. **Create a Virtual Filesystem**
   Set up a virtual filesystem that uses the HTTP protocol to access the data:

   ```python
   fs = fsspec.filesystem("http")
   ```

6. **Set Up Caching (Optional)**
   You can create a caching filesystem to save downloaded data to disk. This step is optional but can improve efficiency:

   ```python
   fs = CachingFileSystem(
       fs=fs,
       cache_storage="nwb-cache",  # Specify a local folder for the cache
   )
   ```

7. **Open the NWB File**
   Use the `h5py` library to open the NWB file through the virtual filesystem:

   ```python
   file = h5py.File(fs.open(s3_url, "rb"))
   io = NWBHDF5IO(file=file, load_namespaces=True)
   ```

8. **Load Data into pynapple**
   You can now stream data directly into pynapple using the `NWBFile` class:

   ```python
   nwb = nap.NWBFile(io.read())
   ```

9. **Accessing Data**
   After loading the NWB file, you can access various data types. For example, to access spike timings or position data:

   ```python
   spikes = nwb["units"]  # Get spike timings
   position = nwb["position"]  # Get tracked position data
   ```

10. **Data Processing and Analysis**
    You can now process and analyze the streamed data in real-time using pynapple's functionalities, such as plotting, computing tuning curves, and more.

## Conclusion
By following these steps, you can stream data directly from the DANDI Archive into pynapple, enabling efficient real-time data analysis. This approach is particularly useful for working with large datasets that may not fit entirely into memory. Happy analyzing!