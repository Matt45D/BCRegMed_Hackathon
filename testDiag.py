from dialog import detect_intent_stream
from micStream import record

projectID = "diagflow-jrhdbf"
sessionID = "2"
audiofilepath = "file.wav"
languageCode = "en"

response = 1
while response:
    record()
    detect_intent_stream(projectID, sessionID, audiofilepath, languageCode)
    response = input("Press 1 to add another command, and 0 to stop")
