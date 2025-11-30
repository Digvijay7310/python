# By default when a fiel is not exist and and we try to open it with w or a method python create a file.

# w method delete all the data from file and insert a new data in file
# a method first add new data in file then show all the data exist previous first
# r+ means read and write 

# when we need to delete a file we import os then os.remove("filename with path")


# f = open("demo.txt", "r")


# line = f.readline()
# print(line)

# line2 = f.readline()
# print(line2)

# data = f.read()
# print(data)
# f = open("hero.txt", "a+")

# print(f.read())
# f.write("abc")
# f.close()



# with open("demo.txt", "r") as f:
#     data = f.read() 
#     print(data)

# with open("hero.txt", "w") as f:
#     f.write("Hello how are you.")

# For remove a particular file

# import os
# os.remove("heero.txt")




# with open("practice.txt", "r") as f:
#     data = f.read()

#     new_data = data.replace("Java", "Python")
#     print(new_data)


# with open("practice.txt", "w") as f:
#     f.write(new_data)
    # f.write("Hi everyone\nwe are learning File I/O")
    # f.write("\nusing Java\nI like programming in Java")



# def check_for_word():
#     with open("practice.txt", "r") as f:
#      data = f.read()

#     if(data.find("learning") != -1):
#         print("found")
#     else:
#         print("not found")


# check_for_word()





# def check_for_line():
#    word = "learnin3g"
#    data = True
#    line_no = 1
#    with open("practice.txt", "r") as f:
#       while data:
#          data = f.readline()
#          if(word in data):
#             print(line_no)
#             return
#          line_no += 1


#       return -1

# print(check_for_line())




# count = 0
# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = data.split(",")
#     for values in num:
#         if(int(values) % 2 == 0):
#             print(values)
#             count += 1

# print(count)
