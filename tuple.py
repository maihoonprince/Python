# a tuple is another built-in data structure that is similar to a list but with some key differences.
# Like a list, a tuple is an ordered sequence of elements, but unlike lists, tuples are immutable.

t = (1, 34, 55, 65, 55,3, 2)

print(t.count(55))
print(t.index(65))

#it will show error if we try to change in tuple just like string...
#t[0] = 89 ----> it will show error

