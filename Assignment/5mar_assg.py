"""
Q1. How can you create a Bokeh plot using Python code?
Ans:
we can create bokeh plot using following commands
import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()
from bokeh.plotting import figure,output_file,show  
from bokeh.sampledata.iris import flowers  
output_file('test.html')
p=figure(title = 'test flower')
p.xaxis.axis_label = 'petal_length'
p.yaxis.axis_label = 'petal_width'
p.circle(flowers['petal_length'] , flowers['petal_width'])
show(p)              
"""

"""
Q2. What are glyphs in Bokeh, and how can you add them to a Bokeh plot? Explain with an example.
Ans:
Glyphs are the building blocks of Bokeh visualizations. A glyph is a vectorized graphical shape or marker that is used to represent your data.
from bokeh.io import output_file
from bokeh.plotting import figure, show
x = [1, 2, 1]
y = [1, 1, 2]

# Output the visualization to a static HTML file - first_glyphs.html
output_file('first_glyphs.html', title='First Glyphs')

# Create a figure with no toolbar and axis ranges [0, 3]
fig = figure(title='My Coordinates',
             plot_height=300, plot_width=300,
             x_range=(0, 3), y_range=(0, 3),
             toolbar_location=None)

# Draw the coordinate as circles
fig.circle(x=x, y=y, 
           color='green', size=10, alpha=0.5)

# Show plot 
show(fig)
"""
"""
Q3. How can you customize the appearance of a Bokeh plot, including the axes, title, and legend?
Ans:
using following commands we can customize axis
p.xaxis.axis_label = "Temp"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"



The legend of a graph reflects the data displayed in the graph’s Y-axis. In Bokeh, the legends correspond to glyphs.
# display legend in top left corner
plots.legend.location = "top_left"
 
#give title to legend
plots.legend.title = "Observation of plot"
 
#customize legend appearance
plots.legend.label_text_font = "times"
plots.legend.label_text_font_style = "bold"
plots.legend.label_text_color = "black"
"""
"""
Q4. What is a Bokeh server, and how can you use it to create interactive plots that can be updated in
real time?
Ans:
Bokeh server is a Python library that allows you to build interactive web applications and dashboards with Bokeh plots. 
Bokeh is a Python visualization library that generates interactive plots and charts for modern web browsers. 
The Bokeh server allows you to add interactivity to your plots, such as zooming and panning, selecting data points, 
and updating the data in real-time.

To use Bokeh server to create interactive plots that can be updated in real-time, you'll need to follow these steps:

Create a Bokeh plot: Start by creating a Bokeh plot with the data you want to display. You can create a variety of plots, 
such as line charts, scatter plots, and bar charts, using the Bokeh library.

Define the Bokeh server application: Define a Bokeh server application that serves your plot and handles the user interactions. 
This application can be defined as a Python script that imports the necessary libraries and defines the Bokeh plot and its interactivity.

Launch the Bokeh server: Launch the Bokeh server using the bokeh serve command, and specify the path to your Bokeh server application.

Interact with the plot: Once the Bokeh server is running, you can interact with the plot in your web browser. 
The Bokeh server handles the user interactions and updates the plot in real-time based on the user input.
"""

"""
Q5. How can you embed a Bokeh plot into a web page or dashboard using Flask or Django?
Ans:
To embed a Bokeh plot into a web page or dashboard using Flask or Django, you can use the Bokeh server and embed the plot in an HTML template 
using the {{ bokeh_script | safe }} and {{ bokeh_div | safe }} variables provided by the Bokeh library.

Here are the general steps you can follow:

Define the Bokeh server application: Define a Bokeh server application that serves your plot. 
This application can be defined as a Python script that imports the necessary libraries and defines the Bokeh plot and its interactivity.

Create a Flask or Django app: Create a Flask or Django app that will host the web page or dashboard. In Flask, 
you can define the app using the Flask constructor, and in Django, you can create a new app using the startapp command.

Define a route for the web page or dashboard: Define a route in your Flask or Django app that will serve the HTML template for 
your web page or dashboard.

Embed the Bokeh plot in the HTML template: In the HTML template, use the {{ bokeh_script | safe }} and {{ bokeh_div | safe }} variables to embed 
the Bokeh plot in the page.

Launch the Flask or Django app: Launch the Flask or Django app using the appropriate command for your framework, and navigate to the web page or 
dashboard in your web browser.

"""