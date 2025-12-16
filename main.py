import pandas as pd

df = pd.read_csv("students.csv")

# Student-wise average
df["average"] = df[["sub1", "sub2", "sub3"]].mean(axis=1)           # row-wise mean

# Topper(s)
highest_avg = df["average"].max()
toppers = df[df["average"] == highest_avg]["name"]

# Subject-wise averages
subject_avgs = df[["sub1", "sub2", "sub3"]].mean()

# Weakest subject
weakest_subject = subject_avgs.idxmin()         # gives subject name with weakest mean and not mean value

# Performance labeling
def performance_label(avg):
    if avg >= 85:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    elif avg >= 50:
        return "Average"
    else:
        return "Needs Improvement"

df["performance"] = df["average"].apply(performance_label)

# Output
print("\nStudent Averages:")
print(df[["name", "average"]])

print("\nTopper(s):", ", ".join(toppers), "with average", highest_avg)

print("\nSubject-wise Averages:")
print(subject_avgs)

print("\nWeakest Subject:", weakest_subject)

print("\nStudent Performance:")
print(df[["name", "performance"]])
