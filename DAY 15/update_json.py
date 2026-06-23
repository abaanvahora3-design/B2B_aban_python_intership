import json

try:
    with open("student.json", "r") as file:
        student = json.load(file)
        
    print(f"Original: {student}")
    
    student["marks"] = 95
    student["grade"] = "A"
    
    with open("student.json", "w") as file:
        json.dump(student, file, indent=4)
        
    print(f"Updated: {student}")
    print("Updates saved successfully!")

except FileNotFoundError:
    print("Error: Run task1_write_json.py first to create the file.")