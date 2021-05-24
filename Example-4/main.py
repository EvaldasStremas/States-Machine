# import time, threading

# def foo():
#     print(time.ctime())

#     threading.Timer(10, foo).start()

# foo()

###############################################

# Program to demonstrate
# timer objects in python
  
# import threading
# def gfg():
#     print("GeeksforGeeks\n")
  
# timer = threading.Timer(2.0, gfg)
# timer.start()
# print("Exit\n")

###############################################

import threading, time

def foo():
    print(time.ctime())
    
WAIT_TIME_SECONDS = 2

ticker = threading.Event()
while not ticker.wait(WAIT_TIME_SECONDS):
    foo()