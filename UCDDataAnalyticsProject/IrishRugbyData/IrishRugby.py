import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# File name
file = "IREMatchData(FULL).csv"

# Loading file
IrelandDF = pd.read_csv(file)

print(IrelandDF.head())
print(type(IrelandDF))
print(IrelandDF.info())
