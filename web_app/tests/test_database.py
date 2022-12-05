import unittest
from flask import current_app
from controller import app, get_db



class Test_Web_App(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()


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
        db = get_db(0)
        db_text = get_db(1)
        assert db.command("buildinfo")
        assert db_text.command("buildinfo")


    def test_db_collection(self):
        self.setUp()
        response = self.client.get('/', follow_redirects=True)
        db_lang = get_db(0)
        assert db_lang.list_collection_names() == ["langs"]


    def test_db_languages(self):
        self.setUp()
        response = self.client.get('/', follow_redirects=True)
        db = get_db(0)
        assert db.langs.find({"lang": "Bulgarian", "code": "bg"})
        assert db.langs.find({"lang": "Czech", "code": "cs"})
        assert db.langs.find({"lang": "Danish", "code": "da"})
        assert db.langs.find({"lang": "German", "code": "de"})
        assert db.langs.find({"lang": "Greek", "code": "el"})
        assert db.langs.find({"lang": "English", "code": "en"})
        assert db.langs.find({"lang": "Spanish", "code": "es"})
        assert db.langs.find({"lang": "Estonian", "code": "et"})
        assert db.langs.find({"lang": "Finnish", "code": "fi"})
        assert db.langs.find({"lang": "Hungarian", "code": "hu"})
        assert db.langs.find({"lang": "Italian", "code": "it"})
        assert db.langs.find({"lang": "Lithuanian", "code": "lt"})
        assert db.langs.find({"lang": "Latvian", "code": "lv"})
        assert db.langs.find({"lang": "Dutch", "code": "nl"})
        assert db.langs.find({"lang": "Polish", "code": "pl"})
        assert db.langs.find({"lang": "Portuguese (Brazil)", "code": "pt-BR"})
        assert db.langs.find({"lang": "Portuguese (Portugal)", "code": "pt-PT"})
        assert db.langs.find({"lang": "Romanian", "code": "ro"})
        assert db.langs.find({"lang": "Russian", "code": "ru"})
        assert db.langs.find({"lang": "Slovak", "code": "sk"})
        assert db.langs.find({"lang": "Slovenian", "code": "sl"})
        assert db.langs.find({"lang": "Swedish", "code": "sv"})
        assert db.langs.find({"lang": "Turkish", "code": "tr"})
        assert db.langs.find({"lang": "Ukrainian", "code": "uk"})
        assert db.langs.find({"lang": "French", "code": "fr"})
        assert db.langs.find({"lang": "Japanese", "code": "ja"})
        assert db.langs.find({"lang": "Chinese", "code": "zh-CN"})

