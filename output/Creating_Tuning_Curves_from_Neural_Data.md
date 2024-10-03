# How-To Guide: Creating Tuning Curves from Neural Data

This guide will walk you through the process of generating and analyzing tuning curves from neural activity datasets using the `pynapple` package. Follow these step-by-step instructions to visualize how neural activity relates to various stimuli or behavioral variables.

## Step 1: Import Necessary Libraries

First, import the libraries you will be using for your analysis.

```python
import numpy as np
import pynapple as nap
import matplotlib.pyplot as plt
import seaborn as sns
```

## Step 2: Load Neural Data

Load your dataset, which can be in the form of neural spike data stored in a `NWB` file or any other compatible format. Here, we assume you have a `NWB` file.

```python
data = nap.load_file("path/to/your/datafile.nwb")  # Load the NWB file
```

## Step 3: Extract Relevant Variables

Extract the spike times and the relevant behavioral variable (e.g., position, head direction). Here's how you might get spike data and a behavior variable from your dataset:

```python
spikes = data["units"]  # Extract the spike timings
behavior_variable = data["ry"]  # Extract the behavioral variable, e.g., head direction
```

## Step 4: Select Epochs for Analysis

Identify the relevant time intervals during which your analysis will take place. You can define specific epochs of interest, such as periods when the animal is running or exploring.

```python
epochs_of_interest = data["running_epoch"]  # Define the epochs of interest
```

## Step 5: Compute Tuning Curves

Use the `compute_1d_tuning_curves` function to calculate the tuning curves for each neuron. This function requires your spike data, the behavior variable, and the specified epochs.

```python
tuning_curves = nap.compute_1d_tuning_curves(
    group=spikes, 
    feature=behavior_variable, 
    nb_bins=61,  # Number of bins
    ep=epochs_of_interest,  # Specify the epochs of interest
    minmax=(0, 2 * np.pi)  # Specify minimum and maximum values for normalization
)
```

## Step 6: Analyze the Tuning Curves

You can now analyze the tuning curves to identify patterns in neural activity. You may want to plot the tuning curves for individual neurons or calculate preferred angles, if applicable.

### Plotting Tuning Curves

```python
plt.figure(figsize=(12, 6))
for i in range(tuning_curves.shape[1]):  # Loop through the neurons
    plt.subplot(4, 5, i + 1)
    plt.plot(tuning_curves.iloc[:, i])  # Plot the tuning curve for neuron i
    plt.title(f"Neuron {i + 1}")
    plt.xlabel("Behavior variable (units)")
    plt.ylabel("Firing Rate (Hz)")
plt.tight_layout()
plt.show()
```

### Preferred Angle Calculation

If applicable, you may want to calculate the preferred angle or condition information based on the tuning curves:

```python
preferred_angles = tuning_curves.idxmax()  # Get preferred angle for each neuron
```

## Step 7: Compare Across Conditions (Optional)

If you have data from different conditions or epochs, you can repeat the above steps for each condition and compare the results. This might involve averaging tuning curves or calculating differences in preferred angles.

## Conclusion

Following these steps, you will be able to create, analyze, and visualize tuning curves from neural data using the `pynapple` package. This analysis helps uncover how neural activity corresponds to specific behavioral variables or stimuli.

Feel free to modify any parameters or plots to suit the specifics of your dataset and analysis needs!