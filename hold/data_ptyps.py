import plotext as plx
import mysql.connector
import matplotlib.pyplot as plt
from datetime import timedelta
import pandas as pd

import numpy as np
import plotext


from datetime import datetime

from matplotlib import pyplot as p
#decimal time = hh.hhh,

cnn = mysql.connector.connect(port=3306, host='localhost', database='timeproject', password='kartoshka')

cnn.connect()
cu = cnn.cursor()

cu.execute('select * from prototype;')
data = cu.fetchall()


print(data)

def render_bar(data, format='in'):
    str = []

    for item, time, stamp in data:
        'to convert hh:mm:ss format to hh.hhh'
        time = time.total_seconds()
        hours = int(time // 3600)
        minutes = int((time % 3600) // 60)
        seconds = time % 60
        'finish'

        hours_fraction = float(hours + minutes / 60 + seconds / 3600) #type = float

        item = (f'{item}', hours_fraction)# + , f'{stamp}
        str.append(item)

    cu.close()
    cnn.close()

    "converts into float for plotext" #i tried but somehow it didnt work
    if format == 'out':
        items, time_values = zip(*str)
        plt.bar(items, time_values)
        plt.xlabel("Item")
        plt.ylabel("Time (hours)")
        plt.title("Time Spent on Each Item")

        plt.show()
    else:
        items, time_values = zip(*str)
        plx.bar(items, time_values)
        plx.xlabel("Item")
        plx.ylabel("Time (hours)")
        plx.title("Time Spent on Each Item")

        plx.show()

    return print('Bar chart rendered..')

str = render_bar(data, format='out')
