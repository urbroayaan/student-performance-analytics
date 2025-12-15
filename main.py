students = {
    "Ayaan": [59, 85, 90],
    "Rahul": [60, 72, 68],
    "Neha": [99, 85, 90],
    "Sara": [55, 65, 58]
}

topper = []
highest_avg = 0

for name, marks in students.items():
    avg = sum(marks) / len(marks)

    if (avg > highest_avg):
        highest_avg = avg
        topper = [name]

    elif (avg == highest_avg and highest_avg != 0):
        topper.append(name)
        highest_avg = avg

    print(f"Name: {name}    Average Marks: {avg}")

print()

if len(topper) == 1:
    print("Topper:", topper[0], "with an average mark of", highest_avg)
else:
    print("Multiple Toppers: ",", ".join(topper), "with an average mark of", highest_avg)
