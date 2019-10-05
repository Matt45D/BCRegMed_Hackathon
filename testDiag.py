from dialog import detect_intent_stream
from micStream import record

projectID = "diagflow-jrhdbf"
sessionID = "2"
audiofilepath = "file.wav"
languageCode = "en"

record()
detect_intent_stream(projectID, sessionID, audiofilepath, languageCode)
