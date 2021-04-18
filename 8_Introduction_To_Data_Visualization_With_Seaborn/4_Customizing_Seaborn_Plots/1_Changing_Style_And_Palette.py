# Changing Style and Palette

import matplotlib.pyplot as plt
import seaborn as sns

# sns.set_style()
# Some background style types to use: 'white', 'dark', 'whitegrid', 'darkgrid', 'ticks'.
# sns.set_palette()
# Some Diverging Palettes to use: 'RdBu', 'PRGn', 'RdBu_r', 'PRGn_r'.
# The palettes above are Red-Blue, Purple-Green, Blue-Red(Red-Blue reversed), Green-Purple(Purple-Green reversed).
# Some Sequential Palettes: 'Greys', 'Blues', 'PuRd'(Purple-Red), 'GnBu'(Green-Blue.)

# Set the style to "whitegrid" to help the audience determine the number of responses in each category.
sns.set_style('whitegrid')

# Set the color palette to the sequential palette named "Purples".
sns.set_palette("Purples")

# Change the color palette to the diverging palette named "RdBu".
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes",
                  "Often", "Always"]

sns.catplot(x="Parents Advice",
            data=survey_data,
            kind="count",
            order=category_order)

# Show plot
plt.show()