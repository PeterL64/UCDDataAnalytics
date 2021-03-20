# Extracting and Visualizing HDF5 Data

# Get the HDF5 group, assign to: group
group = data['strain']

# Check out keys of group
for key in group.keys():    # Iterate over group.keys() in the for loop
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value # You can get values of the time series data by
                                        # appending .value to data['strain']['Strain']

# Set number of time points to sample and assign to variable: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
