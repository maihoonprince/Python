# a string is a sequence of characters enclosed within single quotes ('') or double quotes ("").
# Strings are immutable, which means that once created, their content cannot be changed.

name = 'prince'
print(name)
print(name[0:3])
print(name[1:4])
print(name[4:5])
#print(name[a:b])  <---- Output start from a and gp all the way b-1.

#string methods

print(name.capitalize())
print(name.upper())
print(name.count("r"))
print(name.isalnum())

# 1. str.upper(): Converts all characters in the string to uppercase.
# 2. str.lower(): Converts all characters in the string to lowercase.
# 3. str.capitalize(): Capitalizes the first character of the string and converts the rest to lowercase.
# etc many more https://docs.python.org/3/library/stdtypes.html#string-methods