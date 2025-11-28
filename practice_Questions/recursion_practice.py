'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1) * n

print(factorial(5))
'''

"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
       return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
"""



'''
def sum_n(n):
    if(n == 0):
        return 0
    
    return n + sum_n(n-1)



print(sum_n(10))

'''



'''

def reverse_string(s):
    if s == "":
        return ""
    
    return reverse_string(s[1:]) + s[0]


print(reverse_string("hello"))

'''




'''
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1: -1])

print(is_palindrome('racecar'))

'''



'''
def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y-1)

print(power(2,3))

'''


'''

def gcd(a, b):
    if(b ==0):
        return a
    return gcd(b, a % b)

print(gcd(122, 144))
'''