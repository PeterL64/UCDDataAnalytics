# Adjusting the Whiskers

import matplotlib.pyplot as plt
import seaborn as sns

sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box")

# Adjust the code to make the box plot whiskers to extend to 0.5 * IQR. Recall: the IQR is the interquartile range.
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=0.5)
plt.show()

# Change the code to set the whiskers to extend to the 5th and 95th percentiles.
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=[5,95])
plt.show()

# Change the code to set the whiskers to extend to the min and max values.
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=[0, 100])
plt.show()