# Exception handling in Python is a mechanism that allows you to handle
# and manage runtime errors and exceptional conditions that may occur during the execution of a program.
# By using exception handling, you can catch and handle errors gracefully,
# preventing the program from crashing and providing useful error messages or performing alternative actions.

# Exception handling is done using a combination of the "try", "except", "else", and "finally" keywords.

try:
    a = int(input("Enter a number"))
    print(a + 5)

except Exception as e:
    print("Some error occured: ",e)