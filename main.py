def calculateAvg(marks):

    return sum(marks) / len(marks)

def loadStudents(filename):

    students = {}
    with open("students.csv","r") as file:
        lines = file.readlines()

    for line in lines[1:]:
        parts = line.strip().split(",")

        name = parts[0]
        marks = list(map(int, parts[1:]))
        students[name] = marks
    
    return students

def findToppers(students):

    topper = []
    highest_avg = 0

    for name, marks in students.items():
        avg = calculateAvg(marks)

        if (avg > highest_avg):
            highest_avg = avg
            topper = [name]

        elif (avg == highest_avg):
            topper.append(name)

    print(f"Name: {name}    Average Marks: {avg}")
    return topper, highest_avg

def main():
    students = loadStudents("students.csv")
    toppers, highestAvg = findToppers(students)

    print()


    if len(toppers) == 1:
        print("Topper:", toppers[0], "with an average mark of", highestAvg)
    else:
        print("Multiple Toppers: ",", ".join(toppers), "with an average mark of", highestAvg)

main()
