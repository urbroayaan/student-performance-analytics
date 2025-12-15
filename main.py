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


def weakest_subject(subje_
