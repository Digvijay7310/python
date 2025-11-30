'''


class Student:
    college_name = "ABC College"
    name = "anonymous"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("Welcome student!", self.name)

    def get_marks(self):
        print(self.marks, "is the marks of", self.name)

s1 = Student("Karan", 98)
s1.hello()
s1.get_marks()

'''




# Create student class that makes name and marks 0f 3 subjects as arguments in constructor then create a method to pritn the averge


'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "your average score is: ", sum/3) 



s1 = Student("Arjun", [98, 78, 89])

print(s1.name)
s1.get_avg()

s1.name = 'ironman'
s1.get_avg()

'''



'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello")

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "your average score is: ", sum/3) 


s1 = Student("tony stark", [99, 98, 97])
s1.hello()
s1.get_avg()

'''



# Object oriented pr


# Abstraction 

#  - Hiding the implementation details of a class only showing the essentials features to the users.


'''

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

# Here the unnecessary work like clutch accelataotr not show in result  thats called absraction

    def stop(self):
        self.clutch = False
        self.acc = False
        print("car stop!.")


car1 = Car()
car1.start()
car1.stop()

'''




# Encapsulation
# Every thin gwe done before like write static method and hello method in student class and do all work in a single object




# Create Account class with 2 attributes balance and account no. Create methods for debit, credit & printing the balance.

'''
class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def get_deb(self, amount):
        self.bal -= amount
        print("Rs.", amount, "was debited")
        print("Total balance", self.get_bal())

    def get_crd(self, amount):
        self.bal += amount
        print("Rs.", amount, "was credit")
        print("Total balance", self.get_bal())

    def get_bal(self):
        return self.bal



a1 = Account(10000, 123456)
print(a1.get_bal())
a1.get_deb(890)
print(a1.get_bal())
a1.get_crd(1000)
print(a1.get_bal())

'''