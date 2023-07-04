# some of the commonly used operators in Python:

# Arithmetic Operators:

# + : Addition
# - : Subtraction
# * : Multiplication
# / : Division
# % : Modulo (Remainder)
# ** : Exponentiation (Power)
# // : Floor Division (Integer Division)

# Assignment Operators:

# = : Assigns a value to a variable
# += : Adds the right operand to the left operand and assigns the result to the left operand
# -= : Subtracts the right operand from the left operand and assigns the result to the left operand
# *= : Multiplies the left operand by the right operand and assigns the result to the left operand
# /= : Divides the left operand by the right operand and assigns the result to the left operand
# %= : Performs modulo operation on the left operand with the right operand and assigns the result to the left operand
# **= : Raises the left operand to the power of the right operand and assigns the result to the left operand
# //= : Performs floor division on the left operand with the right operand and assigns the result to the left operand

# Comparison Operators:

# == : Equality
# != : Inequality
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

# Logical Operators:

# and : Logical AND
# or : Logical OR
# not : Logical NOT

# Bitwise Operators:

# & : Bitwise AND
# | : Bitwise OR
# ^ : Bitwise XOR
# ~ : Bitwise NOT
# << : Bitwise Left Shift
# >> : Bitwise Right Shift

# Membership Operators:

# in : Evaluates if a value is present in a sequence
# not in : Evaluates if a value is not present in a sequence

# Identity Operators:

# is : Evaluates if two variables refer to the same object
# is not : Evaluates if two variables do not refer to the same object

#we cannot use space between variable names. like num 1 it is wrong
num1 = 10
num2 = 3

#Arithmetic Operator

print("num1 + num2 =", num1 + num2)
print("num1 - num2 =", num1 - num2)
print("num1 * num2 =", num1 * num2)
print("num1 / num2 =", num1 / num2)
print("num1 // num2 =", num1 // num2) #In Python, the // operator is used for floor division or integer division.
print("num1 ** num2 =", num1 ** num2) #In Python, the ** operator is used for exponentiation
print("num1 % num2 =", num1 % num2) # use to remainder calculation

#Assignment Operator


a = 4
a *= 2
print(a)

b = 2
b **= 2
print(b)

c = 8
c /= 4
print(c)

#Comprasion Operator

x = 8
y = 3
print(x<y)
print(x>y)
print(x != y)

z = 8
print(x==z)

#Logical Operator

print("Logical Operator")
print(x==z and x<y)
print(x==z or x<y)
print(not(True))
print(not(False))
