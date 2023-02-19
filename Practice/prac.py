# lst = [1,2,3,4,5,6,7,8]
# d = {}
# for i in lst:
#     d[i]="apple"
# print(d)

# l = [12,3,4,5,'222','asdasd',324235345,[1,2,3,4,]]
# def t(a):
#     n = []
#     for i in a:
#         if type(i) == int:
#             n.append(i)
#         elif type(i)==list:
#             for j in i:
#                 n.append(j)
#         else:
#             pass
    
#     return n

# print(t(l))

"""Reduce function"""

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# product = reduce(lambda x, y: x*y, numbers)

# print(product)

"""Filter function"""
# numbers = [1, 2, 3, 4, 5]

# even_numbers = filter(lambda x: x%2 == 0, numbers)

# print(list(even_numbers))

"""OOPS"""

# class test():
#     def add(self,a,b):
#         return a+b
#     def sub(self):
#         print("Hello")

# test1 = test()
# print(test1.add(2,3))
# test1.sub(2,3)     #call the method differently

"""1.Constructor takes input and gives to class
   2.when we define constructor we have to pass the argument,
   when we call the class (below example) varible defined in 
   constructor can be accessed by all method which is defined 
   under the class
   3.when we dont define costructor and pass variable directly 
   to method that variable is only accessed by that method(above example)"""

# class test():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a+self.b

# test1=test(2,3)
# print(test1.add())

"""Polymorphism  : same method shows diffrent behaviour w.r.t class"""

# def add(a,b):
#     return a+b

# print(add(2,3)) #same method adding two int

# print(add("hello","boys"))   #same method performs conctenation


   
#eg 2

# class data_sci():
#     def met(self):
#         print("this is my method 1")

# class web_dev():
#     def met(self):
#         print("this is my method 2")

# def parser(pars):
#     for i in pars:
#         i.met()

# mt1 = data_sci()
# mt2 = web_dev()
# par = [mt1,mt2]
# a= parser(par)
# print(a)

"""Encapsulation : Prevents direct modification of data
for that you have to make variable inside class private which
is done by double underscore before var declaration eg self.__var 
after making it private no one from outside can access it or modify it
to give access of modification you have to define seprate method 
for modification"""

# class test():
#     def __init__(self,a,b):
#         self.a  = a
#         self.b = b
# test1 = test(10,20)
# print(test1.a) #accessing the var a val
# test1.a=40 #modifying the value of var a
# print(test1.a)  #accessing the modified value

#hence noone from outside should able to modify variable for that purose we uses encapsulation

# class car():
#     def __init__(self,name,model,speed):
#         self.__name = name     #__(double underscore) added to make var private
#         self.__model = model
#         self.__speed = speed
    
#     def get_speed(self):
#         return self.__speed
        
# car1 = car("maruti",1,200)  
# #print(car1.speed) #with this speed cannot be accessed bcoz it is private
# """to get access of speed you have define seperate method in class for getting access"""
# print(car1.get_speed()) #now you can access speed likewise to modify var you have define seprate method

"""eg 2 encapsulation """
# class bank():
#     def __init__(self,balance):
#         self.__balance = balance

#     def deposite(self,amount):
#         self.__balance = self.__balance+amount
    
#     def withdraw(self,amount):
#         if self.__balance>=amount:
#             self.__balance = self.__balance-amount
#             return True
#         else:
#             return False
#     def get_balance(self):
#         return self.__balance
    
# obj_bank_acc = bank(1000)
# print(obj_bank_acc.get_balance())
# obj_bank_acc.deposite(1000)
# print(obj_bank_acc.get_balance())
# obj_bank_acc.withdraw(500)
# print(obj_bank_acc.get_balance())

"""Inheritance : inheriting or envoking property of parent """

# class parent():
#     def test_parent(self):
#         print("parent class")

# class child(parent):
#     pass
# child_obj = child()
# child_obj.test_parent()

"""Multi-level inheritance : class1->class2->class3 ---class n """

# class class1():
#     def test_cls1(self):
#         print("from class 1")

# class class2(class1):
#     def test_cls2(self):
#         print("from cls 2")

# class class3(class2):
#     def test_cls3(self):
#         print("from cls 3")
# obj_class3 = class3()
# obj_class3.test_cls1()

"""Multiple inhe : inheriting prop from diff class"""
# class class1():
#     def test_cls1(self):
#         print("from cls1")
# class class2():
#     def test_cls2(self):
#         print("from cls2")
# class class3(class1,class2):
#     pass
# obj_class3 = class3()
# obj_class3.test_cls1()
# obj_class3.test_cls2()