# Visualizing standard deviation with line plots
import matplotlib.pyplot as plt
import seaborn as sns

# Change the plot so the shaded area shows the standard deviation instead of the confidence interval for the mean.
sns.relplot(x="model_year", y="mpg", data=mpg, kind="line", ci='sd')
# ci = Confidence Interval, sd = Standard Deviation

plt.show()