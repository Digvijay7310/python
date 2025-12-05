computer = -1
yourStr = input("Enter your choice: ")
yourDict = {"s": 1, "w": -1, "g": 0}
you = yourDict[yourStr]

if(computer == -1 and you == 1):
    print("You win")

elif(computer == -1 and you == 0):
    print("You Loose")

elif(computer == 1 and you == -1):
    print("You Lose!")

elif(computer == 1 and you == 0):
    print("You Win!")

elif(computer == 0 and you == -1):
    print("You Lose!")

elif(computer == 0 and you == 1):
    print("You Lose!")

else:
    print("Somthing went wrong")