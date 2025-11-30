# Basics questions for python practice

'''
Take a number from user and do all math calculation
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

print("Sum of a and b is ", a+b)
print("Difference of a and b is ", a-b)
print("product of a and b is ", a*b)
print("divison of a and b is ", a/b)



Take a str from user and print reverse
a = input("Enter a reverse: ")

print("Reversed string ", a[::-1])



Take a number from user and check if they can vote or not

age = int(input("Enter the age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")




# Take a number from user and see the number is odd or even

n = int(input("Enter the number: "))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")




# Calculate the celsius to fahrenheit

c = float(input("Enter temp. in celcius: "))
f = (9/5) * c + 32
print("Temperature in fahrenheit: ", f)'''



# Loop & condition

'''
Print all the numbers between 1 to 100
for n in range(1, 101):
    if(n % 2 == 0):
        print(n)


# Print the factorial of number
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Fact of n is ",fact)




# Check if a number is prime or not

n = int(input("Enter the number: "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not prime number")
        break
else:
    print(f" {n} is prime")




# Print the series of fibonacci
n = int(input("Enter the value n: "))

a, b = 0, 1

print("Fibonacci series: ")

for _ in range(n):
    print(a, end="")
    a, b = b, a + b




# from a list find largest and smallest number using loop

li = [12, 32, 45, 1, 0, 56, 9, 20]

print(max(li))
print(min(li))

largest = li[0]
smallest = li[0]

for num in li:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num


print("Largest ", largest)
print("smallest ",smallest)


# make a list and print all list element squares

numbers = [1, 2, 3, 4, 5]
square = []

for n in numbers:
    square.append(n * n)

print("Original list:", numbers)
print("Square list:", square)



# Take a 5 number form user and print the list, sum and factorial of a list
li = []
sum = 0
fact = 1

li.append(int(input("Enter a number: ")))
li.append(int(input("Enter b number: ")))
li.append(int(input("Enter c number: ")))
li.append(int(input("Enter d number: ")))
li.append(int(input("Enter e number: ")))

print("List is:", li)

for i in li:
    sum += i
print("Sum is", sum)

for i in li:
    fact *= i
print("Factorial is", fact)


# Make a dictionary that take student data name, age, marks

student = {
    "name": "Gopal",
    "age": 23,
    "marks": 94
}

print(student)

student["marks"] = input("Change your marks ")
print(student)



# Made ziop of two list and make a single dictionary

keys = ["a", "b", "c"]
values = [1, 2, 3]

result = dict(zip(keys, values))

print(result)



s = input("Enter a string: ")

char_count = {}

for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("charactetr counts: ", char_count)

'''

