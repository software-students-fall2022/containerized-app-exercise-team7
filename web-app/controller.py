from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
from unicodedata import name
from dotenv import dotenv_values
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_bootstrap import Bootstrap

import pymongo
import datetime
import sys
# import db as translator
import speech_recognition as sr

# instantiate the app
app = Flask(__name__)
bootstrap=Bootstrap(app)
# # load credentials and configuration options from .env file
# # if you do not yet have a file named .env, make one based on the template in env.example
# config = dotenv_values(".env")

# # turn on debugging if in development mode
# if config['FLASK_ENV'] == 'development':
#     # turn on debugging, if in development
#     app.debug = True # debug mnode


# # connect to the database
# cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
# try:
#     # verify the connection works by pinging the database
#     cxn.admin.command('ping') # The ping command is cheap and does not require auth.
#     db = cxn[config['MONGO_DBNAME']] # store a reference to the database
#     print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
# except Exception as e:
#     # the ping command failed, so the connection is not available.
#     # render_template('error.html', error=e) # render the edit template
#     print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
#     print('Database connection error:', e) # debug

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
    transcript = ""
    """
    Route for the home page
    """
    if request.method == "POST":
        # print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return render_template('home.html', error=True)
        
        file = request.files["file"]
        if file.filename == "":
            return render_template('home.html', error=True)

        if file:
            try:
                recognizer = sr.Recognizer()
                audioFile = sr.AudioFile(file)
                with audioFile as source:
                    data = recognizer.record(source)
                transcript = recognizer.recognize_google(data, key=None)
            except:
                return render_template('home.html', error=True)
            return render_template('home.html', transcript=transcript, cont=True)

        
    return render_template('home.html') # render the home template

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client["lang"]
    return db

@app.route('/languages', methods=['GET', 'POST'])
def get_languagess():
    if request.method=='GET':
        # do something with translation maybe and voice recording
        return render_template('languages.html')
    if request.method=='POST':
        db=""
        try:
            db = get_db()
            languages = db.langs.find()
            language = [{"id": langs["_id"], "lang": langs["lang"], "code": langs["code"]} for langs in languages]
            #return render_template('languages.html', languages-languages)
            return jsonify({"languages": language})
        except:
            pass
        finally:
            if type(db)==MongoClient:
                db.close()

#(NOTDONE)
#route for translating the recognized audio file input using machine learning
@app.route('/translate', methods = ["GET", "POST"])
def translate():
    return render_template('translate.html')

if __name__ == "__main__":
    app.run(debug=True, threaded = True)
