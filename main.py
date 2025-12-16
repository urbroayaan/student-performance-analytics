import pandas as pd
df = pd.read("students.csv")

df["average"] = df[["sub1", "sub2", "sub3"]].mean(axis=1)                   # row-wise mean

highest_avg = df["average"].max()
toppers = df[df["average"] == highest_avg]["name"]

subject_avgs = df[["sub1", "sub2", "sub3"]].mean()
weakest_subject = df["average"].idxmin()                   # gives subject name with weakest mean and not mean value

def load_students(filename):
    students = {}

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines[1:]:
        parts = line.strip().split(",")
        name = parts[0]
        marks = list(map(int, parts[1:]))
        students[name] = marks

    return students

def find_toppers(students):
    toppers = []
    highest_avg = 0

    for name, marks in students.items():
        avg = calculate_avg(marks)

        if avg > highest_avg:
            highest_avg = avg
            toppers = [name]
        elif avg == highest_avg:
            toppers.append(name)

    return toppers, highest_avg

def subject_averages(students):
    subject_totals = []
    student_count = len(students)

    for marks in students.values():
        if not subject_totals:
            subject_totals = [0] * len(marks)

        for i in range(len(marks)):
            subject_totals[i] += marks[i]

    return [total / student_count for total in subject_totals]

def weakest_subject(subject_avgs):
    weakest_index = 0
    for i in range(len(subject_avgs)):
        if subject_avgs[i] < subject_avgs[weakest_index]:
            weakest_index = i
    return weakest_index

def performance_label(avg):
    if avg >= 85:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    elif avg >= 50:
        return "Average"
    else:
        return "Needs Improvement"

print("\nStudent Averages:")
print(df[["name", "average"]])

print("Topper(s):", ",".join(toppers), "with average", highest_avg)

print("\nSubject-wise Averages:")
print(subject_avgs)
