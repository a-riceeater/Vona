import speech_recognition as sr
import sys 
import os
sys.path.append(os.path.abspath("./modules"))
from speech import speech
import datetime


active = False

def process_command(words):
    global active

    if "hey siri" in words and not active:
        speech("how may I help you?")
        active = True
    elif active:
        if "time" in words:
            now = datetime.datetime.now()
            speech("It is currently " + str(now.time()))



def listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        with microphone as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            recognized_words = recognizer.recognize_google(audio)
            print("You said:", recognized_words)
            process_command(recognized_words.lower())

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error: {0}".format(e))

if __name__ == "__main__":
    listen()
