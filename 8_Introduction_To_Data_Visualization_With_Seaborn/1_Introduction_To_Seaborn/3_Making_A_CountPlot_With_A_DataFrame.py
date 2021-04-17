# Making a CountPlot with a DataFrame


# Import Matplotlib, Pandas, and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Use the countplot() function with the x= and data= arguments to create a count plot
# with the "Spiders" column values on the x-axis.
sns.countplot(x='Spiders', data=df)

# Display the plot
plt.show()
