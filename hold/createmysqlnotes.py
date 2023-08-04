import pandas as pd
import matplotlib as mtp
import datetime, time, logging
import threading
import concurrent.futures
# import mysql.connector
# from mysql.connector import errorcode
# import mysqlx
# from mysql.connector import (connection)
#
# # try:
# cnn = mysql.connector.connect(
#     host="127.0.0.1",
#     port=3306,
#     database='timeproject',
#     password='kartoshka'
# )
#
# print('SERVER CONNECTED')
#
#
#
#
#
# cursor = cnn.cursor()
# #
# query = ("INSERT INTO data(time_spent) VALUES(%s)")
# # denn = 'dennis'
# # ung= 'ungureanu'
# #
# # nm = (denn, ung)
# tm = '00:00:00'
#
# dta = ('nothing', '12:20:00') # only accepts from tuple dict or list mysql
# cursor.execute(query, '01')
#
# cursor.execute('SELECT * FROM data;')
#
# data1 = cursor.fetchall()
# print(data1)
# cnn.commit()
# cursor.close()
# cnn.close()

# except mysql.connector.Error as e:
#     if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print('SOMETHING IS WRONG WITH USER OR PASSWORD')
#     elif e.errno == errorcode.ER_BAD_DB_ERROR:
#         print('DATABASE DOES NOT EXIST')
#     else:
#         print(e)
import concurrent.futures

# [rest of code]
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)