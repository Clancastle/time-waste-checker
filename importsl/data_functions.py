import json
import mysql.connector
import pandas as pd
import matplotlib as mtp
import re, time
from datetime import datetime
from threading import Event
from threading import Thread
# from time_waste_checker.main import check_cmd
exit = Event()


cnn = mysql.connector.connect(
    port=3306,
    host='localhost',
    database='timeproject',
    password='kartoshka'
)


data = {}
cursor = cnn.cursor()
def add_data():
    try:

        def call_inp():
            print('\ntype \'x\' to close, when 24hs have been reached.\n')
            print('Item name: (coding) (Example) \nTime spent: (05:30:00) format(hh/mm/ss)(example)\n')
            var = input('item: ')
            time = input('time spent: ')
            return var, time

        while True:
            cursor = cnn.cursor()
            print(data)

            var, time = call_inp()

            if var == 'x' or time == 'x':
                cursor.close()

                cnn.close()
                return None

            if (not re.search(r'[\d\W]', var)) and (re.match(r'(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)', time)):
                print('Passed Validation')
                data[var] = [time]

                cursor.execute('insert into data(variable, time_spent, timestamp) values (%s, %s, %s)', (var, time, datetime.now()))
                cnn.commit()
                continue
            else:
                cursor.close()

                cnn.close()
                return print('Try again with correct formatting.'), add_data()

        return data
    except Exception as e:
        cursor.close()

        cnn.close()
        return print(f'Error occurred: {e}'), add_data()

def sleep():
    while not exit.is_set():
      exit.wait(10)

def quit(_frame):
    exit.set()

    print("All done!")
def delete_data():
    def get_input():
        print('\nPlease read /info delete before using this to prevent unintentional data loss.')
        print('e.x. \n> delete variable (or)\n> delete time')
        inp = input('\n>')
        return inp

    try:

        inp = get_input()
        if re.compile('([a-zA-Z0-9\s])+').match(inp):

            if inp.split()[0] == 'recent':
                print(f'Deleting last entry of: {inp.split()[1]}..')
                cnn.connect()
                query = 'delete from data where variable=(%s) order by timestamp desc limit 1;'
                cnn.cursor().execute(query, (inp.split()[1],))
                print(f'Deleted')
                cnn.commit()
                cnn.cursor().close()
                cnn.close()


                return None
            elif inp.split()[0] == 'all':

                query = f'delete from data where variable=(%s)'

                cnn.connect()
                print(f'Deleting all {inp.split()[1]}..')
                cnn.cursor().execute(query, (inp.split()[1],))
                print('Deleted')

                cnn.commit()
                cnn.cursor().close()
                cnn.close()

                return None

            elif inp.split()[0] == 'last':
                print('Deleting..')
                cnn.connect()
                cnn.cursor().execute('delete from data order by timestamp desc limit 1;')
                cnn.commit()
                print('Deleted..')
                cnn.cursor().close()
                cnn.close()

                return

            else:
                return print('Does not exist:'), None

    except Exception as e:
        print(f'Error found: {e}\n Not Deleted..')

def data_map():
    print('used')


def data_graph():
    print('used')


def linear_regression():
    print('used')


def streaks():
    print('used')



