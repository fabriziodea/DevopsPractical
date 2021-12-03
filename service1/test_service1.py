from flask import url_for
from flask_testing import TestCase
import requests_mock
import pytest
from application import app, db
from application.models import Winners

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db", DEBUG=True)
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Winners(name='old yellow beast'))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResp(TestBase):
    def test_race(self):
        with requests_mock.Mocker() as g:
            g.get("http://service2:5001/randomnames", text = "25")
            g.get("http://service3:5002/winner", text = "6")

            dict={'1':'Noisy purple', '2':'Mean green', '3':'Smart blue', '4':'Noisy blue', '5':'Stubborn red', '6':'Quiet green', '7':'Dangerous blue', '8':'Noisy yellow', '9':'Dangerous blue'}
            g.post("http://service4:6000/racelist", json=dict)
            
            response = self.client.get(url_for('race'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Race', response.data)
            self.assertIn(b'Smart blue', response.data)
            self.assertIn(b'Stubborn red', response.data)

    def test_hall(self):
        response = self.client.get(url_for('hall'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'old', response.data)

    def test_results_lost(self):
        response = self.client.get(url_for('results', bet='Fast red'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sorry', response.data)

    def test_results_won(self):
        response = self.client.get(url_for('results', bet='Dangerous blue'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Congratulations', response.data)

