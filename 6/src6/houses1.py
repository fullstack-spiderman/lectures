# Reads a CSV file into a list of dict objects

students = []

with open("houses.csv") as file:
    next(file)
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({
            "name": name,
            "house": house
        })

for student in students:
    print(f"{student['name']} is in {student['house']}")