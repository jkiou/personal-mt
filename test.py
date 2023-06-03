from playsound import playsound
from gtts import gTTS
tts = gTTS('hello')
tts.save('hello.mp3')
playsound('/path/to/a/sound/file/you/want/to/play.mp3')