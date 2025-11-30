# Guess the random game using random module

'''
import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the number or quit: ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break

    elif(userChoice < target):
        print("Your number is to small. Take a bigger guess")
    else:
        print("Your number is to big. Take a smaller guess")

print("-------GAME OVER---------")

'''


'''
import random
import string

pass_len = 12
charVal = string.ascii_letters + string.digits + string.punctuation


res = "".join([random.choice(charVal) for i in range(pass_len)])
print(res)

password = ""
for i in range(pass_len):
     password += random.choice(charVal)



print("your password string ", password)
'''

