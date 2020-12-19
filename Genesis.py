import speech_recognition as sr #Voice Recog
import pyttsx3 # TTS
from datetime import datetime
import sys
# import pywhatkit

tts = pyttsx3.init()
listener = sr.Recognizer()

def Talk(txt):
    print(txt)
    tts.say(txt)
    tts.runAndWait()

def CommandLine(command):
    if 'time' in command:
        Talk("Current time is "+datetime.now().strftime('%I:%M'))
    if 'day' in command:
        Talk("Current date is "+datetime.today.strftime('%d %B %Y'))
    if 'play' in command:
        song = command.replace('play', '')
        Talk("Playing "+song)
        # pywhatkit.playonyt(song)

    TakeCommand(0)

def TakeCommand(check):
    if(check):
        Talk("I'm Listenning...")
    else:
        print("Call Me Please...")

    try:
        with sr.Microphone() as source:
            command = listener.recognize_google(listener.listen(source)).lower()
            if(check != 1):
                if 'genesis' in command: #Check If It Calls
                    TakeCommand(1) #Trigger The Command To Take Command
            else:
                if "i'm good" in command:
                    Talk("See you later")
                else:
                    CommandLine(command.replace('genesis',''))
    except:
        if(check):
            if "i'm good" not in command:
                Talk("Can't catch that one")
                TakeCommand(0)
        else:
            TakeCommand(0)

    if(check):
        if "i'm good" not in command:
            TakeCommand(0)
    else:
        TakeCommand(0)

TakeCommand(0)