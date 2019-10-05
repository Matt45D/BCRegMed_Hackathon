def implicit():
    from google.cloud import speech

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    speech_client = speech.SpeechClient()

    # Make an authenticated API request
    buckets = list(speech_client.list_buckets())
    print(buckets)

implicit()
