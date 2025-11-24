# List is the another build in data type which can store multiple set of values.
# It can be mutable 
# It store value like integer, float, and string


# list practice question:-

# # Enter three movie name and store in a list 

movies = []

movies.append( input("Enter first movie: "))
movies.append( input("Enter second movie: "))
movies.append( input("Enter third movie: "))

print(movies)
print(type(movies))

# Tuple is a another build in datatype which can store multiple value inside a paranthesis.
# It is immutable and same like list.

# # List contains a palindrome of elements.

list = [1, 2, 3, 2, 1]
print(list)

copy_list = list.copy()

print(copy_list)

if(list == copy_list):
    print("list is palindrome")
else:
    print("List is not palindrome")

list = ["r", "a", "c", "e", "c", "a", "r"]

print("List", list)
new_list = list.copy()
print("New list", new_list)

if(new_list == list):
    print("Palindrome")
else:
    print("Not Palindrome")



# WAP to check the count of number of students with the following grade in a tuple and also store the values in list and sort with a and d

tup = ("C", "D", "A", "A", "B", "B", "A")

print(tup.count("A")) # Check the count in a tuple

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort() # Sort the grade by A and D
print(grade)
