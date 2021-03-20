# How to save your plots so you can share them with others

plt.show()

# Save file as a PNG file
fig.savefig('my_figure.png')

# Save the file as a PNG with 300dpi (dots per inch)
fig.savefig('my_figure_300dpi.png', dpi=300)

# Set the figure size as width of 3 inches and height of 5 inches and
# save it as 'figure_3_5.png' with default resolution.
fig.set_size_inches([3,5])
fig.savefig('figure_3_5.png')

# Set the figure size to width of 5 inches and height of 3 inches and
# save it as 'figure_5_3.png' with default settings.
fig.set_size_inches([5,3])
fig.savefig('figure_5_3.png')