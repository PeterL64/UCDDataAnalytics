# Hue and Count Plots

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Fill in the palette_colors dictionary to map the "Rural" location value
# to the color "green" and the "Urban" location value to the color "blue".
palette_colors = {'Rural': "green", 'Urban': "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x='school', data=student_data, hue='location', palette=palette_colors)



# Display plot
plt.show()