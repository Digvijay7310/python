"""
Docstring for learning.Exception_handling.data
"""
""" 
This will help us to if error not throw error send a message this will not stop our program.

try:
    # code that may fail
except:
    # What to do if code occurs

"""

# Case: Take a number from user if string send a message

# try:
#     n = int(input("Enter a number: "))
#     print("Your number is: ", n)

# except:
#     print("Please enter only number")


# Handle multiple error

# try:
#     x = int(input("Enter a number: "))
#     print(10/x)
# except ZeroDivisionError:
#     print("Numner is not divisible by 0")
# except ValueError:
#     print("Number is required")



# Handle error with a finally msg 
# try:
#     f = open("../file_handling/students.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Program completed")



# Zero Division Handling
try:
    x = int(input("Enter a number: "))
    print("Your number is: ", x)
    print(100/x)
except ValueError:
    print("Invalid input - enter numbers only")


try:
    f = open("student.txt", 'r')
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Thanks for using program")



try:
    n = int(input("Enter a number: "))
    if n == 0:
        print("Numbre is greater than 0")
    else:
       print("Square is:", (n * n))
except ValueError:
    print("Invalid input - Enter number")