from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

# set up the routes

# route for the home page
def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client["lang"]
    return db
@app.route('/')
def home():
    """
    Route for the home page
    """
    return render_template("home.html")
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
