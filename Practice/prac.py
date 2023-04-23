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

"""Decorators : decorator is a function that takes another function and extends the behavior of the later function without explicitly modifying it.
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
#    base_price = 1000 #class var (var which is defined inside a class)
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

"""Files""" #if file code does not run here go for colab
"""text file"""
# f = open("test.txt",'w') #to create a text file, w is a type of file you can use other check by pressing tab

# f.write("hello") #writing something in blabk file
# f.close() #after writing in file you have to use close command in order to execute

# data.seek(place)  #seek use to set thecursor at any place
"""json file"""
# data = {
#     "name":'123',
#     'email':'123@gmail.com',
#     'contact_no.':1234,
#     'subject':['abc','pqr','xyz']

# }

# import json #adding data to json file
# with open('test1.json','w') as f:
#     json.dump(data,f)

# with open('test1.json','r') as f: #reading data from json file
#   data1 = json.load(f)

"""csv = comma seperated value in csv file data must be seperated by comma"""
#writing comma seperated data in csv file where 1st row will be name of coulmns


# data = [['name','email','number'],
#         ['abc','abc@gmail.com',1234],
#         ['pqr','pqr2gmail.com',5678]
#         ]
# import csv
# with open('test3.csv','w') as f:
#    w = csv.writer(f)
#    for i in data:
#       w.writerow(i)

#reading data from csv

# with open('test3.csv','r') as f:
#     read = csv.reader(f)
#     for i in read:print(i)

"""binary file (image etc)"""
#opening binary file
# with open('test4.bin','wb') as f:
#     f.write(b'\x01\x02\x03')

# #reading bin value
# with open('test4.bin','rb') as f:
#     print(f.read())

"""Logging and debugger : """
# import logging
# logging.basicConfig(filename= 'test.log',level = logging.INFO)

"""module : check example in pw file"""
# from Practice import prac2
# def prac():
#     print("hello from file prac")

"""Exception handling : """

# f = open('test.txt','r') #after throwing error by this line remaining lines will not executed
#so of you dont want to stop your remaing lines execution take take suspicious line inside try and except
# try:
#     f = open('test.txt','r')
# except Exception as e:
#     print('issue with my code',e)
    
# print('this is my file')

# try:
#     f = open('test.txt','w')
#     f.write('this is msg')
   
# except Exception as e:
#     print('issue with my code',e)

# else:
#     f.close()
#     print('this block will execute once try will execute itself without exception')
    
# try:
#     f = open('test1.txt','r')
#     f.write('hello')
# finally:
#     print('this will always execute') #anything inside finally always execute while try block thorows error or not
"""we can execute all thing together too"""
# try:
#     f = open('test.txt','w')
#     f.write('this is msg')
   
# except Exception as e:
#     print('issue with my code',e)

# else:
#     f.close()
#     print('this block will execute once try will execute itself without exception')

# finally:
#     print('this will always execute')

"""Custom Exception handling : exception like user entering negative age"""
# class validateage(Exception):
#     def __init__(self,msg):
#         self.msg = msg

# def validate_age(age):
#     if age<0:
#         raise validateage("age should not less than zero")
#     elif age>200:
#         raise validateage("age is too high")
#     else:
#         print('age is valid')

# try:
#     age = int(input('enter age : '))
#     validate_age(age)
# except validateage as e:
#     print(e)

"""genral exception"""
# try:
#     a= 10
#     10/0
# except ZeroDivisionError as e:
#     print(e)

# # try:
# #     int('sudh')
# # except TypeError as e:
# #     print(e)

# try:
#     import hello
# except ImportError as e:
#     print(e)
# try:
#     'heel'.test()
# except AttributeError as e:
#     print(e)

# try:
#     l=[1,2,3,4]
#     l[10]
# except IndexError as e:
#     print(e)

"""Multithreading : 
Multithreading allows the execution of multiple parts of a program at the same time. These parts are known as threads and are lightweight processes available within the process. 
So multithreading leads to maximum utilization of the CPU by multitasking."""
# import threading
# def test(id):
#     print('this is my test id %d' %id)
# # test(10)
# # test(20)
# # test(30)

# #following code snippet also gives the same result which would be given after 3 function call

# thred = [threading.Thread(target=test,args = (i,)) for i in [10,20,30]]
# thred 
# for i in thred:
#     i.start()

"""importing data from file"""
# import urllib.request
# import threading
# def file_download(url,filename):
#     urllib.request.urlretrieve(url,filename)

# #file_download('https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt','test.txt')
# url_list = [
#     'https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt',
#     'https://raw.githubusercontent.com/itsfoss/text-files/master/sherlock.txt',
#     'https://raw.githubusercontent.com/itsfoss/text-files/master/sample_log_file.txt'
# ]

# # print(url_list)
# data_file_list = ['data1.txt','data2.txt','data3.txt']
# thread1= [threading.Thread(target= file_download , args= (url_list[i],data_file_list[i])) for i in range(len(url_list))]
# # threading.Thread(target=file_download, args = (url_list[i],data_file_list[i]) for i in range(len(url_list)))
# for t in thread1:
#     t.start() 

# def test2(x):
#     for i in range(10):
#         print('test1 printing value of x %d and printing value of i %d ' %(x,i))

# # test2(10)
# """Now for exectuing same func for diffrent parameter will take so long
# instead of this using threading we can run same prog consecutively in efficient manner"""

# thread2 = [threading.Thread(target=test2, args=(i,)) for i in [100,20,10,30]]
# for t in thread2:
#     t.start()

""" Multiprocessing :  

"""
#import multiprocessing
#eg 1
# def test():
#     print('this is multi programming func')

# if __name__ == "__main__": #main method which act as oarent
#     m=multiprocessing.Process(target = test)
#     print('this is my main prog')
#     m.start() #to start the multiprocessing
#     m.join() #to join diff multiprocess

#eg2
# def sqr(n):
#     return n**2

# if __name__ == '__main__' :
#     with multiprocessing.Pool(processes = 5) as pool:
#         out = pool.map(sqr,[2,3,4,5,6])
#         print(out)

#eg3 : queue 
# def producer(q):
#     for i in ['a','b','c','d']:
#         q.put(i)

# def consumer(q):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print(item)

# if __name__ == '__main__':
#     queue = multiprocessing.Queue()
#     m1  = multiprocessing.Process(target = producer,args = (queue,)) #enqueue
#     m2 = multiprocessing.Process(target = consumer,args = (queue,))  #dequeue
#     m1.start()
#     m2.start()
#     queue.put('xyz')
#     m1.join()
#     m2.join()

# video have one more great eg which is at last

"""Database : SQL """ 

# import mysql.connector
# # import mysql.connector
# #create user 'user'@'%' identified by 'password'
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="abc",
#   password="password"
# )
# print(mydb)
# mycursor = mydb.cursor()
# #till these everything will be common above syntax
# mycursor.execute("SHOW DATABASES") #itvwill show current db avaiable
# for x in mycursor:
#   print(x)


#syntax to create new table using python
#1 create .py file and write following code

# import mysql.connector
# # import mysql.connector
# #create user 'user'@'%' identified by 'password'
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="abc",
#   password="password"
# )
# mycursor = mydb.cursor()
# mycursor.execute('CREATE DATABASE if not exists test1')
# mycursor.execute('CREATE TABLE  if not exists test1.test_table (c1 INT , c2 VARCHAR(50), c3 INT, c4 FLOAT);')
#aboce line is to create table inside db test1
# mydb.close() #mandatory to write close command

"""Connecting with mongodb
1. create account(free)
2.create server
3.copy client prog and paste in compiler
4. change password from url to which you have set in mongo server"""

# import pymongo

# client = pymongo.MongoClient("mongodb+srv://username:<Password123>@cluster0.rja1xrb.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# connection have done with db
#check download

"""web api : it is a subset of api ,application programming interface using https is web api
data send and receive through http protocol  

reat and soap archi : 
rest : representational state transfer used http protocol
soap : simple object access protocol use tcp,smtp prtocol

both used to create api


"""

"""linked list"""
# class node():
#     def __init__(self,data = None):
#         self.data = data
#         self.next = None

# class llist():
#     def __init__(self):
#         self.head = None

#     def detect(self):
#         slow = self.head
#         fast = self.head
#         flag = 0
#         while (slow and fast and fast.next):
#             if slow ==fast and flag!=0:
#                 count=1
#                 slow = slow.next
#                 while(slow!=fast):
#                     slow = slow.next
#                     count+=1
#                 print(count)
#                 break
#             slow = slow.next
#             fast = fast.next.next
#             flag = 1
#             # print(count)
#             if slow == fast:
#                 print("loop")
#                 break
   
#    #  def printlist(self):
#    #      printval = self.head
#    #      while printval is not None:
#    #          print(printval.data)
#    #          printval = printval.next

    
   
   




# list1 = llist()
# list1.head = node("mon")
# e2 = node('tue')
# e3 = node('wed')
# list1.head.next = e2
# e2.next = e3
# e3.next = list1.head
# list1.detect()

# class node():
#     def __init__(self,data = None):
#         self.data = data
#         self.next = None
    
# class llist():
#     def __init__(self):
#         self.head = None

#     def detect(self):
#         slow = self.head
#         fast = self.head
#         while slow!=fast :
#             print('hello')
#             slow = slow.next
#             fast = fast.next.next

#     # def printlist(self):
#     #     printval = self.head
#     #     while printval!=None:
#     #         print(printval.data)
#     #         printval = printval.next



# list1 = llist()
# list1.head = node("1")
# e2 = node('2')
# list1.head.next = e2
# e3 = node('3')
# e2.next = e3
# e3.next = e2

# list1.detect()


"""Pandas : run on lab
Why Use Pandas? Pandas allows us to analyze big data and make conclusions based on statistical theories. Pandas can clean messy data sets,
 and make them readable and relevant. Relevant data is very important in data science."""

import pandas as pd  
#we can use anything as a alias in this case we have taken pd
ab=pd.read_csv('services.csv') #reading a csv file we can read any structured file
#pandas by default consider first row as a column name or header
print(ab)