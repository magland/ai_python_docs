# Advanced Time Series Manipulation with Pynapple

## Description
Delve deeper into time series slicing, indexing, and arithmetic operations tailored for neuroscience data using the `pynapple` package. This guide will cover the various techniques to effectively manipulate time series data, focusing on their specific applications within neuroscience.

## 1. Initialization of Time Series Objects

Before diving into the manipulations, let's initialize different time series objects using sample data.

```python
import numpy as np
import pynapple as nap

# One-dimensional time series
tsd = nap.Tsd(t=np.arange(100), d=np.random.rand(100), time_units="s")

# Multi-dimensional time series (frame)
tsdframe = nap.TsdFrame(t=np.arange(100), d=np.random.rand(100, 3), columns=['a', 'b', 'c'])

# Tensor time series
tsdtensor = nap.TsdTensor(t=np.arange(100), d=np.random.rand(100, 5, 5), time_units="s")
```

## 2. Slicing Time Series

Pynapple supports slicing of time series. This allows you to retrieve specific segments of your data.

### 2.1 Slicing Tsd Object
To slice a Tsd object:

```python
# First 10 elements from the Tsd
print(tsd[0:10])
```

### 2.2 Slicing TsdFrame Object
You can also select specific columns and rows:

```python
# First column from TsdFrame
print(tsdframe[:, 0])  # Returns a Tsd object

# Rows based on specific column values
print(tsdframe.loc['a'])  # Access all rows for column 'a'
print(tsdframe.loc[['a', 'c']])  # Access multiple columns
```

### 2.3 Slicing TsdTensor Object
You can slice tensors similarly:

```python
# First 10 elements from TsdTensor
print(tsdtensor[0:10])
```

## 3. Indexing for Time Series Data

Pynapple provides robust indexing capabilities that allow you to focus on data points of interest.

### 3.1 Accessing Attributes
The basic attributes of the dataset can be accessed:

```python
print(len(tsd))  # Length of the time series
print(tsd.shape)  # Shape of the data
print(tsd.ndim)   # Number of dimensions
```

### 3.2 Time Indexes
The `time index` can be accessed using:

```python
print(tsd.index)  # Get the time index array
```

## 4. Arithmetic Operations on Time Series

You can perform arithmetic operations directly on time series data, adhering to the dimensionality rules.

### 4.1 Element-wise Arithmetic
Perform arithmetic operations such as addition, subtraction, etc., while ensuring dimensional compatibility:

```python
# Addition example
tsd = nap.Tsd(t=np.arange(5), d=np.ones(5))
result = tsd + 1  # Add 1 to each element
print(result)

# Subtraction example
result = tsd - np.ones(5)  # Subtract a numpy array
print(result)

# Note: Operations between Tsd objects with the same time index are not allowed
try:
    tsd + tsd  # This will raise an error
except Exception as error:
    print(error)
```

### 4.2 Statistical Operations
You can also leverage Numpy functions for statistical operations. Most common functions will return a time series if applicable:

```python
# Mean across time
mean_tsd = np.mean(tsdtensor, 0)  # Average over the first dimension; returns a numpy array
print(mean_tsd)

# Average across the second dimension; returns TsdFrame
mean_frame = np.mean(tsdtensor, 1)
print(mean_frame)
```

## 5. Modifying Time Series

Pynapple allows you to modify time series elements:

```python
# Modifying elements based on conditions
tsd[tsd.values > 0.5] = 0.0
print(tsd)

# Element-wise modification
tsd1 = nap.Tsd(t=np.arange(5), d=np.ones(5))
tsd1[0] = np.pi  # Set the first element to pi
print(tsd1)
```

## Conclusion

In this guide, we've explored advanced techniques for manipulating time series data with the Pynapple package. With the ability to slice, index, and perform arithmetic operations, you will be better equipped to handle and analyze neuroscience data. Happy coding!