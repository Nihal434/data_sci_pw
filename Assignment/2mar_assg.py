"""
Q1: What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of
Matplotlib.
Ans:
    Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
    Matplotlib makes easy things easy and hard things possible.
    plot(x, y)
    scatter(x, y)
    bar(x, height)
    stem(x, y)
    step(x, y)
"""

"""
Q2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
plot a scatter plot.
import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))

Ans:
    A scatter plot is a visual representation of how two variables relate to each other. 
    You can use scatter plots to explore the relationship between two variables, for example by looking for any correlation between them.
    plt.scatter(x,y)
    plt.xlabel("this is X axis")
    plt.ylabel("this is Y axis")
    plt.title("Scatter plot")
"""
"""
Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.
Use the following data:
import numpy as np
For line 1: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([0, 100, 200, 300, 400, 500])
For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])

Ans :
x = np.array([0, 1, 2, 3, 4, 5]) 
y = np.array([0, 100, 200, 300, 400, 500])
plt.subplot(2, 2, 1)
plt.plot(x,y)
x = np.array([0, 1, 2, 3, 4, 5]) 
y = np.array([50, 20, 40, 20, 60, 70])
plt.subplot(2, 2, 2)
plt.plot(x,y)
x = np.array([0, 1, 2, 3, 4, 5]) 
y = np.array([10, 20, 30, 40, 50, 60])
plt.subplot(2, 2, 3)
plt.plot(x,y)
x = np.array([0, 1, 2, 3, 4, 5]) 
y = np.array([200, 350, 250, 550, 450, 150])
plt.subplot(2, 2, 4)
plt.plot(x,y)
plt.show()
"""
"""
Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.
import numpy as np
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
Ans :
    The purpose of a bar graph is to convey relational information quickly in a visual manner. 
    The bars display the value for a particular category of data. The vertical axis on the left or right side of the bar graph is called the y-axis. 
    The horizontal axis at the bottom of a bar graph is called the x-axis
    company = np.array(["Apple", "Microsoft", "Google", "AMD"])
    profit = np.array([3000, 8000, 1000, 10000])
    plt.bar(company,profit)
    plt.xlabel("Name of company")
    plt.ylabel("profit of company")
    plt.show()
"""

"""
Q5: What is a box plot? Why is it used? Using the following data plot a box plot.
box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
Ans:
Box plots are used to show distributions of numeric data values, especially when you want to compare them between multiple groups. 
They are built to provide high-level information at a glance, 
offering general information about a group of data's symmetry, skew, variance, and outliers.

box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
fig = plt.figure(figsize =(10, 7))
ax = fig.add_axes([0, 0, 1, 1])
bp = ax.boxplot([box1,box2])
plt.show()
"""