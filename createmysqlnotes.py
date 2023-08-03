import pandas as pd
import matplotlib as mtp
import datetime
import mysql.connector
from mysql.connector import errorcode
import mysqlx
from mysql.connector import (connection)

# try:
cnn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database='timeproject',
    password='kartoshka'
)

print('SERVER CONNECTED')





cursor = cnn.cursor()
#
query = ("INSERT INTO data (variable, time_spent) VALUES (%s, %s)")
# denn = 'dennis'
# ung= 'ungureanu'
#
# nm = (denn, ung)

dta = ('nothing', '12:20:00')
# cursor.execute(query, dta)

cursor.execute('SELECT * FROM data;')

data1 = cursor.fetchall()
print(data1)
cnn.commit()
cursor.close()
cnn.close()

# except mysql.connector.Error as e:
#     if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print('SOMETHING IS WRONG WITH USER OR PASSWORD')
#     elif e.errno == errorcode.ER_BAD_DB_ERROR:
#         print('DATABASE DOES NOT EXIST')
#     else:
#         print(e)