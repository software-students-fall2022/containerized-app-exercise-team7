import unittest
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

    def test_db_connect(self):
        self.setUp()
        response = self.client.get('/', follow_redirects=True)
        db=get_db(0)
        assert db.command("buildinfo")

    def test_db_collection(self):
        self.setUp()
        response = self.client.get('/', follow_redirects=True)
        db=get_db(0)
        assert db.list_collection_names()==["langs"]
    
    def test_db_languages(self):
        self.setUp()
        response = self.client.get('/', follow_redirects=True)
        db=get_db(0)
        assert db.langs.find({"lang": "English", "code": "en"})
        assert db.langs.find({"lang": "Spanish", "code": "es"})
        assert db.langs.find({"lang": "French", "code": "fr"})
        assert db.langs.find({"lang": "Japanese", "code": "ja"})
        assert db.langs.find({"lang": "Chinese", "code": "zh-CN"})
   
    def test_home_connect(self):
        self.setUp()
        response = self.client.get('/', follow_redirects=True)
        assert response.status_code == 200