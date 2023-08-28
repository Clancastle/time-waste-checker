import mysql.connector
from importsl import data_functions

'compare tables in database'

cnn = mysql.connector.connect(port=3306, host='localhost', database='timeproject', password='kartoshka')
cnn.connect()
cursor = cnn.cursor()

data = data_functions.clean_input()

print(data)



cursor.close()
cnn.close()