import threading
from streamdialog import request_generator
from dialog import detect_intent_stream
from micStream import record

projectID = "diagflow-jrhdbf"
sessionID = "2"
audiofilepath = "file.wav"
languageCode = "en"

print("1")

response = 1
while response:
    print("2")
    micRecordThread = threading.Thread(target=record())
    dialogConnectionThread = threading.Thread(target=detect_intent_stream(), args=(projectID, sessionID, audiofilepath, languageCode))
    response = input("Press 1 to add another command, and 0 to stop")
