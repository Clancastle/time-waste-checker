import json
import mysql.connector
import plotext as plx
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mtp
import re
import time as tim
from datetime import datetime
from importsl import data_functions

'compare tables in database'

cnn = mysql.connector.connect(port=3306, host='localhost', database='timeproject', password='kartoshka')
cnn.connect()
cursor = cnn.cursor()

data = data_functions.clean_input()

print(data)



cursor.close()
cnn.close()