students = [
    {"Name": "abaan", "Marks": 85},
    {"Name": "faiz", "Marks": 92},
    {"Name": "saed", "Marks": 78}
]

for student in students:
    name = student["Name"]
    marks = student["Marks"]
    print(f"Student: {name}, Marks: {marks}")
