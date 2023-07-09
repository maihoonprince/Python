# File I/O (Input/Output) in Python allows you to read data from and write data to files.

#
# s = "Prince is a good boy"

# Writing to a file:-

# with open("test.txt", "w") as f:
#     f.write(s)

# fp = open("file.txt", "w")
# fp.write(s)
# fp.close()

# Reading to a file:-

# with open("test.txt", "r") as f:
#     r = f.read()
#     print(r)
#
# f = open("test.txt", "r")
# s  = f.read()
# print(s)
# f.close()


#appending to a file
#Append will write everytime we process the code.

with open("test.txt", "a") as f:
    f.write("i am persuing B.tech in cse")

