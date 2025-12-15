students = {
    "Ayaan": [99, 85, 90],
    "Rahul": [60, 72, 68],
    "Neha": [88, 91, 84],
    "Sara": [55, 65, 58]
}

topper = ""
highest_avg = 0

for name, marks in students.items():
    avg = sum(marks) / len(marks)

    if (avg > highest_avg):
        highest_avg = avg
        topper = name

    elif (avg == highest_avg and highest_avg != 0):
        print("Multiple Toppers")
        highest_avg = avg

    print(f"Name: {name}    Average Marks: {avg}")

print(f"Topper is {topper} with an average mark of {highest_avg}")
