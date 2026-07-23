import pandas as pd
df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 40],
    }
)
print(df) 

ages = pd.Series([25, 30, 35, 40], name="Age")
print(ages.max())
print(ages.min())
print(ages.mean())
print(ages)

