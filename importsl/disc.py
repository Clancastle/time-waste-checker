#// first make the disc for commands, then /info {cmd}


#  /
info = """
-----------------------------------------------------------------
> /info 'command'
Will return a description of the command and how to use it.
-----------------------------------------------------------------
"""

#  /
cmd = """
-----------------------------------------------------------------
Commands have a '/' prefix.

> / 
Returns you to default.  

Basic Commands
> info, cmd, help, terminate, streak, add_data, delete

Data Visualization Commands
> data_map, data_graph, linear_regression
-----------------------------------------------------------------
"""

#  /
help = """
-----------------------------------------------------------------
This is a project made to increase my experience in Data Science.
-----------------------------------------------------------------

Commands have a '/' prefix.
Do /cmd for basic commands.

if you have questions or concerns, contact me at -dennisungureanu0@gmail.com
-----------------------------------------------------------------
"""
terminate = '''
-----------------------------------------------------------------
This command terminates all processes.
----------------------------------------------------------------- 
'''
#  /
delete = """
-----------------------------------------------------------------
This command deletes data specified if exists.

> /delete prefix.
> commands > all, last, recent


/delete all (variable)
> when you add data by /add_data, item = variable, and you will delete all mentions of the variable.

/delete last 
> deletes the last item added to the list, sorted by last uploaded.

/delete recent (variable)
> deletes the most recent mention of the variable. 
-----------------------------------------------------------------
"""

#  /
streak = """
-----------------------------------------------------------------
This command returns True or False if you currently have a streak.
-----------------------------------------------------------------
"""


'Data Visualization'

#  /
add_data = """
-----------------------------------------------------------------
Adds data to a database, in order to cultivate a streak and understand your time wasted.

How:
/add_data
> 'Input Variable:'
> 'Input Time spent on Variable:'
> Validating: 
> Inserted in database, ready to plot.

Type x: to terminate process.
-----------------------------------------------------------------
"""
#  /
data_graph = """
-----------------------------------------------------------------
Returns a graph of the data collected, to see how well you've been doing.
-----------------------------------------------------------------

> commands > /data_graph, data_graph(in/out)

/data_graph in
displays a bar chart of data in current table for today, and returns it in terminal

/data_graph out
displays a bar chart of data outside of terminal, and that bar chart is easier to visualize.

"""
#  /
data_map = """
-----------------------------------------------------------------
Returns a scatterplot of the data collected. 
-----------------------------------------------------------------
"""
#  /
linear_regression = """
-----------------------------------------------------------------
Returns a linear regression model, based on past data.
-----------------------------------------------------------------
"""

# # more commands coming
# /data > commands
# /data_map
# /data_graph
# etc
