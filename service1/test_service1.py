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
        db.session.add(Winners(name='Old Yellow Donkey'))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResp(TestBase):
    def test_race(self):
        with requests_mock.Mocker() as g:
            g.get("http://service2:5001/randomnames", text = "25")
            g.get("http://service3:5002/winner", text = "6")

            dict={'1':'Noisy Purple', '2':'Mean Green', '3':'Smart Blue', '4':'Noisy Blue', '5':'Stubborn Red', '6':'Quiet Green', '7':'Dangerous Blue', '8':'Noisy Yellow', '9':'Dangerous Blue'}
            g.post("http://service4:6000/racelist", json=dict)
            
            response = self.client.get(url_for('race'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Race', response.data)
            self.assertIn(b'Smart Blue', response.data)
            self.assertIn(b'Stubborn Red', response.data)

    def test_hall(self):
        response = self.client.get(url_for('hall'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Old', response.data)

    def test_results_lost(self):
        response = self.client.get(url_for('results', bet='Fast Red'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sorry', response.data)

    def test_results_won(self):
        response = self.client.get(url_for('results', bet='Old Yellow'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Congratulations', response.data)

