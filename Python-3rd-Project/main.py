import speech_recongintion as sr

listener = sr.Recognizer()
try:
    with sr.Microphone as source:
        print('Listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print (command)

except:
    pass

