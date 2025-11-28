# ------------------------------
# Base Class (Parent Class)
# ------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# ---------------------------------------------------
# Single Inheritance → Student inherits from Person
# ---------------------------------------------------
class Student(Person):
    def __init__(self, name, age, roll, grade):
        super().__init__(name, age)   # Call parent constructor
        self.roll = roll
        self.grade = grade

    def show_student(self):
        self.show_details()
        print(f"Roll No: {self.roll}")
        print(f"Grade: {self.grade}")


# ---------------------------------------------------
# Single Inheritance → Teacher inherits from Person
# ---------------------------------------------------
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_teacher(self):
        self.show_details()
        print(f"Subject: {self.subject}")


# ---------------------------------------------------
# Multilevel Inheritance → Principal → Teacher → Person
# ---------------------------------------------------
class Principal(Teacher):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age, subject)
        self.experience = experience

    def show_principal(self):
        self.show_teacher()
        print(f"Experience: {self.experience} years")


# ---------------------------------------------------
# Multiple Inheritance → ClassMonitor(Student + Responsibilities)
# ---------------------------------------------------
class Responsibilities:
    def duty(self):
        print("Responsible for maintaining discipline in class.")

class ClassMonitor(Student, Responsibilities):
    def show_monitor(self):
        self.show_student()
        print("Position: Class Monitor")
        self.duty()


# ---------------------------------------------------
# Hierarchical Inheritance → Different staff inherit from Person
# ---------------------------------------------------
class Clerk(Person):
    def show_clerk(self):
        self.show_details()
        print("Role: Clerk")


class Librarian(Person):
    def show_librarian(self):
        self.show_details()
        print("Role: Librarian")


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

print("---- STUDENT ----")
s = Student("Amit", 16, 12, "10th")
s.show_student()

print("\n---- TEACHER ----")
t = Teacher("Mrs. Sharma", 40, "Maths")
t.show_teacher()

print("\n---- PRINCIPAL ----")
p = Principal("Dr. Verma", 55, "Science", 25)
p.show_principal()

print("\n---- CLASS MONITOR (Multiple Inheritance) ----")
m = ClassMonitor("Riya", 15, 5, "9th")
m.show_monitor()

print("\n---- CLERK ----")
c = Clerk("Suresh", 35)
c.show_clerk()

print("\n---- LIBRARIAN ----")
l = Librarian("Meena", 45)
l.show_librarian()
