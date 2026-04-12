class employee:
    start_time = "10:00 AM"
    end_time = "6:00 PM"

    def change_end_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(employee):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class admin(employee):
    def __init__(self, name, department):
        self.name = name
        self.department = department        


t1 = Teacher("Arnob", "Maths")
t1.change_end_time("7:00 PM")
print(t1.name, t1.subject, t1.start_time, t1.end_time)          # Arnob Maths 10:00 AM 6:00 PM

a1 = admin("John", "IT")
print(a1.name, a1.department, a1.start_time, a1.end_time)        # John IT 10:00 AM 6:00 PM