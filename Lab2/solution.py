
import pandas as pd

df = pd.read_csv("C:\Users\the_m\Documents\GitHub\Machine-learning-Lab\Lab2\food_coded.csv")


print("shape:", df.shape)      # rows, columns
display(df.head())             # first few rows
print("\ncolumns:\n", df.columns)
print("\ndtypes:\n", df.dtypes)

print("\nmissing values (top):")
print(df.isna().sum().sort_values(ascending=False).head(15))
