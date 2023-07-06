# the if-else statement is used for conditional execution of code blocks based on certain conditions.
# It allows you to specify different paths of execution depending on whether a condition is True or False.

age = int(input("Enter your age: "))
if(age >= 18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
print("End of Code")


marks = int(input("Enter your marks"))

if 90<marks<=100:
    print("You are  Amazing")
elif 70 < marks <=90:
    print("Very Good")
elif 60 < marks <=70:
    print("Good")
elif 40 < marks <= 60:
    print("Average")
elif 30<= marks <= 40:
    print("Below Average")
else:
    print("Better Luck Next Time")

