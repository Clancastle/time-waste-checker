import datetime
import time

from importsl import data_functions
from importsl import disc
import threading
import mysql.connector
from threading import Thread
# from importsl.disc import cmd_disc

cnn = mysql.connector.connect(port=3306, host='localhost', database='timeproject', password='kartoshka')

date_yymmdd = datetime.datetime.today().strftime('%Y_%m_%d')

'# if there is something i learnt , always use return'
'# like return print()'
print('STARTING...\n')
print('CONNECTED TO SERVER')

'do more classes and object oriented programming'
def check_cmd(inp):
    try:

        if len(inp.split()) > 1 and inp.split()[0] == '/info':
            # makes sure input from user is more than 1 word, so it doesnt return an error (list index out of range)

            if inp.split()[1] == 'delete':
                return print(disc.delete)

            if inp.split()[1] == 'terminate':
                return print(disc.terminate)

            if inp.split()[1] == 'streak':
                return print(disc.streak)

            if inp.split()[1] == 'add_data':
                return print(disc.add_data)

            if inp.split()[1] == 'data_map':
                return print(disc.data_map)

            if inp.split()[1] == 'data_graph':
                return print(disc.data_graph)

            if inp.split()[1] == 'linear_regression':
                return print(disc.linear_regression)

        if inp.split()[0] == '/info' and len(inp.split()) == 1:
            return print(disc.info)

        if inp.split()[0] == '/cmd':
            return print(disc.cmd)

        if inp.split()[0] == '/help':
            return print(disc.help)

        if inp.split()[0] == '/add_data':
            return data_functions.add_data()

        if inp.split()[0] == '/delete':
            try:
                if inp.split()[1] == 'all':

                    query = f'delete from {date_yymmdd} where item=(%s) order by timestamp'

                    cnn.connect()
                    print(f'Deleting all {inp.split()[2]}..')
                    cnn.cursor().execute(query, (inp.split()[2],))
                    print('Deleted')
                    cnn.commit()
                    cnn.cursor().close()
                    cnn.close()

                    return None

                if inp.split()[1] == 'recent':
                    print(f'Deleting last entry of: {inp.split()[2]}..')
                    cnn.connect()
                    query = f'delete from {date_yymmdd} where item=(%s) order by timestamp desc limit 1;'
                    cnn.cursor().execute(query, (inp.split()[2],))
                    print(f'Deleted')
                    cnn.commit()
                    cnn.cursor().close()
                    cnn.close()
                    return None

                if inp.split()[1] == 'last':
                    print('Deleting..')
                    cnn.connect()
                    cnn.cursor().execute(f'delete from {date_yymmdd} order by timestamp desc limit 1;')
                    cnn.commit()
                    print('Deleted..')
                    cnn.cursor().close()
                    cnn.close()
                    return


            except Exception as e:
                print(f'Error: {e}\nTry /info delete \n /delete is different from other commands.')


        if (inp.split()[0] == '/terminate') or (inp == 'x'):
            return '/terminate'

        if inp.split()[0] == '/streak':
            return data_functions.streaks()

        if inp.split()[0] == '/data_map':
            return data_functions.data_map()

        if inp.split()[0] == '/data_graph':

            if (len(inp.split()) > 1):

                if inp.split()[1] != 'out':
                    return data_functions.render_bar(format='in')

                if inp.split()[1] == 'out':
                    return data_functions.render_bar(format='out')

            return data_functions.render_bar(format='in')


        if inp.split()[0] == '/linear_regression':
            return data_functions.linear_regression()

        if inp.split()[0] == '/tables':
            return print(data_functions.show_tables())

        if inp.split()[0] == '/':
            return start_script()

    except Exception as e:
        print(e)


def start_script():
    try:
        print("""
-----------------------------------------------------------------
Welcome, this project has taken many years of my life, and it probably does not work.
The purpose of this project is to better understand the time I waste everyday.

In this project I use MySQL, Workbench, with a simple user interface, as well as some other libraries and frameworks. 
I decided to not upload this project to a server or put it on the web, since i've done so several times and I wanted to try something new.
Im using plotext (pip install plotext) for this neat terminal stuff.

-----------------------------------------------------------------
Do /cmd
Do '/' to reset
-----------------------------------------------------------------
"""

)
        time.sleep(.7)
        inp = input('\n\n>')
        time.sleep(.5)

        return check_cmd(inp)

    except Exception as e:
        return print(f'An error encountered: {e}', f'\nReason: {inp}')
'^ This is most likely complete ^'


def get_input():
    try:
        user_input = input('\n>')
        return user_input.strip()
    except Exception as e: #when enconters error, sends error to user, reason for error(not really), and does simple function recursion
        #reason for this, is to prevent sql injection slightly, and prevent user from messing up database.
        print('Please enter a valid data format.'), print(f'Error encountered: {e}',f'\nReason: {user_input}')
        return get_input()


check_cmd(start_script())
while True:

    cmd = check_cmd(get_input())

    # cmd = threading.Thread(target=check_cmd(get_input()), args=(3,))
    # cmd.start()
    # c = check_cmd(get_input())
    time.sleep(1)
    if cmd == '/terminate':
        break



print('CLOSING CONNECTION...')
