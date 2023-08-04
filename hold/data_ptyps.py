import matplotlib.pyplot as plt
import mysql.connector
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotext
import plotext as plt

from datetime import datetime

from matplotlib import pyplot as p

cnn = mysql.connector.connect(port=3306, host='localhost', database='timeproject', password='kartoshka')

cnn.connect()
cu = cnn.cursor()

cu.execute('select * from prototype;')
data = cu.fetchall()


print(data)

def convert(data):
    for item, time, stamp in data:
        str = []
        str.append((f'{item}', f'{time}', f'{stamp}'))
        continue
    return str

print(convert(data))
cnn.commit()
cu.close()
cnn.close()

import plotext as plt

data = [
    ("workout", 0),
    ("coding", 9),
    ("studying", 2.5),
    ("meditate", 0.33),
    ("journal", 0.25),
    ("reading", 0.75),
    ("walking", 0),
    ("sunset", 0.08),
    ("6 am", 0),
    ("abstinence", 0),
    ("no sugar", 0),
    ("sleep", 0),
]

items, time_values = zip(*data)
plt.bar(items, time_values)
plt.xlabel("Time (hours)")
plt.ylabel("Item")
plt.title("Time Spent on Each Item")
plt.show()

