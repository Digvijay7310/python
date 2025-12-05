# Recursion
# when a function call itself repeatly then we can say that recursion and this is a another sibling of loop that performs task repetly but sometime both usecase is different.


# Write a recursice function to calculate the sum of first n natural numbers. 

# def sum(n):
#     if(n == 0):
#         return 0
#     else:
#         return sum(n-1) + n
    
# print(sum(5))

# Print factorial of a n numbers
# def fact(n):
#     if(n <= 1):
#         return 1
#     return fact(n-1) * n
# print(fact(5))

# Write a recursive function to print all elements in a list.
# Hint: user list & index as parameters.

# def print_el(list):
#     idx = 0
#     while idx < len(list):
#         print(list[idx])
#         idx += 1

# nums = [10, 20, 30, 40, 50, 60]
# print_el(nums)


# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["Mango", "Litchi", "Banana", "Apple", ]

# print_list(fruits)