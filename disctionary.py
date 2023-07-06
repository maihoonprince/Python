#a dictionary is a built-in data structure that represents a collection of key-value pairs.
# Dictionaries are also known as associative arrays or hash maps in other programming languages.
# They provide an efficient way to store and retrieve data based on a unique key.

#Dictionaries are defined using curly braces {} and separating key-value pairs with colons ":" .

dict1 = {}  #method to create empty dictionary
a = set() #method to create empty set

print(type(dict1))
print(type(a))

b = {"good": "Something Pleasant", "fetch": "to bring", "1": "The number 1"}
marks = {"prince": "90", "lalit": "89", "som": "56", "vivek": "12"}

print(b["fetch"])
print(marks["prince"])

#Dictionary is mutable(we can change in dict.)
marks["priyanka"] = 34
print(marks)

#Dictionary Method's
print(marks.get("priyanks chopra"))
print(marks.get("priyanka"))
print(marks.keys())
print(marks.items())
print(marks.values())
print(b.keys())

