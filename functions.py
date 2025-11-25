# Functions in python is a vlock of code that performs a specific tasks and can be reuseable in a app or code.

# def sum(a, b):  functions defination
#     s = a + b
#     return s
# print(sum(10, 20)) function call the value are arguments that we pass to a funciton

# Take value from user in function

# def sum(a, b):
#     s = a + b
#     return s

# a = int(input("Enter value a "))
# b = int(input("Enter value b "))

# print(sum(a, b))


# A function is never return anuything their output will be none

# def hello():
#     print("hello")

# output = hello()  # when fn call the print fn inside hello fn work but while calling show none becuse not return anything
# print(output)
# print(hello())



# def cal_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg

# d = int(input("Enter a "))
# e = int(input("Enter b "))
# f = int(input("Enter c "))

# print(cal_avg(d, e, f))



# WAP to print the lenght of a list using fns (list is teh parameter)
# cities = ["delhi", "gurugram", "noida", "pune", "mumbai", "chennai"]
# heroes = ["thor", "ironman", 'captain america', 'shaktiman']

# def print_len(li):
#     print(len(li))

# print_len(cities)
# print_len(heroes)

# WAF to print the elements of a list in a single line (list is the parameter)

# cities = ["delhi", "gurugram", "noida", "pune", "mumbai", "chennai"]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(cities)   



# WAP to find the factorial of n (n is parameter)
# n = int(input("Enter number: "))

# fact = 1
# i = 1

# while i <= n:
#     fact *= i
#     i += 1

# print(fact)


# def cal_fac(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)



# cal_fac(5)


# WAP to convert USD to INR 

# def convertor(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val, "INR")

# convertor(10)



# WAP to check number is odd or even

def check_odd_even(n):
    if(n % 2 != 0):
        print(n, "Is odd number")
    elif(n % 2 == 0):
        print(n, "is even number")
    else:
        print("Invalid number")

check_odd_even(20)
