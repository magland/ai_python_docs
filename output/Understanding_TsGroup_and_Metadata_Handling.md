# How-to Guide: Understanding TsGroup and Metadata Handling

This guide provides insights into organizing and manipulating groups of time series data with metadata using pynapple's `TsGroup`. `TsGroup` is a powerful tool for managing multiple time series with varying timestamps and associating metadata with each series. Follow the steps below to effectively use `TsGroup` and handle metadata:

## Step 1: Import Necessary Libraries
Start by importing the necessary libraries.
```python
import numpy as np
import pandas as pd
import pynapple as nap
```

## Step 2: Create Time Series Objects
Generate a few `Ts` objects, which hold timestamped data. These will be used to create the `TsGroup`.
```python
my_ts = {
    0: nap.Ts(t=np.sort(np.random.uniform(0, 100, 1000)), time_units="s"),
    1: nap.Ts(t=np.sort(np.random.uniform(0, 100, 2000)), time_units="s"),
    2: nap.Ts(t=np.sort(np.random.uniform(0, 100, 3000)), time_units="s")
}
```

## Step 3: Instantiate a TsGroup
Create a `TsGroup` from the `Ts` objects. `TsGroup` can hold multiple `Ts` objects and is useful for organizing groups of time series data.
```python
tsgroup = nap.TsGroup(my_ts)
print(tsgroup)
```

## Step 4: Add Metadata to TsGroup
Customize your `TsGroup` by adding metadata, such as labels or other relevant information, for each time series. Metadata can be added during initialization or after creating the `TsGroup`.

### Option 1: Add Metadata During Initialization
```python
label = pd.Series(index=list(my_ts.keys()), data=["A", "B", "C"])
tsgroup = nap.TsGroup(my_ts, my_label=label)
```

### Option 2: Add Metadata After Initialization
Use the `set_info` method or direct item assignment to add metadata.
```python
tsgroup.set_info(new_label=np.array(["Type1", "Type2", "Type3"]))
tsgroup["additional_info"] = np.random.randn(len(tsgroup))
```

## Step 5: Access and Manipulate Metadata
Access the metadata using attributes or methods, and manipulate them as needed.

### View Metadata
```python
print(tsgroup.my_label)
print(tsgroup.get_info("new_label"))
```

### Query TsGroup Based on Metadata
Use metadata to query and filter the `TsGroup`. This is helpful for focusing analyses on specific subsets of your data.

#### Categorize by Metadata
```python
categories = tsgroup.getby_category("my_label")
print(categories["A"])
```

#### Threshold by Metadata
```python
subset = tsgroup.getby_threshold("additional_info", 0)
print(subset)
```

## Step 6: Apply Operations on TsGroup
Perform operations directly on `TsGroup`, such as restricting the time series to certain intervals or calculating counts.

### Restrict to Specific Intervals
```python
intervals = nap.IntervalSet(start=[0, 50], end=[20, 100])
restricted_group = tsgroup.restrict(intervals)
```

### Count Data Points
```python
counts = tsgroup.count(1, intervals, time_units="s")
print(counts)
```

## Conclusion
`TsGroup` in pynapple allows for the organization and manipulation of multiple time series with associated metadata. By following this guide, you can effectively use `TsGroup` to manage complex time series data and conduct efficient analyses based on metadata attributes.