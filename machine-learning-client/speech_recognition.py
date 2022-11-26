from flask import Flask
import speech_recognition as sr
import pyttsx3
import pyaudio
import wave
import sys

#app = Flask(__name__)
#app.secret_key = "secret key"

# need to fill out
#client = pymongo.MongoClient("")
#db=client["team7"]

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
# p used for audio input
p = pyaudio.PyAudio()
# r used for speech recognition
r = sr.Recognizer()

# the following function takes in audio and converts it to text - the "command" input 
# is input that is said to the user and what ever the user speaks is repeated back to
# them
def recognize(command):
    #this function translates the audio file to text
    #Initalize the engine (gotten from https://www.simplilearn.com/tutorials/python-tutorial/speech-recognition-in-python)
    engine = pyttsx3.init()
    # engine will speak "command"
    engine.say(command)
    engine.runAndWait()
    #input = sr.AudioFile(command +".wav")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.1)
        audio = r.listen(source)

        text = r.recognize_google(audio)
        text = text.lower()

        if text=="stop":
            return
        print("Did you say: "+text)
        #the engine will speak whatever the user says
        recognize(text)
    '''
    with input as source:
        audio = r.record(source)
    return audio
    '''

