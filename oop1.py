class Parent:
    def parent_info(self):
        print("This is Parent class.")

class Child1(Parent):
    def c1_info(self):
        print("This is Child 1.")

class Child2(Parent):
    def c2_info(self):
        print("This is Child 2.")

c1 = Child1()
c2 = Child2()

c1.parent_info()
c2.parent_info()
# Base class
class A:
    def show_A(self):
        print("Class A")

# Child of A
class B(A):
    def show_B(self):
        print("Class B")

# Another child of A
class C(A):
    def show_C(self):
        print("Class C")

# Multiple inheritance (inherits from B and C)
class D(B, C):
    def show_D(self):
        print("Class D")

d = D()
d.show_A()   # From A
d.show_B()   # From B
d.show_C()   # From C
d.show_D()   # From D



class GrandFather:
    def grand_info(self):
        print("This is GrandFather.")

class Father(GrandFather):
    def father_info(self):
        print("This is Father.")

class Son(Father):
    def son_info(self):
        print("This is Son.")

s = Son()
s.grand_info()    # From GrandFather
s.father_info()   # From Father
s.son_info()      # From Son



# Parent Class 1
class Father:
    def father_info(self):
        print("This is Father class.")

# Parent Class 2
class Mother:
    def mother_info(self):
        print("This is Mother class.")

# Child class inheriting both Father & Mother
class Child(Father, Mother):
    def child_info(self):
        print("This is Child class.")

c = Child()
c.father_info()
c.mother_info()
c.child_info()


# Parent Class
class Animal:
    def speak(self):
        print("Animals can make sounds.")

# Child Class (Inheriting Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks.")

# Object
d = Dog()
d.speak()   # From parent
d.bark()    # From child


class Student:
    # Constructor (__init__)
    def __init__(self, name, age, grade):
        self.name = name      # Instance Variable
        self.age = age
        self.grade = grade

    # Method
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


# Creating Objects of Student class
student1 = Student("Amit", 20, "A")
student2 = Student("Riya", 19, "B")

# Calling method using objects
student1.show_details()
print()       # Just for spacing
student2.show_details()
#single inheritance
