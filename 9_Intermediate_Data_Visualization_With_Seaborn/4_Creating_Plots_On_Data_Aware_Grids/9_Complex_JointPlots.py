# Complex JointPlots

# The jointplot is a convenience wrapper around many of the JointGrid functions.
# However, it is possible to overlay some of the JointGrid plots on top of the standard jointplot.


# Create a jointplot with a scatter plot comparing temp and casual riders.
# Overlay a kdeplot on top of the scatter plot.
g = (sns.jointplot(x="temp",
                   y="casual",
                   kind='scatter',
                   data=df,
                   marginal_kws=dict(bins=10, rug=True))
     .plot_joint(sns.kdeplot))

plt.show()
plt.clf()


# Replicate the above plot but only for 'registered' riders.
g = (sns.jointplot(x="temp",
             y="registered",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True))
    .plot_joint(sns.kdeplot))

plt.show()
plt.clf()
