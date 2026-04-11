class Teacher:
    def __init__(self,salary):
        self.salary = salary

class Student:
    def __init__(self,grade):
        self.grade = grade

class TA(Teacher,Student):
    def __init__(self,salary,grade,name):
        super().__init__(salary)
        Student.__init__(self,grade)
        self.name = name

ta1 = TA(50000, 'A', 'John Doe')
print(f"TA Name: {ta1.name}, Salary: {ta1.salary}, Grade: {ta1.grade}")

