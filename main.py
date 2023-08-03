import time

from importsl import data_functions
from importsl import disc
import threading
from threading import Thread
# from importsl.disc import cmd_disc

'# if there is something i learnt , always use return'
'# like return print()'
print('STARTING...\n')
print('CONNECTED TO SERVER')

delete_cooldown = False
def perform_deletion():
    global delete_cooldown

    if delete_cooldown:
        print("1 hr delete cooldown is in effect. Please wait until it completes.")
        return
    time.sleep(2)
    data_functions.delete_data()
    delete_cooldown = True

    def reset_cooldown():
        global delete_cooldown
        time.sleep(3600)  # Sleep for 1 hour
        delete_cooldown = False

    # Start the thread to reset cooldown after 1 hour
    reset_thread = threading.Thread(target=reset_cooldown, daemon=True)
    reset_thread.start()
def check_cmd(inp):

    if len(inp.split()) > 1 and inp.split()[0] == '/info':
        # makes sure input from user is more than 1 word, so it doesnt return an error (list index out of range)

        if inp.split()[1] == 'delete':
            return print(disc.delete)

        elif inp.split()[1] == 'terminate':
            return print(disc.terminate)

        elif inp.split()[1] == 'streak':
            return print(disc.streak)

        elif inp.split()[1] == 'add_data':
            return print(disc.add_data)

        elif inp.split()[1] == 'data_map':
            return print(disc.data_map)

        elif inp.split()[1] == 'data_graph':
            return print(disc.data_graph)

        elif inp.split()[1] == 'linear_regression':
            return print(disc.linear_regression)
        else:
            return print('Sorry, that does not exist.')

    if inp.split()[0] == '/info' and len(inp.split()) == 1:
        return print(disc.info)

    elif inp.split()[0] == '/cmd':
        return print(disc.cmd)

    elif inp.split()[0] == '/help':
        return print(disc.help)

    elif inp.split()[0] == '/add_data':
        return data_functions.add_data()

    elif inp.split()[0] == '/delete':
        if delete_cooldown:
            return print("1 hr delete cooldown is in effect. Please wait until it completes.")
        else:
            x = threading.Thread(target=perform_deletion)
            x.start()
            return print('Connecting to SQL Server')




    elif inp.split()[0] == '/terminate' or inp == 'x':
        print('Sorry to see you go.')
        return '/terminate'

    elif inp.split()[0] == '/streak':
        return data_functions.streaks()

    elif inp.split()[0] == '/data_map':
        return data_functions.data_map()

    elif inp.split()[0] == '/data_graph':
        return data_functions.data_graph()

    elif inp.split()[0] == '/linear_regression':
        return data_functions.linear_regression()

    elif inp.split()[0] == '/':
        return start_script()


    else:
        if len(inp.split()) > 1:
            if inp.split()[1] == 'data_map' or 'data_graph' or 'linear_regression' or 'terminate' or 'delete' or 'add_data' or 'streak' or 'help' or 'cmd' or 'info':
                pass

        return print(f'Sorry, the specified command does not exist.')

def start_script():
    try:
        print("""
-----------------------------------------------------------------
Welcome, this project has taken many years of my life, and it probably does not work.
The purpose of this project is to better understand the time I waste everyday.

In this project I use MySQL, with a simple user interface, as well as some other libraries and frameworks. 

-----------------------------------------------------------------
Do /cmd
Do '/' to reset
-----------------------------------------------------------------
""")
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

# start_script()

while True:

    cmd = check_cmd(get_input())

    # cmd = threading.Thread(target=check_cmd(get_input()), args=(3,))
    # cmd.start()
    # c = check_cmd(get_input())
    time.sleep(1)
    if cmd == '/terminate':
        print('Ha, fooled ya. ')
        #break



print('CLOSING CONNECTION...')
# cnn.close()