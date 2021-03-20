# Adding data to an Axes object

# Import the matplotlib.pyplot submodule.
import matplotlib.pyplot as plt

# Create a Figure and an Axes object by calling plt.subplots.
fig, ax = plt.subplots()

# Add data from the seattle_weather DataFrame by calling the Axes plot method.
ax.plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-NORMAL'])

# Add data from the austin_weather DataFrame in a similar manner and
# call plt.show to show the results.
ax.plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])
plt.show()