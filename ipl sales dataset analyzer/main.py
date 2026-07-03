import pandas as pd

data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\python data automation\ipl sales dataset analyzer\sales.csv")

print(data)

print("Dataset:")
print(data)

print("\nTotal Sales:", data["Sales"].sum())
print("Average Sales:", data["Sales"].mean())

sorted_data = data.sort_values(by="Sales", ascending=False)
print("\nSorted Sales:")
print(sorted_data)