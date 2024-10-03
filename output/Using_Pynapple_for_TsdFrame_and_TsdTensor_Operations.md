# Using Pynapple for TsdFrame and TsdTensor Operations

## Overview
Pynapple offers specific data structures to handle different types of time-series data efficiently. This guide focuses on two key data structures: `TsdFrame` for column-based data and `TsdTensor` for multi-dimensional data. Understanding how to use these structures will help you manage and analyze your time-series data effectively.

## Data Structures

### TsdFrame
- **Definition**: The `TsdFrame` is designed for column-based data representations, similar to a pandas DataFrame. It allows easy manipulation and access to individual columns of time-series data.
- **Initialization**: You can create a `TsdFrame` by providing time and data along with optional column labels.

```python
import pynapple as nap
import numpy as np

# Example initialization of a TsdFrame
t = np.arange(100)  # Time
d = np.random.rand(100, 3)  # Data for three columns
columns = ['a', 'b', 'c']  # Column labels
tsdframe = nap.TsdFrame(t=t, d=d, columns=columns)
```

- **Accessing Data**: You can access specific columns, rows, or utilize pandas-like operations.

```python
# Access first column
first_column = tsdframe['a']

# Access multiple columns
selected_columns = tsdframe[['a', 'c']]

# Get as pandas DataFrame
df = tsdframe.as_dataframe()
```

- **Attributes**: You can access attributes such as `.values` for the data array, `.shape` for dimensions, and `.ndim` to know the number of dimensions.

### TsdTensor
- **Definition**: The `TsdTensor` is intended for managing multi-dimensional time-series data, such as in movies or multi-channel recordings. Each dimension can represent a different variable in addition to time.
- **Initialization**: Similar to `TsdFrame`, you can create a `TsdTensor` by providing time and multi-dimensional data.

```python
# Example initialization of a TsdTensor
t = np.arange(100)  # Time
d = np.random.rand(100, 5, 5)  # Multi-dimensional data (e.g., 5x5 grid)
tsdtensor = nap.TsdTensor(t=t, d=d, time_units="s")
```

- **Accessing Data**: You can slice these tensors in a similar manner to numpy arrays, allowing for powerful data manipulation.

```python
# Access a slice of the tensor
slice_tensor = tsdtensor[0:10]  # First 10 time points

# Access a specific element in the tensor
element = tsdtensor[0]  # First element in the first dimension
```

- **Attributes**: Similar to `TsdFrame`, you can access attributes such as `.values`, `.shape`, and `.ndim`.

## Operations

### Slicing
Both `TsdFrame` and `TsdTensor` allow you to slice and access their contents in a way that retains the time support for the data you extract.

```python
# For TsdFrame (Columns can be sliced similarly to pandas DataFrames)
first_ten_rows = tsdframe[:10]  # First 10 rows of the dataframe
```

### Arithmetic Operations
You can perform arithmetic operations directly on objects of these types, which will output another object of the same type, maintaining the time structure.

```python
# Element-wise operations
result = tsdframe + 1  # Adds 1 to each element in the TsdFrame
```

### Conversion to Pandas
Both `TsdFrame` and `Tsd` can be easily converted to their respective pandas types, allowing for further analysis or visualization using pandas tools.

```python
# Convert TsdFrame to pandas DataFrame
df_from_tsdf = tsdframe.as_dataframe()
```

### Combining Data
When working with two separate time series represented by either `TsdFrame` or `TsdTensor`, you can concatenate them along the appropriate axis, provided the time indices are compatible.

```python
# Concatenating two TsdFrames vertically if they share the same columns
combined_frame = np.concatenate((tsdframe1, tsdframe2), axis=0)
```

## Conclusion
With `TsdFrame` and `TsdTensor`, Pynapple provides versatile data structures for managing both column-based and multi-dimensional time-series data. Use these structures effectively to streamline your data analysis and make the most of your time-series data.