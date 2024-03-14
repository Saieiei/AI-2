import speech_recognition as sr #speech recognition package
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() #creating recognizer to recognize your voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try: #To avoid trouble with microphone
        with sr.Microphone() as source: #source
            print('listening...')
            voice = listener.listen(source) #To listen to source
            command = listener.recognize_google(voice) #Pass voice to google and google will give text
            command = command.lower()
            if 'zara' in command:
                command = command.replace('zara','')
                print(command)
    except:
        pass
    return command
    
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'Wikipedia' in command:
        person = command.replace('Wikipedia','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')
while True:
    run_alexa()