import speech_recognition as sr #Voice Recog
import pyttsx3 # TTS
from datetime import datetime #For Time Purposes
import os
import pywhatkit #Play Youtube
import webbrowser #For Searching Purposes
import wikipedia #Summary Informations
import pyautogui as pyag #For Screenshots
import json #To read Json Files
import psutil #To Get Battery and CPU

tts = pyttsx3.init('sapi5')
listener = sr.Recognizer()
listener.pause_threshold = 0.5

querys = ["who is", "what is", "time", "date", "play", "weather", "screenshot", "battery"]
wisher = ["Good Morning Sir!", "Good Afternoon Sir!", "Good Night Sir!"]

#Get BitRate
rate = tts.getProperty('rate')
tts.setProperty('rate', 220) #Default Bitrate = 200
listener.pause_threshold = 0.5

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

#Screenshots the entire screens
def Screenshots():
    img = pyag.screenshot()
    with open('settings.json') as jsons:
        data = json.load(jsons)
        path = data['SaveScreen_Shots']
        if not os.path.exists(data['SaveScreen_Shots']):
            os.mkdir(path)

        date = datetime.today().strftime('%d-%m-%y')
        time = datetime.today().strftime('%H-%M-%S')
        filename = "/Genesis_"+date+"_"+time+".png"
        img.save(data['SaveScreen_Shots']+filename)

        if os.path.exists(path+filename):
            Talk("Screenshots Taken!")

def GetBattery():
    return psutil.sensors_battery()

def CommandLine(command):
    if CheckQuery(command):
        if NewCheckQuery(["time", "date", "weather", "battery"], command):
            if 'time' in command:
                CurrentTime()
            if 'date' in command:
                CurrentDate()
            if 'weather' in command:
                CurrentWeather(command)
            if 'battery' in command:
                Talk("Your current battery is "+str(GetBattery().percent)+"%")
        if not NewCheckQuery(["time", "date", "weather", "battery"], command):
            if 'who is' in command:
                SearchWho(command)
            if 'what is' in command:
                SearchWhat(command)
        if 'play' in command:
            PlayYoutube(command)
        if 'screenshot' in command:
            Screenshots()
    else:
        Talk("Command not found")

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

batCount = 0
firstRun = True

while True:
    print("Call Me Please...")
    if firstRun:
        Talk("The Current Battery is "+str(GetBattery().percent)+"%")
        firstRun = False
    if GetBattery().percent == 100:
        if batCount == 0:
            Talk("Sir, your battery is full")
            batCount = 1
    elif GetBattery().percent == 25:
        Talk("Sir, only 25% of your battery left")
    else:
        if batCount == 1:
            batCount = 0
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
            print(command)
            CommandLine(command)