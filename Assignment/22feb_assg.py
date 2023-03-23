"""Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.
    Ans :
    import pandas as pd
    a = [4,8,15,16,23,42]
    var = pd.Series(a)
    print(var)
"""

"""Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
variable print it.
    Ans:
    import pandas as pd
    list_ = ['a','b','c','d','e','f','g','h','i','j']
    lst = pd.Series(list_)
    print(lst)
"""

"""Q3. Create a Pandas DataFrame that contains the following data:
    Ans : 
    import pandas as pd
    data = [['Alice',25,'Female'],['Bob',30,'Male'],['Clarie',27,'Female']]
    df = pd.DataFrame(data,columns=['Name','Age','Gender'])
    df
"""
"""Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.
    Ans:
    Pandas DataFrame:
    The Pandas DataFrame is a two-dimensional data structure composed of columns and rows. 
    You can think of the DataFrame as similar to a CSV or relational database table.
    Pandas Series:
    The Pandas Series data structure is a one-dimensional labelled array. 
    It is the primary building block for a DataFrame, making up its rows and columns.
    following are the example which differentiate pandas dat frame and pandas series
    dataframe eg : 
    import pandas as pd
    data = [['Alice',25,'Female'],['Bob',30,'Male'],['Clarie',27,'Female']]
    df = pd.DataFrame(data,columns=['Name','Age','Gender'])
    here df is a two dimensional like a csv file
    series eg:
    import pandas as pd
    list_ = ['a','b','c','d','e','f','g','h','i','j']
    lst = pd.Series(list_)
    here lst ia a one dimensional entity


"""

"""Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
you give an example of when you might use one of these functions?
    Ans:
    1. read_csv()
    This is one of the most crucial pandas methods in Python. 
    read_csv() function helps read a comma-separated values (csv) file into a Pandas DataFrame.
    2. head()
    head(n) is used to return the first n rows of a dataset. 
    By default, df.head() will return the first 5 rows of the DataFrame.
    3. tail()
    tail(n) is used to return the last n rows of a dataset. 
    By default, df.tail() will return the last 5 rows of the DataFrame.
"""

"""Q6. Which of the following is mutable in nature Series, DataFrame, Panel?
    Ans: dataframe is mutable in nature
"""
"""Q7. Create a DataFrame using multiple Series. Explain with an example.
    Ans : 
    import pandas as pd
    course = pd.Series(['Data Science','DSA','Full Stack'], name = 'Courses')
    fees = pd.Series([1000,2000,3000],name = 'Fees')
    discount = pd.Series([100,200,300],name = "Discount")
    df = pd.concat([course,fees,discount],axis=1)
    df

    
"""