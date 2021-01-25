import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes


listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
     try:
         with sr.Microphone() as nayem:
              print('listening........')
              voice = listener.listen(nayem)
              command = listener.recognize_google(voice)
              command = command.lower()
              if 'alexa' in command:
                  command = command.replace('alexa', '')


     except:
        pass
     return command


def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M')
        print(time)
        talk('Current Time Is '+time)
    elif 'play' in command:
        song = command.replace('play','')
        talk('Playing' +song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about','')
        info = wikipedia.summary(look_for, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry Vaiya, I am in another Relationship ')
    elif 'single' in command:
        talk('No I have no relationship' 'You love me, THen I love You, I kiss You, I hage You')
    elif 'feeding' in command:
        talk("Yes I Feeding You")
    else:
        talk('Please say it again, I did not get it but I am going to search it for you again')
        pywhatkit.search(command)

while True:
      run_alexa()