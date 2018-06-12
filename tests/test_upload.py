"""
ccextractor-web | TestUpload.py

Author   : Saurabh Shrivastava
Email    : saurabh.shrivastava54+ccextractorweb[at]gmail.com
Link     : https://github.com/saurabhshri

"""
import unittest
from run import app, createConfig


class TestUpload(unittest.TestCase):

    def setUp(self):
        createConfig()

    def test_if_without_login_redirected_to_login_page(self):
        response = app.test_client().get('/upload')
        self.assertEqual(response.status_code, 302)
        self.assertIn(b'<a href="/login?next=mod_dashboard.upload">/login?next=mod_dashboard.upload</a>', response.data)
