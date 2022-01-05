from nlpconfig import *
from timing import *
from datetime import datetime, timedelta
from playsound import playsound

#update time from timing
now = datetime.now().time()
print(now)


def assemblytime():
    global currenttime
    time = now

    while int(time.strftime("%H%M%S")) > int(assembly.strftime("%H%M%S")):
        print("Not yet time")
        time = datetime.now().time() #update time from timing
        if int(time.strftime("%H%M%S")) == int(assembly.strftime("%H%M%S")):
            initspeech.speech('Assembly Time')
            break

    currenttime = time
    return currenttime

def period():
    playsound('school-bell-sound.mp3')
    initspeech.speech("Next Period Begin")

def longbreak():
    playsound('school-bell-sound.mp3')
    initspeech.speech("Long break")

def teabreak():
    playsound('school-bell-sound.mp3')
    initspeech.speech("Short break")

def extbreak():
    playsound('school-bell-sound.mp3')
    initspeech.speech("Extension break")

def closetime():
    playsound('school-bell-sound.mp3')
    initspeech.speech("Closing Time")

