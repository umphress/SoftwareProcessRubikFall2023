import unittest
import app as app

class AppTest(unittest.TestCase):


    def test_app_010_shouldReturnDeveloperName(self):
        myName = 'umphrda'
        self.assertIn(myName, app.about())