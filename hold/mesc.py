import logging
import threading
import time
lock = threading.Lock()

def task():
    print('Using Thread')
    time.sleep(30)
    print('Complete')

def background():
    for i in range(100):
        print(i)
        time.sleep(.3)
#
#
# thread = threading.Thread(target=task, args=(lock,))
# task(thread)
# background()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")


    x = threading.Thread(target=task(), args=(1,))
    bx = threading.Thread(target=background(), args=(2,))
    bx.start()
    x.start()


    # x.join()




