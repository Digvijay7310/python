class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

p = Person("DJ", 21)
print(p.name, p.age)
p.info()