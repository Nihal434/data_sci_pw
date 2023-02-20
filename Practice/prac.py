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
"""double underscore means private var
   single underscore means protected var
   no underscore means public var"""

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

"""Decorators : decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
                 decorators helps when we have to do repeated work"""
# def test2(func):
#     print("start")
#     func()
#     print("End")
# @test2
# def test1():
#     print(3+4)

# t1 = test1()
# t2 = test2(test1) or we can use @name of funct this method is known as decorator
"""eg 2 decorators"""
# import time
# def timer_test(func):
#     def timer_test():
#         start  = time.time()
#         func()
#         end = time.time()
#         print(f'start time {start}')
#         print(f'end time {end}')
#         print(f'time complexity {end-start}')
#     return timer_test

# @timer_test
# def test():
#     print("Task addition : ",10+29)
# t1 = test()

# @timer_test
# def test1():
#     print("task multiplication : " , 20*40)
# t2 = test1()

# @timer_test
# def test2():
#     print("task divide : ", 20/2)
# t3 = test2()

# @timer_test
# def test3():
#     for i in range(100000000):
#         pass
# t4 = test3()

"""Class method : inbuilt method to pass data to variable directly to 
                  class instead of using init method """

#without class method
# class stud():
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#     def stud_details(self):
#         print(self.name,self.email)

# t1 = stud("123","123@gmail.com")
# print(t1.name)
# print(t1.email)
# t1.stud_details()

#class method
"""class method directly provide var value to class itself instead of giving to 
constructor (class method helps to modify class var directly)
in real world class method is used to modify the class var it can be modify in other way too
but its not a good practice"""
# class car():
#    base_price = 1000 #class var (var which is efined inside a class)
#    def __init__(self,windows,doors,power):
#       self.windows = windows
#       self.doors = doors
#       self.power = power
#    def what_base_price(self):
#       print(f'Base price is {self.base_price}')

#    @classmethod
#    def revise_base_price(cls,inflation):
#       cls.base_price = cls.base_price + cls.base_price*inflation


# car1 = car(4,4,200)
# print(car1.base_price)
# print(car.base_price) #class var can be call directly with class name or instance name
# car.revise_base_price(0.10) #class method can be call with the help of instance(object) or directly with class name
# print(car.base_price)

"""if you want to add external function to class dynamically then class method is used
syntax : class_name.funct_name = classmethod(func_name) 
to delete func inside class use del class_name.func_name"""
# def mileage(cls,mileage):  #external funct
#    print("mileage" , mileage)
# car.mileage = classmethod(mileage) #external funct adding to class
# car.mileage(20)

"""static method :Static methods in Python are extremely similar to python class level methods, the difference being that a static method is bound to a class rather than the objects for that class. 
This means that a static method can be called without an object for that class. """
#instance method
# class stud():
#     def stud_details(self,name,email,number):
#         print(name,email,number)

# test1 = stud()
# test1.stud_details("123","123@gmail.com",123)

# #static method : saves memory from memory which is occupied by repeated func
# class stud():
#     def stud_details(self,name,email,number):
#         print(name,email,number)

#     @staticmethod
#     def mentor_list(men_list):
#         print(men_list)

# test2 = stud()
# test2.mentor_list(["abc",'xyz'])

"""Special method(magic/dunder) : predifined funct"""
# a= 10
# print(a+10)
# print(a.__add__(10)) #addition using special method

"""Property decorators : it exposed the property of decorator to outside """

# class course():
#     def __init__(self,course_price,course_name):
#         self.__course_price = course_price
#         self.course_name = course_name

#     @property   #now price is accessible
#     def price_access(self):
#         return self.__course_price
#     @price_access.setter # setter gives user access to modify the private var
#     def course_price_set(self,price):
#         self.__course_price = price
#     @price_access.deleter #gives access to del private var
#     def  course_price_del(self):
#         del self.__course_price
        

# test = course(400,"abc")
# print(test.course_name)
# print(test._course__course_price)
# print(test.price_access)
# test.course_price_set = 500
# print(test.price_access)
# test.course_price_del
# print(test.price_access)

"""Files"""
