# Python is case sensitive
#if prince = 8 and Prince = 6, here both are different veriable


#List

# a list is a built-in data structure that represents a collection of items or elements.
# It is an ordered sequence of objects, where each element can be of any data type such as numbers, strings, or even other complex objects.

l1 = [3, 54,  4, 67 ,67, 778, 8976, "Prince"]

print(type(l1))
print(l1)

#we cannot  modify string but we can modify list.

l1.remove("Prince") #use to remove any element from list
print(l1)

print(l1.count(67)) #use to count no. of element present in list

l1.sort()
print(l1)

l1.pop() #use to pop last element
print(l1)

l1.append(105) #use to add element in list
print(l1)

l1.sort() #use to sort element
print(l1)

# l1.clear() #use to clear whole list

l1.extend([89, 73, 23])
print(l1)

print(l1.index(778))
