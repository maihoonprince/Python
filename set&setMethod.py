
#set is collection of well defined elements

#a set is a built-in data structure that represents an unordered collection of unique elements.
#Sets are used to store distinct values and perform mathematical set operations like union, intersection, difference, and more.

#Sets are defined using curly braces {} or the set() function.

a1 = {2, 54, 4, 34, 56, 76, 65}
a2 = {3, 54, 43, 76, 56, 9}

# a1.clear()
print(a1)
print(a2)

print(a1.pop())
print(a1)

print(a1.union(a2))

a3 = a1.union(a2)
print(a3)

a4 = a1.intersection(a2)
print(a4)