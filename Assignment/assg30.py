"""1. Write a program to accept percentage from the user and display the grade according to the following 
criteria: 
Marks            Grade 
>90               A 
>80 and <=90      B 
>=60 and <=80     C 
below 60          D 


Ans :

a= int(input('Enter your mark : ' ))
if a>90:
    print('Your grade is "A"')
elif a>80 and a<=90:
    print('Your grade is "B"')
elif a>=60 and a<=80:
    print('Your grade is "C"')
else :
    print('Your grade is "D"')

"""

"""
2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the 
following criteria: 
Tax    Cost Price(in Rs)
15%     >100000
10%     50000 and <= 100000 
5%      <= 50000

Ans :

 
a=int(input("Enter the cost price of a bike : "))
if a>100000:
    print("You have to pay 15% tax")
elif a>50000 and a<= 100000:
    print("You have to pay 10% tax")
else:
    print("You have to pay 5% tax")

"""

"""
3. Accept any city from the user and display monuments of that city. 
City        Monument
Delhi       Red Fort
Agra        Taj Mahal 
Jaipur      Jal Mahal 

Ans:


a= input("Enter city name :")
if a.capitalize() == 'Delhi':
    print(f'Monument in {a} is Red fort ')
elif a.capitalize()=='Agra':
    print(f'Monument in {a} is Taj Mahal ')
elif a.capitalize() =='Jaipur':
    print(f'Monument in {a} is Jal Mahal ')
else:
    print("Please enter a valid city")

"""

"""
4. Check how many times a given number can be divided by 3 before it is less than or equal to 10.

Ans : 

a= int(input('Enter a number : '))
count = 0
if a>=10:
    while a>=10:
        a=a//3
        # print(a)
        count+=1
    print(f'Given number can be divided by 3 before it is less than or equal to 10 is {count}')
else:
    print("please enter a number greater than or equal to 10")

"""

"""
5. Why and When to Use while Loop in Python give a detailed description with example

Ans: Python while loop is used to run a block code until a certain condition is met
example:
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1
"""

"""
6. Use nested while loop to print 3 different pattern. 


# pattern 1 :

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')



# Pattern 2 :

rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
    
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1


# Pattern 3:
n=5 
i=1;j=0
while(i<=n):
    while(j<=i-1):
        print("* ",end="")
        j+=1
    print("\r")
    j=0;i+=1

"""
"""
7. Reverse a while loop to display numbers from 10 to 1.
8. Reverse a while loop to display numbers from 10 to 1

Ans :


i = 10
while i > 0:
    print(i)
    i = i - 1

"""




    


