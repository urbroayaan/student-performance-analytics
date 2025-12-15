def calculateAvg(marks):
    return sum(marks) / len(marks)

students = {}
with open("students.csv","r") as file:
    lines = file.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")

    name = parts[0]
    marks = list(map(int, parts[1:]))
    students[name] = marks

topper = []
highest_avg = 0

for name, marks in students.items():
    avg = calculateAvg(marks)

    if (avg > highest_avg):
        highest_avg = avg
        topper = [name]

    elif (avg == highest_avg):
        topper.append(name)
        highest_avg = avg

    print(f"Name: {name}    Average Marks: {avg}")

print()

if len(topper) == 1:
    print("Topper:", topper[0], "with an average mark of", highest_avg)
else:
    print("Multiple Toppers: ",", ".join(topper), "with an average mark of", highest_avg)
