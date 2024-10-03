# How-to Guide: Creating Continuous Spectral Density Estimates

## Description:
This guide will help you compute power spectral densities (PSD) across different epochs to thoroughly analyze the signal characteristics using the `pynapple` package. 

## Steps:

1. **Load Your Data**: First, ensure that you have your signal data in a `Tsd`, `TsdFrame`, or `TsGroup` format and that you have defined the epochs you are interested in analyzing.

    ```python
    import pynapple as nap

    # Load your data (Example)
    data = nap.load_file("your_data_file.nwb")  # Replace with your file
    signal = data["desired_signal"]  # Change to your signal object
    epochs = data["desired_epochs"]  # Change to your epoch object
    ```

2. **Select the Interval Size**: Determine the duration of epochs you wish to analyze. This is done by setting the `interval_size` parameter. This size defines how long each segment of data will be for the PSD computation.

3. **Compute Power Spectral Density**: Use the `nap.compute_mean_power_spectral_density` function to compute the spectral density estimates. Set the `ep` argument to the epochs you defined earlier and specify other necessary parameters like the sampling rate.

    ```python
    fs = 1250  # Sampling frequency, update based on your specific data
    mean_psd = nap.compute_mean_power_spectral_density(
        signal,
        interval_size=1.5,  # Set your desired interval size
        fs=fs,
        ep=epochs,
        norm=True  # To ensure the output is normalized
    )
    ```

4. **Analyze the Results**: The output will be a normalized power spectral density for each specified epoch. You can visualize the results or further analyze the data for your specific application.

    ```python
    import matplotlib.pyplot as plt
    
    # Plotting the resulting mean PSD
    plt.figure(figsize=(10, 6))
    plt.plot(mean_psd.index, mean_psd.values)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power Spectral Density")
    plt.title("Mean Power Spectral Density Estimates")
    plt.show()
    ```

5. **Iterate if Needed**: If you want to analyze different epochs or modify the intervals, repeat steps 2 to 4 with the new configuration to explore various characteristics of your signal.

### Conclusion:
By following the above steps, you can efficiently compute continuous spectral density estimates for your signal data across different epochs. This method will provide invaluable insights into the frequency characteristics of your signals, especially for time-varying phenomena.