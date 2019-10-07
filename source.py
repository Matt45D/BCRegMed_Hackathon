import threading
from streamdialog import request_generator
from dialog import detect_intent_stream
from micStream import record
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

projectID = "diagflow-jrhdbf"
sessionID = "2"
audiofilepath = "file.wav"
languageCode = "en"

print("1")

response = 1
while response:
    print("2")
    micRecordThread = threading.Thread(target=record())
    dialogConnectionThread = threading.Thread(target=detect_intent_stream, args=(projectID, sessionID, audiofilepath, languageCode))
    response = input("Press 1 to add another command, and 0 to stop")
    
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
