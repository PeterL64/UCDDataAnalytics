# Defining Custom Palettes

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# When visualizing multiple elements of data it is useful to use a colour palette to better show the data.
# However different palette types are better for different types of data.
# Here are some examples:

# Circular Data: When the data is not ordered. (Random Colours)
sns.palplot(sns.color_palette('Paired', 12))
# This has a random palette of 12 colours

# Sequential Colours: When the data has a consistent range from high to low. (Light blue growing to a solid blue)
sns.palplot(sns.color_palette('Blues', 12))
# This palette starts as a faded light blue and grows in 12 steps to a full coloured blue.

# Diverging Colours: When both low and high values are interesting.
sns.palplot(sns.color_palette('BrBG', 12))
# This palette starts as solid brown, fades to a light colour in the middle, then fades to a blue/green at the end.

plt.show()


# Create and display a Purples sequential palette containing 8 colors.
sns.palplot(sns.color_palette('Purples', 8))

# Create and display a palette with 10 colors using the husl system.
sns.palplot(sns.color_palette('husl', 10))

# Create and display a diverging palette with 6 colors coolwarm.
sns.palplot(sns.color_palette('coolwarm',6))
plt.show()
