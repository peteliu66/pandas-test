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
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
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
# print(df2.shape)

print(df.head)

print(df.tail(3))

print(df.index)

print(df.columns)

print(df.to_numpy())
print(df2.to_numpy())

print(df.describe)
print(df.T)

print("Sorting by an axis:")
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by="B"))

print(df["A"])
print(df[1:4])

print(df["20130102":"20130104"])

print(df.loc[dates[0]])
print(df.loc[:, ["A", "B"]])

print(df.loc["20130102",["A","B"]])

print(df.loc[dates[0],"A"])