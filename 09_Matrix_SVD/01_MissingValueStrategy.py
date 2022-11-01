import pandas as pd
import numpy as np
data = pd.DataFrame([[1,2,np.nan],
                     [np.nan,2,np.nan, 'Yulia'],
                     [3,np.nan,np.nan, 'Anna'],
                     [np.nan,3,8],
                     [5,3,np.nan, 'Vladimir']],columns=['A','B','C','D'])

print(data,'\n') # prints the data
# counts NaN values for each feature
print(data.isnull().sum(axis=0))
"""
Because feature C has just one value, you can drop it 
from the dataset. The code
then replaces the missing values in feature B with 
a medium value and interpolates
the value in feature A because it displays a progressive order.
"""

# Drops definitely C from the dataset
data.drop('C', axis=1, inplace=True)

# Creates a placeholder for B's missing values
data['missing_B'] = data['B'].isnull().astype(int)

# uses the mode - the first most frequent value in the series
data['missing_D'] = data['D'].isnull().astype(str)

# Fills missing items in B using B's average
data['B'].fillna(data['B'].mean(), inplace=True)
data['D'].fillna(data['D'].mode().iloc[0], inplace=True),

# Interpolates A
data['A'].interpolate(method='linear', inplace=True)
print(data)