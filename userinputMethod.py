name = input("Enter your name: ")
print(name)
print(type(name))  #----> type(name) is used to find datatype of any element...

# PYTHON ALWAYS TAKE INPUT IN THE FORM OF STRING.

#it will show error  if we add directly without  changing input number in integer:  ex:  print(number + 6) ----> it will show error:

number = input("Enter a number: ")
print(int(number) + 6)
 