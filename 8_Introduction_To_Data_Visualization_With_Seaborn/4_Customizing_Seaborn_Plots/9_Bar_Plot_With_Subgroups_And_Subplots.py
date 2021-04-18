# Bar Plot with Subgroups and Subplots

# Set the figure style to "dark"
sns.set_style('dark')

# Adjust the bar plot code to add subplots based on "Gender", arranged in columns.
g = sns.catplot(x="Village - town", y="Likes Techno",
                data=survey_data, kind="bar",
                col='Gender')

# Add the title "Percentage of Young People Who Like Techno" to this FacetGrid plot.
# Label the x-axis "Location of Residence" and y-axis "% Who Like Techno".
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence",
       ylabel="% Who Like Techno")

# Show plot
plt.show()