# Efficiently Saving and Loading Pynapple Objects

This guide covers best practices for saving and restoring pynapple objects using NPZ and NWB formats.

## Saving Pynapple Objects

### Using NPZ Format

1. **Choose the Right Directory:**
   Ensure you have a structured directory setup that aligns with your project needs. This helps in maintaining clarity and organization, especially for larger datasets.

2. **Saving a Pynapple Object:**
   Use the `save` method of a `Folder` object to save your pynapple objects. Provide a filename and description for the object you're saving.

   ```python
   import pynapple as nap
   import numpy as np

   # Creating sample objects
   tsd = nap.Tsd(t=np.arange(0, 100), d=np.random.rand(100))
   epoch = nap.IntervalSet(start=[0, 10], end=[5, 15])

   # Assuming 'session' is your Folder object where you want to save these
   session.save("example_tsd", tsd, description="Sample TSD object")
   session.save("example_epoch", epoch, description="Sample IntervalSet")
   ```

3. **Add Metadata:**
   Make sure your NPZ file is accompanied by a JSON sidecar file with metadata. This follows BIDS specifications for better data sharing and understanding.

4. **Visualize and Document:**
   After saving, use the `expand` method to check and confirm your data structure.

   ```python
   # Visualizing the saved data
   session.expand()

   # Documenting
   session.doc("example_tsd")
   ```

### Using NWB Format

While pynapple can load NWB files efficiently, creating NWB files typically requires other tools like NeuroConv or NWBmatic. Once created, NWB files can be easily loaded for use in your pynapple workflows.

```python
# Basic loading structure
import pynapple as nap

# Load NWB file
path = "path_to_your_file.nwb"
data = nap.load_file(path)

# Access data
spikes = data["units"]
```

## Loading Pynapple Objects

### Loading from NPZ Files

1. **Utilize the Folder Class:**
   Use pynapple's `Folder` object to navigate through structured datasets easily. Initialize your folder structure and load NPZ files accordingly.

   ```python
   data = nap.load_folder("path_to_your_project")
   session = data["subject"]["session_name"]

   # Access loaded data
   tsd_loaded = session["example_tsd"]
   epoch_loaded = session["example_epoch"]
   ```

2. **Lazy Loading:**
   Pynapple supports lazy loading for efficient memory utilization. When using NPZ files, data is only loaded when accessed, reducing unnecessary memory usage.

3. **Verify and Use Metadata:**
   Always verify metadata using the `doc` method to understand data provenance and structure.

   ```python
   # Verify metadata
   session.doc("example_tsd")
   ```

### Loading from NWB Files

1. **Utilize Lazy Loading:**
   When loading NWB files, pynapple ensures efficient memory management by employing lazy loading, loading data only when accessed.

   ```python
   nwb_data = nap.NWBFile(path, lazy_loading=True)

   # Access specific data
   lfp = nwb_data['lfp_channel_name']
   ```

2. **Streamlining Data Access:**
   Use `get` and `restrict` methods when loading data slices or when working with specific epochs to enhance performance.

   ```python
   # Example of accessing a specific time interval
   example_interval = nap.IntervalSet(start=0, end=10)
   restricted_data = lfp.restrict(example_interval)
   ```

By following these practices, you can efficiently save, document, and load pynapple objects in both NPZ and NWB formats, ensuring your data is well organized and easily accessible for analysis.