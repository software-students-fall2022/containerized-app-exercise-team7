from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
from unicodedata import name
from dotenv import dotenv_values
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_bootstrap import Bootstrap
import speech_recognition as sr
import sys
import os
import trans
import importlib  
import itertools


import pymongo
import datetime
import sys
#import speech_recognition as sr

# instantiate the app
app = Flask(__name__)
bootstrap=Bootstrap(app)

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#input_audio = myclient["input_audio"]
#lang = myclient["language"]

# load credentials and configuration options from .env file
# if you do not yet have a file named .env, make one based on the template in env.example
config = dotenv_values(".env")

# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode


# connect to the database
cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[config['MONGO_DBNAME']] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    # render_template('error.html', error=e) # render the edit template
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e) # debug

transcript = ""
def db_init():
    db.langs.insert_many([{"lang": "Bulgarian","code": "bg"},
                    {"lang": "Czech","code": "cs"},
                    {"lang": "Danish","code": "da"},
                    {"lang": "German","code": "de"},
                    {"lang": "Greek","code": "el"},
                    {"lang": "English","code": "en"},
                    {"lang": "Spanish","code": "es"},
                    {"lang": "Estonian","code": "et"},
                    {"lang": "Finnish","code": "fi"},
                    {"lang": "French","code": "fr"},
                    {"lang": "Hungarian","code": "hu"},
                    {"lang": "Italian","code": "it"},
                    {"lang": "Japanese","code": "ja"},
                    {"lang": "Lithuanian","code": "lt"},
                    {"lang": "Latvian","code": "lv"},
                    {"lang": "Dutch","code": "nl"},
                    {"lang": "Polish","code": "pl"},
                    {"lang": "Portuguese","code": "pt-BR"}, 
                    {"lang": "Portuguese","code": "pt-PT"},
                    {"lang": "Romanian","code": "ro"},
                    {"lang": "Russian","code": "ru"},
                    {"lang": "Slovak","code": "sk"},
                    {"lang": "Slovenian","code": "sl"},
                    {"lang": "Swedish","code": "sv"},
                    {"lang": "Turkish","code": "tr"},
                    {"lang": "Ukrainian","code": "uk"},
                    {"lang": "Chinese","code": "zh-CN"},
                    ])

# #********** All Variables ***********************************#
# currentUser = "-1"
# def setvalue(n):
#      global currentUser
#      currentUser=n

#****************** All Routes ******************************#
# (DONE)
#route for homepage 
#Takes in a audio file and display the transcript
@app.route('/', methods = ["GET", "POST"])
def home():
    """
    Route for the home page
    """
    db_init()
    inp = db.langs.find({})
    out = db.langs.find({})
    if request.method == "POST":
        # print("FORM DATA RECEIVED")
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
            file = 'audio.wav'
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            global transcript 
            transcript = recognizer.recognize_google(data, key=None)
            
        print('file uploaded successfully')
        #return render_template('home.html')
    return render_template('home.html', inp=inp, out=out)

#route for translating the recognized audio file input using machine learning

@app.route('/translate', methods = ["GET", "POST"])
def translate():
    inp = request.form.get('input')
    out = request.form.get('output')
    src = db.langs.find_one({"lang": str(inp)})
    targ = db.langs.find_one({"lang": str(out)})
    s = src["code"]
    t = targ["code"]

    in_out = trans.trans(transcript, s, t)
    return render_template('translate.html', in_out=in_out, transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded = True)
