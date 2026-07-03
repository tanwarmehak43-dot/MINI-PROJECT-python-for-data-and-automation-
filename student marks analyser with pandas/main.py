import pandas as pd

# Read CSV
data = pd.read_csv("students.csv")

# Pass/Fail filter
data["Status"] = data["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Add Grade column
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

data["Grade"] = data["Marks"].apply(grade)

# Sort by Marks
sorted_data = data.sort_values(by="Marks", ascending=False)

print(sorted_data)

# Export cleaned data
sorted_data.to_csv("cleaned_students.csv", index=False)

print("\nCleaned data exported successfully!")