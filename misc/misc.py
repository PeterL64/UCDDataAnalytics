import matplotlib.pyplot as plt
import pandas as pd

#fig, ax = plt.subplots()
#plt.show()

df = pd.DataFrame({'a':[1,2,3], 'b':[5,10,15], 'cccc':[2,4,6]})
print('Original df')
print(df)

#df.drop('b', inplace=True, axis=1)
#print('New df')
#print(df)

del df['b']
print('New df method 2')
print(df)