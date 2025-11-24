# Dictinory is a pre built data type which store key and value pairs inside a curly praces.
# It is mutable but not accept duplicate keys
# It is unordered.

info = {
    "name": "Digvijay",
    "lastName": "kumar",
    "age": 22,
    "Subjects": ["English", "Maths", "Physics"],
    "Marks": ("34","56","86")
}
info2 = {}
print(type(info2))

info["city"] = "new Delhi"

info["Subjects"] = {
    "English": 90,
    "Hindi": 79,
    "Maths": 90,
    "Physics": 78
}

sub = tuple(info["Subjects"])
print(type(sub))

print(type(info))
print(len(info))
info["age"] = "23"
print(info)
print(info.keys())
print(info.values())
print(info.items())

# print(info.get("firstName"))  #it never return error so while practice try to use this type.
# print(info["firstName"]) return error 




# Set is a build in datatype which can store the multiple values.
# It is mutable but its values are immutable.
# It can store only single value duplicate value are ignored because their hash numbers are same

num = {1, 2, 3, 4, 4}
print(type(num))

num.add(5)
print(num)
print(num.pop())
print(num)
num.remove(3)
print(num)
num.clear()
print(num.clear())

num2 = {2, 4, 5, 6, 6, 7, 8 ,7, 4}
new_num = num.union(num2) # print only single value same element after ist occurance remove
print(new_num)

#  num2 = {7, 4, 5, 6, 6, 7, 7, 8, 3}
#  num3 = num.intersection(num2) # only unique value print like in ist set {1, 3, 2}  and second set {1, 3, 5} print only 1 and 3
#  print(num3)

# define empty set
# num2 = set()
# print(type(num2))



# store following word meanings in a python dict 
# table: "A piece of a furniture", "List of facts and figures"
# cat: " a small animal"

# texts = {
#     "table": ("a piece of furniture", "list of facts & figures" ),
#     "cat": "a small animal ",
# }

# print(type(texts))


# List of subjects and each subject each class how many class need with a set

collections = {"Python", "Java", "Javascript", "C++", "Python",
               "Java", "C", "C++", "Python", "Javascript"
               }

collection = str(collections)
print(type(collection))
print(len(collections), " Class need for total following subjects")



subjects = {}

subjects.update({"physics": input("Enter physics marks ")})
subjects.update({"Maths": input("Enter Maths marks ")})
subjects.update({"Hindi": input("Enter hindi marks ")})

print(subjects)
print(type(subjects))




# figure out a way to store 9 and 9.0 as seperate value in a set

values = {9, 9.0} # if we do this it return only single value because 9 and 9.0 have same hash value 
print(values)


values = [9, (9.0)]  # it read 9 as number and 9.0 as a float
print(values)

print(type(values[1]))