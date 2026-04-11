class Student:
    class_name ="ABC collage"
    PI = 3.14

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        self.PI = 3.14159

stu1= Student("John Doe", 3.5)
print(f"Student Name: {stu1.name}, CGPA: {stu1.cgpa}, Class Name: {Student.class_name}, PI: {Student.PI}")