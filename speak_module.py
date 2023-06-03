from gtts import gTTS
from playsound import playsound


def speak(text):
    tts = gTTS(text)
    tts.save('hello.mp3')
    playsound('hello.mp3')
