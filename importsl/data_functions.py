import json
import mysql.connector
import plotext as plx
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mtp
import re
import time as tim
from datetime import datetime

date_yymmdd = datetime.today().strftime('%Y_%m_%d')


cnn = mysql.connector.connect(port=3306, host='localhost', database='timeproject', password='kartoshka')

cnn.connect()
data = {}

streak = 0

cursor = cnn.cursor()
def add_data():

    def call_inp():
        print('\ntype \'x\' to close, when 24hs have been reached.\n')
        print('Item name: (coding) (Example) \nTime spent: (05:30:00) format(hh/mm/ss)(example)\n')
        var = input('item: ')
        time = input('time spent: ')
        return var, time

    while True:
        cnn.connect()
        cursor = cnn.cursor()

        var, timex = call_inp()

        if (var == 'x') or (timex == 'x'):
            cursor.close()
            cnn.close()

            return None  #'/terminate'

        if (not re.search(r'[\d\W]', var)) and (re.match(r'(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)', timex)):
            print('Passed Validation')
            data[var] = [timex]
            print('Creating..')
            tim.sleep(.3)
            cursor.execute(f'create table if not exists {date_yymmdd}(variable varchar(255), time_spent time, timestamp timestamp)')
            print('Created table')
            cursor.execute(f'insert into {date_yymmdd} values (%s, %s, %s)', (var, timex, datetime.now()))
            tim.sleep(.5)

            print('Added to table..')

            cnn.commit()
            continue #want to continue
        else:

            return print('Try again with correct formatting.'), add_data()

    cursor.close()
    cnn.close()
    return data

def delete_data():
    def get_input():
        print('\nPlease read /info delete before using this to prevent unintentional data loss.')
        inp = input('\n>')
        return inp

    try:

        inp = get_input()
        if re.compile('([a-zA-Z0-9\s])+').match(inp):

            if inp.split()[0] == 'recent':
                print(f'Deleting last entry of: {inp.split()[1]}..')
                cnn.connect()
                query = f'delete from {date_yymmdd} where variable=(%s) order by timestamp desc limit 1;'
                cnn.cursor().execute(query, (inp.split()[1],))
                print(f'Deleted')
                cnn.commit()
                cnn.cursor().close()
                cnn.close()


                return None
            elif inp.split()[0] == 'all':

                query = f'delete from {date_yymmdd} where variable=(%s)'

                cnn.connect()
                print(f'Deleting all {inp.split()[1]}..')
                cnn.cursor().execute(query, (inp.split()[1],))
                print('Deleted')

                cnn.commit()
                cnn.cursor().close()
                cnn.close()

                return None

            elif inp.split()[0] == 'last':
                print(date_yymmdd)
                print('Deleting..')
                cnn.connect()
                cnn.cursor().execute(f'delete from {date_yymmdd} order by timestamp desc limit 1;')
                cnn.commit()
                print('Deleted..')
                cnn.cursor().close()
                cnn.close()

                return

            else:
                return print('Does not exist:'), None

    except Exception as e:
        print(f'Error found: {e}\n Not Deleted..')
#unneeded func

def data_map():
    pass

def render_bar(format='in'):
    try:
        cnn = mysql.connector.connect(port=3306, host='localhost', database='timeproject', password='kartoshka')

        cnn.connect()
        cursor = cnn.cursor()
        str = []

        cursor.execute(f'select * from {date_yymmdd};')
        print('Collecting Data..')
        tim.sleep(2)
        data = cursor.fetchall()

        for item, time, stamp in data:
            'to convert hh:mm:ss format to hh.hhh'
            time = time.total_seconds()
            hours = int(time // 3600)
            minutes = int((time % 3600) // 60)
            seconds = time % 60
            'finish'

            hours_fraction = float(hours + minutes / 60 + seconds / 3600) #type = float

            itemsx = (f'{item}', hours_fraction)# + , f'{stamp}
            str.append(itemsx)

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

        cnn.cursor().close()
        cnn.close()
        return print('Bar chart rendered..')
    except ValueError:
        return print(f'Table {date_yymmdd} exists but has no values since all items were deleted.')

def linear_regression():
    pass


def streaks(base=0):
    streak = base
    last = ''
    data = clean_input()
    now = datetime.today().strftime('%Y_%m_%d')
    now = '2023_09_30'

    i = 0
    while i < len(data):
        if now in data[i]: #means that it tests if time=now is in database, returns true
            print('match: ',now, data[i])

            yr, m, d = data[i][0].split('_')
            yr, m, d = int(yr), int(m), int(d)

            d-=1

            print(d)
            for x in range(len(data)):

                i_yr, i_m, i_d = data[x][0].split('_')
                i_yr, i_m, i_d = int(i_yr), int(i_m), int(i_m)
                if (i_yr == yr) and (i_m == m) and (i_d == d):
                    print('oo')
                    streak+=1
                    d-=1
                    print(streak)
                    continue




        i+=1



    return data

def clean_input():
    data = show_tables()

    i = 0
    while i < len(data): #tested, will be out of range if you dont do this. i remember to do this cause it counts from 0.
        if len(data[i][0].split('_')) != 3:  # gets the string and splits. checking if its in time format(not really, lazy way)
            data.pop(i)
            continue
        i += 1
    return data

def show_tables():
    cnn = mysql.connector.connect(port=3306, host='localhost', database='timeproject', password='kartoshka')

    cnn.connect()
    cursor = cnn.cursor()
    'returns a list of all tables available; max = 2Bil'
    cursor.execute('show tables;')
    existing_tables = cursor.fetchall()
    cursor.close()
    cnn.close()
    return existing_tables

# print(streaks())
print(streaks())