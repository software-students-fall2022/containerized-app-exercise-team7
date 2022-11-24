import pymongo
from flask import Flask
import deep_translator
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

'''
#this function record audio and saves it to a file
def record(file_name):
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
'''
# ^^ the above function may no longer be necessary
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

        print("Did you say: "+text)
        #the engine will speak whatever the user says
        recognize(text)
    '''
    with input as source:
        audio = r.record(source)
    return audio
    '''
recognize("Say something you would like to be translated")
