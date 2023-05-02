"""
Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
scatter plot for age and fare columns in the titanic dataset.
Ans:
import plotly.graph_objects as go
import seaborn as sns
tips = sns.load_dataset('titanic')
fig = go.Figure()
fig.add_trace(go.Scatter(x =tips.age , y=tips.fare,mode = 'markers'))
"""

"""
Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express.
Ans:
import plotly.express as px 
df = px.data.tips() 
fig = px.box(df, x="day", y="total_bill") 
fig.show()
"""

"""
Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
column with the color parameter.
Ans:
import plotly.express as px 
df = px.data.tips() 
fig = px.histogram(df, x="sex", y="total_bill",pattern_shape="smoker",color = "day") 
fig.show()
"""
"""
Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
the color parameter.
Ans:
import plotly.express as px
df = px.data.iris()
fig = px.scatter_matrix(df,color="species")
fig.show()
"""

"""
Q5. What is Distplot? Using Plotly express, plot a distplot.
Ans:
The distplot figure factory displays a combination of statistical representations of numerical data, 
such as histogram, kernel density estimation or normal curve, and rug plot.
import plotly.express as px
import numpy as np
x = np.random.randn(1000)
hist_data = [x]
group_labels = ['distplot']
fig = ff.create_distplot(hist_data, group_labels)
iplot(fig)
"""