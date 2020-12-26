import json #Reading Json File
from datetime import datetime #For Time Purposes
import os #For OS Use
import pywhatkit #Play Youtube
import webbrowser #For Searching Purposes
import wikipedia #Summary Informations

#Get Current System Time
def CurrentTime():
    return "Current time is "+datetime.now().strftime('%I:%M')

#Get Current System Date
def CurrentDate():
    return "Current date is "+datetime.today().strftime('%d %B %Y')

#Get Current weather
def CurrentWeather(command):
    webbrowser.get().open_new_tab("https://google.com/search?q="+command)
    return "Here is the info of the current wheather"

#Search Specific Things In Googles
def SearchWho(command):
    if len(command.split()) > 2:
        search = command.replace('who is', '', 1)
        info = wikipedia.summary(search, 1)
        webbrowser.get().open_new_tab("https://google.com/search?q="+command)
        return info
    else:
        return "Please Be Specific"
#Search Specific Things In Googles
def SearchWhat(command):
    if len(command.split()) > 2:
        search = command.replace('what is', '', 1)
        info = wikipedia.summary(search, 1)
        webbrowser.get().open_new_tab("https://google.com/search?q="+command)
        return info
    else:
        return "Please Be Specific"

#Play YouTube Videos
def PlayYoutube(command):
    song = command.replace('play', '', 1)
    pywhatkit.playonyt(song)
    return "Playing"+song

#Get Apps path
def AppsPath(command):
    with open('settings.json') as jsons:
        data = json.load(jsons)
        appsName = data['Applications']
        programs = data['Programs']

        for i in range(len(appsName)):
            temp = 'Programs'+str(i+1)
        
            if programs[i][temp]['ApplicationsReference'] in command:
                return programs[i][temp]['ApplicationsPath']

#Get Apps name
def AppsName(command):
    with open('settings.json') as jsons:
        data = json.load(jsons)
        appsName = data['Applications']
        programs = data['Programs']

        for i in range(len(appsName)):
            temp = 'Programs'+str(i+1)
        
            if programs[i][temp]['ApplicationsReference'] in command:
                return programs[i][temp]['ApplicationsName']

#Get Screenshot path and name
def Screenshots():
    with open('settings.json') as jsons:
        data = json.load(jsons)
        path = data['SaveScreen_Shots']
        path = path.replace("%userprofile%",os.getenv("userprofile"))
        if not os.path.exists(path):
            os.mkdir(path)
        
        date = datetime.today().strftime('%d-%m-%y')
        time = datetime.today().strftime('%H-%M-%S')
        filename = "/Genesis_"+date+"_"+time+".png"

        return path+filename