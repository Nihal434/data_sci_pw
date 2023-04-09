"""
Consider following code to answer further questions:
import pandas as pd
course_name = [‘Data Science’, ‘Machine Learning’, ‘Big Data’, ‘Data Engineer’]
duration = [2,3,6,4]
df = pd.DataFrame(data = {‘course_name’ : course_name, ‘duration’ : duration})
Q1. Write a code to print the data present in the second row of the dataframe, df.

Ans : 

    df.loc[1]
"""

"""
Q2. What is the difference between the functions loc and iloc in pandas.DataFrame?
Ans:
    Loc and iloc are two functions in Pandas that are used to slice a data set in a Pandas DataFrame. 
    The function . loc is typically used for label indexing and can access multiple columns, while . iloc is used for integer indexing

"""

"""
Q3. Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df
then find the output for both new_df.loc[2] and new_df.iloc[2].
Ans:
    new_df = df.reindex([3,0,1,2])
    new_df.loc[2]
    new_df.iloc[2]
    The difference is loc returns a row who have index as 2 while iloc returns a row which is at second 

"""

"""
import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)
Q4. Write a code to find the following statistical measurements for the above dataframe df1:
(i) mean of each and every column present in the dataframe.

Ans :

    df1.mean()
    or
    df1.mean(axis=0)

(ii) standard deviation of column, ‘column_2’

Ans:
    df1['column_2].std()

"""

"""
Q5. Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
mean of column, column_2.
If you are getting errors in executing it then explain why.

Ans:
    df1.loc[2] = 'abcd'
    df1['column_2'].mean()
    TypeError: unsupported operand type(s) for +: 'float' and 'str'
"""

"""
Q6. What do you understand about the windows function in pandas and list the types of windows
functions?

Ans:
    Pandas Window functions are functions where the input values are taken from a “window” of one or more rows in a series or a table and calculation is performed over them.
"""

"""
Q7. Write a code to print only the current month and year at the time of answering this question.

Ans:
    df_date = pd.DataFrame({'date':['2023-04-06']})
    df_date['updated_dates'] = pd.to_datetime(df_date['date'])
    1].
    df_date['month'] = df_date['updated_dates'].dt.month
    df_date['year'] = df_date['updated_dates'].dt.year
    2].
    year = df_date['updated_dates'].dt.year
    month = df_date['updated_dates'].dt.month
    print(month,year)
"""

"""
Q8. Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and
calculates the difference between them in days, hours, and minutes using Pandas time delta. The
program should prompt the user to enter the dates and display the result.

Ans:
    import pandas as pd

    # prompt user to enter two dates
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")

    # convert input strings to datetime objects
    date1 = pd.to_datetime(date1)
    date2 = pd.to_datetime(date2)

    # calculate difference between dates
    delta = date2 - date1

    # extract days, hours, and minutes from delta
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60

    # display result
    print(f"The difference between {date1.date()} and {date2.date()} is {days} days, {hours} hours, and {minutes} minutes.")


"""

"""
Write a Python program that reads a CSV file containing categorical data and converts a specified
column to a categorical data type. The program should prompt the user to enter the file path, column
name, and category order, and then display the sorted data.

Ans:

    import pandas as pd
    #taking csv file input
    path = input('Enter file path : ')

    #reading the csv file
    df = pd.read_csv(path)

    #taking column as input
    clm = input('Enter a column name : ')

    #converting column datatype to category
    df[clm] = df[clm].astype('category')

"""

"""
Q10. Write a Python program that reads a CSV file containing sales data for different products and
visualizes the data using a stacked bar chart to show the sales of each product category over time. The
program should prompt the user to enter the file path and display the chart.

Ans:
    import pandas as pd
    import matplotlib as plt

    path = path = input('Enter file path : ')

    #reading the csv file
    df = pd.read_csv(path)

    df.plot()
"""

"""
Q11. You are given a CSV file containing student data that includes the student ID and their test score. Write
a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and
displays the results in a table.

Ans:
    import pandas as pd
    #taking csv file input
    path = input('Enter file path : ')

    #reading the csv file
    df = pd.read_csv(path)

    mean = df['Test Score'].mean()
    median = df['Test Score'].median()
    mode = df['Test Score'].mode()

    print(df)
    print(f'Mean {mean}')
    print(f'Median {median}')
    print(f'Mode {mode}')

"""