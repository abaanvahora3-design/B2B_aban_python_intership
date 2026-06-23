import json

students = [
    {"name": "John", "marks": 85},
    {"name": "Alice", "marks": 92},
    {"name": "Bob", "marks": 78}
]

with open("students_list.json", "w") as file:
    json.dump(students, file, indent=4)
print("Saved 3 students to students_list.json")

print("\n--- Reading Data Back ---")
with open("students_list.json", "r") as file:
    loaded_data = json.load(file)
    
for student in loaded_data:
    print(f"{student['name']} scored {student['marks']}")