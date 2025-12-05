

# class Student:
#     def __init__(self, name):
#         self.name = name


# s1 = Student("shradha")
# print(s1.name)



# MAke a 
'''class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

        


acc1 = Account("12345", "abcde")'''

# print(acc1.acc_no)
# print(acc1.reset_pass())


# class Person:
#     __name = "anonymous"

    
#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()


# p1 = Person()
# print(p1.welcome())



# Inheritance

# Inheritance means pass some function from parent to child like we have some functionality in our body from our parents, parents have from theor parents 

# When one class (child/derived) derives the properties & methods of another class (parent/base)


# Single Inheritance
'''
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car start")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car1.color)

'''



# This is multi level inheritance where a class inherit the methods of its parent of parent method (puppy class access dog and animal class)


'''class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod 
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def _init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type'''


# car1 = Fortuner("Electric")
# car1.start()



class Animal:

    @staticmethod
    def sound():
        print("Animal can make sounds")


class Dog(Animal):

    @staticmethod
    def bark():
        print( "Dogs are barking")


class Puppy(Dog):

    def __init__(self, name):
        self.name = name
    @staticmethod
    def makeSound():
        print("Puppy are also make sounds")


d1 = Dog()
a1 = Puppy("tony")
# print(a1.sound())
# print(a1.bark())
# print(a1.makeSound())



# Multiple class inheritance means multiple class methods access in a single class like car and fortuner class methods are access in Fortuner class
'''class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod 
    def stop():
        print("Car stopped")


class ToyotaCar():
    @staticmethod
    def logo():
        print("Toyota brands start from T")
        

class Fortuner(Car, ToyotaCar):
    @staticmethod
    def brand():
        print("Fotuner is a brand and another is prius")


c1 = Fortuner()'''
# print(c1.start())
# print(c1.logo())
# print(c1.brand())
# print(c1.stop())



class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)



'''class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod 
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()'''

# car1 = ToyotaCar("prius","electric")
# print(car1.type)




# Class method that can change the class attribute

'''class Person:
    name = "anonymous"

    
    # def changeName(self, name):
    #     self.__class__.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)
'''


# Class method use when we have some variable and need to change later without touch any other all details related to tahat change so we use propertry

'''class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

        # Percentage
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(98, 99, 97)
print(s1.percentage)
s1.phy = 86
print(s1.phy)
print(s1.percentage)
'''




# Polymorphism - same operator has different form with different data type


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 5)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()

# num3 = num1 - num2
# num3.showNumber()


# Define a circle to create a circle with radius r using the constructpr 
# Define an Area() methid of the class which calculate the area fo the circle
# Define a peimeter() method of the class which allow you to calculate the permiter of the circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)

# print(c1.area())
# print(c1.perimeter())



# Defin a Employee class with attribute role, department & salary. This class also has a show Details

# Create an Engineer class that inherit properties from Employee and has additional attribute name and age
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("Dept = ", self.dept)
        print("salary =", self.salary)

class Enginner(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Enginner", "IT", "75,000")

# e1 = Employee("accountant", "finance", "50000")
# e1.showDetails()

# eng1 = Enginner("Rahul", "40")
# print(eng1.showDetails())




# Create a class called Order which stores items & its price Use Dunder function __gt__() to convey that:
# Order1 > order2 if price of order1 > price of order2


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price
    
    def __lt__(self, o2):
        return self.price < o2.price



o1 = Order("chips", 20)
o2 = Order("Tea", 15)

print(o1 > o2)
print(o1 < o2)
