import numpy as np
import pandas as pd

# Object creation
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# Creating a DataFrame
dates = pd.date_range("20130101", periods=6)
print(dates)

