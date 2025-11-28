""""

Print all the character starts with k with hello greet

l = ["Digvijay", "kumar", "kavita", "Gopal", "Sachin", "kamini", "Manish"]

for i in l:
    if(i.startswith("k")):
        print(f"Hello {i}")


Write a problem to print multiplicaiton table of a number using loop 

n = int(input("Enter the number: "))

for num in range(1, 11):
    print(f"{n} * {num} = {n*num}")
"""



""""
Do previous questin with while loop

n = int(input("Enter the number: "))

i=1
while i<11:
    print(f"{n} * {i} = {n*i}")
    i += 1

print("Loop End")
"""



"""
Print the given number is prime or not 
n = int(input("Enter the number: "))

for i in range(2, n):
    if n % i == 0:
        print("Number is not prime")
        break

else:
    print("Number is prime")

"""



"""
 Take a number from user and print the sum of n natural numnbers

n = int(input("Enter the number: "))

sum = 0
i = 0

while i <= n:
    sum += i
    i += 1

print(f"sum is {sum}")

"""





""""
Print the factorial number while and for loop

n = int(input("Enter the number: "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print(f"factorial is {fact}")


Using For loop

num = int(input("Enter the number: "))

fact = 1
for i in range(1, num + 1):
    fact *= i

print(f"Factorial number is {fact}")
"""



 
"""
  *
 ***
*****


n = int(input("Enter the number: "))

for i in range(1, n+1):
  print(" "* (n-i), end="")
  print("*"* (2*i-1), end="")
  print("")

"""





""""
*
**
***

n = 3

for i in range(1, n+1):
    print("*"* (i))

"""




'''

***
* *
***



n = int(input("Enter the size: "))

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")


'''




'''

Write a program to print multiplication table of n using for loops in reversed order
    
n = int(input("Enter the number"))


for i in range(1, n+1):
    print(f"{n} * {i} = {n*i}")

'''



''''


1
12
123
1234
12345


n = int(input("Enter the number: "))

a = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")

    print()
    
'''