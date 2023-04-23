"""
Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code
to print the data types of both the variables.
Ans : 
    List is used to collect items that usually consist of elements of multiple data types. 
    An array is also a vital component that collects several items of the same data type. 
    List cannot manage arithmetic operations. Array can manage arithmetic operations.
    list example:
    sample_list = [1,"hello",['a','e']]
    print(sample_list) 

    array_list example :
    import array
    sample_array = array.array('i', [1, 2, 3]) 
    for i in sample_array:
        print(i)
"""

"""
Q2. Write a code to print the data type of each and every element of both the variables list_ and
arra_list.
Ans : 

    list :
    sample_list = [1,"hello",['a','e']]
    for i in sample_list:
        print(i) 

    array list :
    import array
    sample_array = array.array('i', [1, 2, 3]) 
    for i in sample_array:
        print(i)

"""

"""
Q3. Considering the following changes in the variable, array_list:
array_list = np.array(object = list_, dtype = int)
Will there be any difference in the data type of the elements present in both the variables, list_ and
arra_list? If so then print the data types of each and every element present in both the variables, list_
and arra_list.

Ans:
    List :
    sample_list = [1,"hello",['a','e']]
    for i in sample_list:
        print(type(i))

    array_list :
    import array
    sample_array = array.array('i', [1, 2, 3]) 
    for i in sample_array:
        print(type(i))


"""
"""
Q4. Write a code to find the following characteristics of variable, num_array:
(i) shape
(ii) size
Ans:
1] 
    import numpy as np
    num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
    num_array = np.array(object = num_list)
    print(num_array.shape)
2]
    import numpy as np
    num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
    num_array = np.array(object = num_list)
    print(num_array.size)
"""
"""
Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array
creation function.
Ans :
    import numpy as np
    print(np.zeros((3,3)))

"""
"""
Q6. Create an identity matrix of shape (5,5) using numpy functions?
Ans:
    import numpy as np
    print(np.eye(5))
"""


