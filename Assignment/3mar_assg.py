"""
Que 1: Name any five plots that we can plot using the Seaborn library. Also, state the uses of each plot.
Ans:
1. Line Plot : A Line Plot Is The Simplest Plot In All Plotting Types, As It Is The Visualization Of A Single Function. 
This Plot Helps Us To See The Relationship Between X-Axis, Y-Axis And It Also Takes Some Parameters Such As Hue, Size, Color, Etc. 

2. Countplot : A Count Plot Is Used To Show The Counts Of Observations In Each Categorical Bin Using Bars.

This Method Is Accepting The Parameters X, Y  Which Take The Name Of A Variable In Data, Hue It Is An Optional Parameter It Helps To Take Column Name For Color Encoding. 
Data Is Also An Optional Parameter That Takes DataFrame, Array, Or List Of Arrays, Dataset For Plotting. 

3. Bar Chart : A Bar Chart Is A Way Of Comparing A Set Of Categorical Data. It Is Better To Convert Continuous Data To Bins Before Plotting. The Bar Chart Displays Data

Using Several Bars, Each Representing A Particular Category. This Method Is Accepting The Parameters X, Y  
Which Take The Name Of A Variable In Data, Hue It Is An Optional Parameter It Helps To Take Column Name For Color Encoding.

4. Pairplot : Pair Plot Creates A Grid Of Axis Such That Each Numeric Variable In Data Will Create A Plot Between Each Other The Y-Axis Across A Single Row And The X-Axis Across A Single Column. 
The Diagonal Plots Are A Univariate Distribution Plot That Helps To Draw The Marginal Distribution Of The Data In Each Column.

5. Scatter Plot : Scatter Plot Is The Same As A Line Plot, In A Line Plot Instead Of Points Being Joined By Line Segments, The Points Are Shown Individually With A Dot, Circle, Or Any Other Shape. The Position Of Each Marker On 
The Horizontal And Vertical Axis Indicates Values For An Individual Data Point. This Plot Is Used To Observe Relationships Between Variables.


"""
"""
Que 2: Load the "fmri" dataset using the load_dataset function of seaborn. Plot a line plot using x =
"timepoint" and y = "signal" for different events and regions.
Ans:
import seaborn as sns
data = sns.load_dataset('fmri')
sns.lineplot(x=data.timepoint,y=data.signal)
"""

"""
Que 3: Load the "titanic" dataset using the load_dataset function of seaborn. Plot two box plots using x =
'pclass', y = 'age' and y = 'fare'.
Ans:
import seaborn as sns
data = sns.load_dataset('titanic')
sns.boxplot(x=data.pclass,y=data.age)
sns.boxplot(x=data.pclass,y=data.fare)
"""
"""
Que 4: Use the "diamonds" dataset from seaborn to plot a histogram for the 'price' column. Use the hue
parameter for the 'cut' column of the diamonds dataset.
Ans:
import seaborn as sns
data = sns.load_dataset('diamonds')
sns.displot(x=data.price , hue = data.cut)

"""
"""
Que 5: Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column
of the iris dataset.
Ans:
import seaborn as sns
data = sns.load_dataset('iris')
sns.pairplot(data,hue= 'species')
"""
"""
Que 6: Use the "flights" dataset from seaborn to plot a heatmap.
Ans:
import seaborn as sns
flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
ax = sns.heatmap(flights)
"""