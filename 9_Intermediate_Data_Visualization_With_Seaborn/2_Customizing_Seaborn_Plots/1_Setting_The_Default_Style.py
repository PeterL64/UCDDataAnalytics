# Setting the Default Style

# Assume all the libraries have been imported, matplotlib, seaborn, pandas

# Plot a pandas histogram without adjusting the style.
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

# Set Seaborn's default style.
sns.set()

# Create another pandas histogram of the fmr_2 column which represents fair market rent for a 2-bedroom apartment.
df['fmr_2'].plot.hist()
plt.show()
plt.clf()