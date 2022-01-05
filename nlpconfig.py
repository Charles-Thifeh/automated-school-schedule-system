import pyttsx3

engine = pyttsx3.init()

# voice type
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)

# rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

class initspeech:
    def speech(b):
        engine.say(b)
        engine.runAndWait()

