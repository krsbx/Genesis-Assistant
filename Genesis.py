import speech_recognition as sr #Voice Recog
import pyttsx3 # TTS
import pyautogui as pyag #For Screenshots
import psutil #To Get Battery and CPU
import CommandSections #Store lot of Command

tts = pyttsx3.init('sapi5')
listener = sr.Recognizer()
listener.pause_threshold = 0.5

querys = ["who is", "what is", "time", "date", "play", "weather", "screenshot", "battery", "open"]
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

#Screenshots the entire screens
def Screenshots():
    img = pyag.screenshot()
    filename = CommandSections.Screenshots()
    img.save(filename)

    if CommandSections.os.path.exists(filename):
        Talk("Screenshots Taken!")

#Open Apps
def OpenApps(commands):
    path = CommandSections.AppsPath(commands)
    CommandSections.os.popen(path)
    Talk("Opening "+CommandSections.AppsName(commands))

#Get Current Battery
def GetBattery():
    return psutil.sensors_battery()

def CommandLine(command):
    if CheckQuery(command):
        if NewCheckQuery(["time", "date", "weather", "battery", "open"], command):
            if 'time' in command:
                Talk(CommandSections.CurrentTime())
            if 'date' in command:
                Talk(CommandSections.CurrentDate())
            if 'weather' in command:
                Talk(CommandSections.CurrentWeather(command))
            if 'battery' in command:
                Talk("Your current battery is "+str(GetBattery().percent)+"%")
            if 'open' in command:
                OpenApps(command)
        if not NewCheckQuery(["time", "date", "weather", "battery"], command):
            if 'who is' in command:
                return(CommandSections.SearchWho(command))
            if 'what is' in command:
                Talk(CommandSections.SearchWhat(command))
        if 'play' in command:
            Talk(CommandSections.PlayYoutube(command))
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
    hour = CommandSections.datetime.now().hour

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