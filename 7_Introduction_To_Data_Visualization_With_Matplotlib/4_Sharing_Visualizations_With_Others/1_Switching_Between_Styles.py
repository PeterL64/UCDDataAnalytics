# Switching Between Styles

import matplotlib.pyplot as plt


# Select the 'ggplot' style, create a new Figure called fig,
# and a new Axes object called ax with plt.subplots.
plt.style.use('ggplot') # This is the line where you change the style. 'ggplot' is one style
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

# A short list of styles to try for plots:

# plt.style.use('default')
# 'ggplot' - Grey Background, White Gridlines - People familiar with R use this
# 'seaborn-colorblind' or 'tableau-colorblind10' - for colourblind people
# 'grayscale' - black and white, suitable for printing.
