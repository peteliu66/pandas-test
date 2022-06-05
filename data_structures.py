import numpy as np
import pandas as pd

# Object creation
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Object creation")
print(s)
# Creating a DataFrame
dates = pd.date_range("20130101", periods=6)
print("Creating a DataFrame")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

df2 = pd.DataFrame(
    {
        "A":1.0,
        "B":pd.Timestamp("20130102"),
        "C":pd.Series(1,index=list(range(4)), dtype="float32"),
        "D":np.array([3] * 4, dtype="int32"),
        "E":pd.Categorical(["test","train","test","train"]),
        "F":"foo"
    }
)
print(df2)
print(df2.dtypes)
# Here is a subset of the attributes
# df2.<TAB>  # noqa: E225, E999
# df2.A                  df2.bool
# df2.abs                df2.boxplot
# df2.add                df2.C
# df2.add_prefix         df2.clip
# df2.add_suffix         df2.columns
# df2.align              df2.copy
# df2.all                df2.count
# df2.any                df2.combine
# df2.append             df2.D
# df2.apply              df2.describe
# df2.applymap           df2.diff
# df2.B                  df2.duplicated
print(df2.abs)