# the match statement (introduced in Python 3.10) is used for pattern matching and conditional execution based on the value of an expression.
# It allows you to compare the value of an expression against multiple patterns and execute the corresponding code block for the first matching pattern.
from re import match

# The match statement provides a more expressive and structured way of handling multiple conditions compared to traditional if-elif-else statements.
# It promotes code readability and can simplify complex branching logic.

a = int(input("Enter number: "))

match a:
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case 13:
        print("case is 13")
    case 22:
        print("case is 22")
    case _:
        print("no match found")
        


