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
