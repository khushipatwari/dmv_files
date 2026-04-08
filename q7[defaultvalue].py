#python code for handling missing variable
import pandas as pd
data = {
    "Name": ["Arittra", "Riya", "Rahul", None],
    "Age": [21, None, 23, 22],
    "Marks": [85, 90, None, 88]
}
df = pd.DataFrame(data)
print(df)
print("\nMissing Values Count:")
print(df.isnull().sum())

dffilled = df.fillna(0)
print(dffilled)