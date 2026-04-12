class Student:
    def __init__(self,name,subject ):
        self.name = name
        self.subject = subject
        print("This is a constructor")

stq1 = Student("Arnob", "Maths")
stu1 = Student("Python", "Programming")
print(stq1.name)
print(stq1.subject)
print(stu1.name)
print(stu1.subject)