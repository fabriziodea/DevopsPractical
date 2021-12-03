from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResp(TestBase):
    def test_names(self):
        with patch('random.randint') as r:
            r.return_value.int = 2
            response = self.client.get(url_for('random_names'))
            self.assertEqual(response.status_code, 200)
#            self.assertIn(b'2', response.data)