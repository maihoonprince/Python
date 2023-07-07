#  a while loop is a control flow statement that repeatedly executes a block of code as long as a specified condition remains true.
# It is useful when you don't know in advance how many times the loop needs to be executed and want to continue looping until a certain condition is met.

#The syntax of a while loop in Python is :-

i = 0;
while(i<=10):
    print(i)
    i += 1


#infinite Loop:-
# while(True):
#     print("While loop is not finished")

while(True):
    num = int(input("Enter number: "))
    print(num)
    if num == 0:
        break

