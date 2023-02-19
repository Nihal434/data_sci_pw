"""Q1. What are the characteristics of the tuples? Is tuple immutable?
    
    Ans : Tuples contains a sequence of elements. 
    The elements can be types, expressions, or aliases. 
    The number and elements of a tuple are fixed at compile time and they cannot be changed at run time. 
    Tuples have characteristics of both structs and arrays.
    tuples are immutable in nature
"""

"""
Q2. What are the two tuple methods in python? Give an example of each method. Give a reason why
tuples have only two in-built methods as compared to Lists.

Ans : There are only two tuple methods count() and index() that a tuple object can call.

tup = (1,2,3,4,5,5)
print(tup.count(5))
print(tup.index(2))

tuples only have two inbuilt method because tuples are immutable, 
meaning you cannot change their contents after they are created. The length of tuples is also fixed.

"""

"""
Q3. Which collection datatypes in python do not allow duplicate items? Write a code using a set to remove
duplicates from the given list.
Ans : Set datatype in python do not allow duplicates

l1 = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
print(set(l1))
"""
"""
Q4. Explain the difference between the union() and update() methods for a set. Give an example of
each method.
Ans :  difference is that where union() method create and return a new set, containing all the elements ( distinct ) present in all the iterables, 
update() method updates the set on which this method is called with all the distinct elements present in all the iterables.

A = {1,2,3,4,5}
B = {4,5,6,7,8,9}
S = A.union(B)
A.update(B)
print('A : ',A)
print('B : ',B)
print('A Union B : ',S)
print('A Update B : ',A)

"""

"""
Q5. What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered.
Ans : Dictionary is a collection which is ordered , changeable, and does not allow duplicates
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
Dictionary is ordered
"""

"""
Q6. Can we create a nested dictionary? If so, please give an example by creating a simple one-level
nested dictionary.
Ans : Yes we can create nested dictionary

family = {
  "child1" : {
    "name" : "Ram",
    "year" : 2004
  },
  "child2" : {
    "name" : "Shyam",
    "year" : 2007
  },
  "child3" : {
    "name" : "Ghanshyam",
    "year" : 2006
  }
}
print(family)
"""