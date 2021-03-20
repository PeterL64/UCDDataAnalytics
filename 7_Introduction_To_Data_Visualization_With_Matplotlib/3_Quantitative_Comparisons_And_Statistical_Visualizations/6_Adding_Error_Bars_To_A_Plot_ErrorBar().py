# Adding error-bars to a plot using the .errorbar() Method


import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Use the ax.errorbar method to add the Seattle data: the "MONTH" column as x values,
# the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.
ax.errorbar(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'], yerr=seattle_weather['MLY-TAVG-STDDEV'])

# Add the Austin data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values
# and "MLY-TAVG-STDDEV" as yerr values.
ax.errorbar(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'], yerr=austin_weather['MLY-TAVG-STDDEV'])

# Set the y-axis label as "Temperature (Fahrenheit)".
ax.set_ylabel('Temperature (Fahrenheit)')

plt.show()