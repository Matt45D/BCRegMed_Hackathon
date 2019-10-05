import json
import logging
import os
import threading
import time
import sys
from RecThread import ReceiveThread
from SendThread import SendThread
from queue import Queue
from threading import Thread
from time import time


def main():
    print("Hello World From Main Thread!")

    '''Initialize the receiving child thread'''
    thread1 = threading.Thread(target = ReceiveThread(), args = 10)
    thread1.start()

    '''Initialize the sending child thread'''
    thread2 = threading.Thread(target = SendThread(), args = 10)
    thread2.start()

class MyDrone:
    

if __name__ == '__main__':
    main()
