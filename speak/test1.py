# set_voice_and_say.py
import pyttsx3
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru')
tts.say('Привет! Меня зовут Рома. Я очень рад вас видеть!')
tts.runAndWait()

from espeakng import ESpeakNG
engine = ESpeakNG()
engine.voice = 'english'
engine.speed = 150
engine.say("I'd like to be under the sea. In an octopus's garden, in the shade!", sync=True)
engine.speed = 100
engine.pitch = 32
engine.voice = 'russian'
engine.say('Привет! Меня зовут Рома. Я очень рад вас видеть!', sync=True)