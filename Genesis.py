import speech_recognition as sr #Voice Recog
import pyttsx3 # TTS
from datetime import datetime #For Time Purposes
import os
import pywhatkit #Play Youtube
import webbrowser #For Searching Purposes
import wikipedia #Summary Informations

tts = pyttsx3.init('sapi5')
listener = sr.Recognizer()
listener.pause_threshold = 0.5

querys = ["who is", "what is", "time", "date", "play", "weather"]
wisher = ["Good Morning Sir!", "Good Afternoon Sir!", "Good Night Sir!"]

def Talk(txt):
    tts.say(txt)
    tts.runAndWait()

#For All Query That Used
def CheckQuery(command):
    for query in querys:
        if query in command:
            return True

#For Certain Query of strings
def NewCheckQuery(querys, command):
    for query in querys:
        if query in command:
            return True

def CommandLine(command):
    if CheckQuery(command):
        if NewCheckQuery(["time", "date", "weather"], command):
            if 'time' in command:
                CurrentTime()
            if 'date' in command:
                CurrentDate()
            if 'weather' in command:
                CurrentWeather(command)
        if not NewCheckQuery(["time", "date", "weather"], command):
            if 'who is' in command:
                SearchWho(command)
            if 'what is' in command:
                SearchWhat(command)
        if 'play' in command:
            PlayYoutube(command)
    else:
        Talk("Command not found")

#Get Current System Time
def CurrentTime():
    Talk("Current time is "+datetime.now().strftime('%I:%M'))

#Get Current System Date
def CurrentDate():
    Talk("Current date is "+datetime.today().strftime('%d %B %Y'))

#Get Current weather
def CurrentWeather(command):
    webbrowser.get().open_new_tab("https://google.com/search?q="+command)
    Talk("Here is the info of the current wheather")

#Search Specific Things In Googles
def SearchWho(command):
    search = command.replace('who is', '', 1)
    info = wikipedia.summary(search, 1)
    # pywhatkit.search(command)
    webbrowser.get().open_new_tab("https://google.com/search?q="+command)
    Talk(info)
#Search Specific Things In Googles
def SearchWhat(command):
    search = command.replace('what is', '', 1)
    info = wikipedia.summary(search, 1)
    # pywhatkit.search(command)
    webbrowser.get().open_new_tab("https://google.com/search?q="+command)
    Talk(info)

#Play YouTube Videos
def PlayYoutube(command):
    song = command.replace('play', '', 1)
    Talk("Playing"+song)
    pywhatkit.playonyt(song)

def TakeCommand():
    with sr.Microphone() as source:
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice).lower()
    except:
        return "..."
    return command

def WishMe():
    hour = datetime.now().hour

    if hour >= 0 and hour < 12:
        print(wisher[0])
        Talk(wisher[0])
    elif hour >= 12 and hour < 18:
        print(wisher[1])
        Talk(wisher[1])
    else:
        print(wisher[2])
        Talk(wisher[2])

WishMe()
Talk("Genesis is ready!")

while True:
    call = TakeCommand()
    if 'genesis' in call:
        print("I'm Listenning...")
        Talk("I'm Listenning...")
        command = TakeCommand()
        if "i'm good" in command:
            Talk("See you later sir!")
            exit()
        elif command == "...":
            print("Can't catch that one")
            Talk("Can't catch that one")
        else:
            CommandLine(command)
    elif call == "...":
        print("Call Me Please...")