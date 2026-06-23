class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 = Student("John", 85)
student2 = Student("Alice", 92)

print("--- Student 1 ---")
print(f"Name: {student1.name}")
print(f"Marks: {student1.marks}")

print("\n--- Student 2 ---")
print(f"Name: {student2.name}")
print(f"Marks: {student2.marks}")
