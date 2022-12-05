import unittest
import trans
import speech_recognition as sr
from flask import current_app
from controller import app,get_db



class Test_Web_App(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client=self.app.test_client()

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None
        
    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_home_get_connect(self):
        self.setUp()
        response = self.client.get('/', follow_redirects=True)
        assert response.status_code == 200

    def test_home_get_langs(self):
        self.setUp()
        response = self.client.get('/', follow_redirects=True)
        text=response.get_data(as_text=True)
        db=get_db(0)
        cursor = db.langs.find({})
        for document in cursor:
            assert document['lang'] in text

    def test_home_get_functionality(self):
        self.setUp()
        response = self.client.get('/', follow_redirects=True)
        text=response.get_data(as_text=True)
        content=["Record","Pause","Stop",
                    "Record Audio",
                    "Format: start recording to see sample rate",
                    "Select",
                    "Upload",
                    "Output Language",
                    "Translate"]
        str1="next to the audio you would like to translate and select the language you would like to translate the recording to."
        list_str1=str1.split()
        content+=list_str1
        for item in content:
            assert item in text

    def test_dashboard_connect(self):
        self.setUp()
        reponse=self.client.get('/dashboard')
        assert reponse.status_code==200

    def test_dashboard_connect(self):
        self.setUp()
        reponse=self.client.get('/dashboard',follow_redirects=True)
        text=reponse.get_data(as_text=True)
        assert "Translation History" in text

    def test_dashboard_delete(self):
        self.setUp()
        reponse=self.client.get('/dashboard/delete')
        assert reponse.status_code==200

    def test_post_translate(self):
        self.setUp()
        f=open("test.wav","rb")
        db = get_db(0)
        entries = db.langs.find({})
        self.client.post('/',data={"audio_data":f},follow_redirects=True)
        for cur in entries:
            response=self.client.post('/translate',data={"output":cur["lang"]},follow_redirects=True)
            text=response.get_data(as_text=True)
            out_text = trans.trans("hello", "en", cur["code"])
            assert out_text in text

