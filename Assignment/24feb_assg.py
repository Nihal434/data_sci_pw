"""
Q1. List any five functions of the pandas library with execution.

Ans :

    1.read_csv():
    It used to read data from csv file

    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

    2. Head and Tail :
    Once we read a dataset into a pandas data frame, we want to take a look at it to get an overview. 
    The simplest way is to display some rows. Head and tail allow us to display rows from the top of bottom of data frame, respectively.

    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    df.head()
    df.tail()

    3. DataFrame.info( )
    Pandas dataframe.info() function is used to get a concise summary of the dataframe. 
    It comes really handy when doing exploratory analysis of the data. To get a quick overview of the dataset we use the dataframe.info() function.

    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    df.info()

    4.Dtypes:
    Dtypes shows the data type of each column.
    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    df.Dtypes()

    5. describe( )
    If there’s one thing you do over and over again in the process of exploratory data analysis — 
    that’s performing a statistical summary for every (or almost every) attribute.
    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    df.describe()



"""

"""
Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
DataFrame with a new index that starts from 1 and increments by 2 for each row.
Ans:
    student_dict = {'A': ['Joe', 'Nat', 'Harry'], 'B': [20, 21, 19], 'C': [85.10, 77.80, 91.54]}
    df = pd.DataFrame(student_dict,index=['1','3','5'])
    df

"""
"""
Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
function should print the sum to the console.
For example, if the 'Values' column of df contains the values [10, 20, 30, 40, 50], your function should
calculate and print the sum of the first three values, which is 60.

Ans:
    lst = [10,20,30,40,50]
    df = pd.DataFrame(lst,columns=['value'])
    sum = 0
    for i in range(0,3):
        sum = sum+df.loc[i,'value']
    print(sum)
"""

"""
Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
'Word_Count' that contains the number of words in each row of the 'Text' column.

Ans: 
    text = ['abc as as','asdas asa','sdasdas sdca as as sa']
    df = pd.DataFrame(text,columns=['Text'])
    df["Word_Count"] = df["text"].apply(lambda n: len(n.split()))
    df
"""
"""
Q5. How are DataFrame.size() and DataFrame.shape() different?
Ans :
    Size and shape of a dataframe in pandas python: Size of a dataframe is the number of fields in the dataframe which is nothing but number of rows * number of columns. 
    Shape of a dataframe gets the number of rows and number of columns of the dataframe.
"""

"""
Q6. Which function of pandas do we use to read an excel file?

Ans: We can use the pandas module read_excel() function to read the excel file data into a DataFrame object.
"""
"""
Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
addresses in the format 'username@domain.com'. Write a Python function that creates a new column
'Username' in df that contains only the username part of each email address.

Ans: 
    email = ['john.doe@domain.com','username2@domain.com','username3@domain.com','username4@domain.com']
    df = pd.DataFrame(email,columns= ['Email'])
    df['Username'] = df['Email'].str.split('@').str[0]
    df
"""

"""
Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
function should return a new DataFrame that contains only the selected rows.

Ans: 
    lst = [[3,5,1],[8,2,7],[6,9,4],[2,3,5],[9,1,2]]
    df= pd.DataFrame(lst,columns=['A','B','C'])
    df[(df['A']>5)&(df['B']<10)]

"""

"""
Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
median, and standard deviation of the values in the 'Values' column.

Ans:
    val = [10,20,30,40,2]
    df= pd.DataFrame(val,columns=['Value'])
    df.describe()
"""

"""
Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
should include the current day.

Ans: 
    val = [['1-1-2001',100],['2-1-2001',200],['3-1-2001',300],['4-1-2001',400],['5-1-2001',500],['6-1-2001',600],['7-1-2001',700],['8-1-2001',800],['9-1-2001',900],['10-1-2001',1000]]
    df = pd.DataFrame(val,columns=['Date','Sales'])
    df['MovingAverage'] = df['Sales'].rolling(7).mean()
    df.dropna(inplace=True)
    df

"""

"""
Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
Monday, Tuesday) corresponding to each date in the 'Date' column.

Ans:
    df = pd.DataFrame({'Dates':['2023-01-01','2023-01-02','2023-01-03','2023-01-04','2023-01-05']})
    df['Dates'] = pd.to_datetime(df['Dates'])
    df['Weekday'] = df['Dates'].dt.day_name()
    df


"""

"""
Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
function to select all rows where the date is between '2023-01-01' and '2023-01-31'.

Ans:
    def select_dates_between(df):
        start_date = '2023-01-01'
        end_date = '2023-01-31'
        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        selected_df = df.loc[mask]
        return selected_df

    select_dates_between(dates)

"""
"""
Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to
be imported?

Ans: import pandas as pd

"""