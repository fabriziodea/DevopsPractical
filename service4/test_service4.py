from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResp(TestBase):
    def test_racelist(self):
        dict={'1':'11', '2':'22', '3':'33', '4':'44', '5':'55', '6':'66', '7':'77', '8':'88', '9':'5'}
        response = self.client.post(url_for('racelist'), json=dict)


        self.assertIn(b'Smart', response.data)
        self.assertIn(b'Red', response.data)
        self.assertEqual(response.status_code, 200)