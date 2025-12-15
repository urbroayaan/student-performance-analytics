def calculate_avg(marks):
    return sum(marks) / len(marks)


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


def main():
    students = load_students("students.csv")
    toppers, highest_avg = find_toppers(students)

    print("\nStudent Averages:")
    for name, marks in students.items():
        avg = calculate_avg(marks)
        print(f"{name}: {avg}")

    print("\nSubject-wise Averages:")
    subject_avgs = subject_averages(students)
    for i, avg in enumerate(subject_avgs):
        print(f"Subject {i+1}: {avg}")

    weakest = weakest_subject(subject_avgs)
    print(f"\nWeakest Subject: Subject {weakest + 1}")

    print("\nStudent Performance:")
    for name, marks in students.items():
        avg = calculate_avg(marks)
        label = performance_label(avg)
        print(f"{name}: {label}")

    print("\nToppers:", ", ".join(toppers), "with average", highest_avg)


main()
