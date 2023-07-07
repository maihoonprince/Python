# a function is a block of reusable code that performs a specific task.
# It is a way to divide your code into smaller, manageable pieces and organize your program's logic.
# Functions take input arguments, perform operations, and can optionally return a value.

# syntax for defining a function in Python:-

# level-1:-
def greetHello():
    print("Hello World")
    print("I am Prince.")


print("Executing Function.....")
greetHello()
print("Done.")


# Level-2:-
def greetHello(name, ending):  # here name and ending are two veriable
    print("Hello " + name)
    print("I am Prince.")
    print(ending)


print("Executing Function.....")
greetHello("world", "Thank You")
greetHello("shivam", "Thanks")
print("Done.")


# level-3:-
def letterGenerator(name, date):
    st = f"Hi mam, This is {name} and i will not come to school on {date}."
    print(st)


print("Executing Program.....")
letterGenerator("Prince", "8-july")
letterGenerator("shivam", "9-july")
print("done")


#level-4:-

def average(a, b):
    return(a+b)/2

a = int(input("Enter value of a"))
b = int(input("Enter value of b"))

print(average(a, b))
