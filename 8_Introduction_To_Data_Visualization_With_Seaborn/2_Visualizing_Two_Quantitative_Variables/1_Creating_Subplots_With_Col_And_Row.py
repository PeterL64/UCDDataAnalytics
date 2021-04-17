# Creating Subplots with Col and Row

# Change to use relplot() instead of scatterplot()
# sns.scatterplot(x="absences", y="G3", data=student_data)
sns.relplot(x="absences", y="G3", data=student_data, kind='scatter')

# Modify the code to create one scatter plot for each level of the variable "study_time", arranged in columns.
sns.relplot(x="absences", y="G3", data=student_data, kind='scatter', col='study_time')

# Adapt your code to create one scatter plot for each level of a student's weekly study time, this time arranged in rows.
sns.relplot(x="absences", y="G3", data=student_data, kind='scatter', row='study_time')