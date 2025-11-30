# For loop

# string = "Digvijay kumar"

# for char in string:
#     print(char)

# print("End of loop")


# Using else keyword
# string = "digvijay kumar"

# for char in string:
#     if (char == 'i'):
#         print("char fount ", char)
#     else:
#         print("finding...")
#     print("End of loop")


# string = "digvijaykumar"

# for char in string:
#     if (char == 'i'):
#         print("char found ", char)
#         break
#     print("finding..")




# Print the elements of the following list using a loop:

# nums = [1 ,4, 9, 16, 25, 36, 49, 64, 81, 100]

# for num in nums:
#     print(num)

# Searc for a number x in this tuple using for loop:
# nums = [1 ,4, 9, 16, 25, 36, 49, 64, 81, 100]

# x = 30
# for num in nums:
#     if(num == x):
#         print("Number found", num)
#         break
#     print("Searching...")
# print("End ")

 
# Range function
# range(start? , stop, step?)



# seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])




# for i in range(5): # range(stop) 0, 1, 2, 3, 4
#     print(i)

# for i in range(1, 5): # start from 1 and end in 5 answer 1, 2,2 3, 4,
#     print(i)



# for i in  range(1, 10, 2): # range start from 1 and end in 10 and step += 2 means answer 1, 3, 5, 7, 9
#     print(i)




# Print only even number

# for i in range(2, 101, 2):
#     print(i)


# Print odd numbers

# for i in range(1, 101, 2):
#     print(i)


# Print number from 1 to 100

# for i in range(1, 101):
#     print(i)



# Print number form 100 to 1

# for i in range(101, 0, -1):
#     print(i)
 




# Print the multiplication table of a number n using for and range function .

# x = int(input("Enter number: "))

# for i in range(x, x*11, x):
#     print(i)





# pass statement

# for i in range(5):
#     pass

# print("End")



# WAP to find the sum  of first n numbers (using while)


# n = 5
# sum = 0

# for i in range(1, n+1):
#     sum += i

# print("Total sum:", sum)


# n = int(input("Enter the number: "))

# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1

# print("Sum of first n number is: ", sum)


# WAP to find the factorial of first numbers. (using for)

# n = int(input("Enter number: "))

# fact = 1
# i = 1

# while i <= n:
#     fact *= i
#     i += 1

# print("Total fact = ", fact)



# n = 5
# fact = 1

# for i in range(1, n+1):
#    fact *= i

# print("Factorial value ", fact)