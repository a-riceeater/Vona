from gtts import gTTS 
import os
from playsound import playsound 

def speech(text):
    obj = gTTS(text=text, lang="en", slow=False)
    obj.save("speech.mp3")
    playsound("speech.mp3")
    os.remove("speech.mp3")