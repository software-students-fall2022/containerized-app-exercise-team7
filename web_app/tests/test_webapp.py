import unittest
from flask import current_app
from controller import app,get_db,get_transcript



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

    def test_home__get_connect(self):
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

    def test_post_translate_Chinese(self):
        self.setUp()
        f=open("test.wav","rb")
        self.client.post('/',data={"audio_data":f},follow_redirects=True)
        transcript=get_transcript("hello")
        response=self.client.post('/translate',data={"output":"Chinese"},follow_redirects=True)
        text=response.get_data(as_text=True)
        assert "你好" in text


